import re
import torch

from collections import Counter
from torch import Tensor
from torch.nn import functional as F
from copy import deepcopy


def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def equality_metric(preds: Tensor, target: Tensor):
    return torch.sum(preds.cpu() == target.cpu()) / len(target)


def classification_metric(preds: Tensor, target: Tensor):
    return torch.sum(torch.argmax(preds, dim=1).cpu() == target.cpu()) / len(target)


def argmax_metric(preds: Tensor, target: Tensor):
    return torch.sum(torch.argmax(preds, dim=1).cpu() == torch.argmax(target, dim=1).cpu()) / len(target)


def binarize(tensor: Tensor, threshold=0.5):
    return tensor.where(tensor > threshold, 0.0).where(tensor <= threshold, 1.0)


def binary_metric(preds: Tensor, target: Tensor, threshold=0.5):
    preds = binarize(preds, threshold=threshold)
    return torch.sum(target == preds) / len(preds)


def mae_metric(preds: Tensor, target: Tensor):
    return torch.mean(torch.abs(preds - target))


def top_metric(preds: Tensor, target: Tensor, n_top=3, metric=mae_metric):
    top_indices = torch.topk(target, n_top).indices
    return metric(preds[top_indices], target[top_indices]) / n_top


def mean(arr):
    return sum(arr) / len(arr)


def evaluate(model, dataloader, loss_fn, accuracy_fn, device):
    model.eval()
    
    losses = []
    accuracies = []
    
    for i, batch in enumerate(dataloader):
        x_batch = batch[0].to(device)
        y_batch = batch[1].to(device)
        with torch.no_grad():
            logits = model(x_batch)
            loss = loss_fn(logits, y_batch)
            losses.append(loss.item())
            
            accuracy = accuracy_fn(logits, y_batch)
            accuracies.append(accuracy.item())
    return mean(accuracies), mean(losses)


def train(model, loss_fn, optimizer, train_dataloader, val_dataloader, n_epochs, accuracy_fn, device, logging_period=500, must_improve=False):
    # цикл обучения сети
    model.to(device)
    prev_val_accuracy = 0
    epoch = 1
    while epoch <= n_epochs:
        if must_improve:
            prev_model = deepcopy(model)
        print(f"Epoch: {epoch}")
        model.train(True)
        losses = []
        accuracies = []
        n_iterations = len(train_dataloader)
        for i, batch in enumerate(train_dataloader):
            x_batch = batch[0].to(device)
            y_batch = batch[1].to(device)
            # forward pass (получение ответов на батч)
            logits = model(x_batch)
            # вычисление лосса от выданных сетью ответов и правильных ответов на батч
            loss = loss_fn(logits, y_batch)
            loss.backward()  # backpropagation (вычисление градиентов)
            optimizer.step()  # обновление весов сети
            optimizer.zero_grad()  # обнуляем веса
            losses.append(loss)
            with torch.no_grad():
                accuracy = accuracy_fn(logits, y_batch)
                accuracies.append(accuracy.item())
                # Логирование результатов
                if (i + 1) % logging_period == 0 or i + 1 == n_iterations:
                    i_from = max(0, i - logging_period)
                    print(f"Mean train accuracy and loss on {i_from + 1}-{i + 1}/{n_iterations} iterations: {mean(accuracies[i_from:i])} {mean(losses[i_from:i])}")
        # после каждой эпохи получаем метрику качества на валидационной выборке
        model.train(False)
        val_accuracy, val_loss = evaluate(model, val_dataloader, loss_fn, accuracy_fn, device)
        if must_improve and val_accuracy < prev_val_accuracy:
            print("Got no progress this time. Restarting the epoch...")
            model = prev_model
            continue
        prev_val_accuracy = val_accuracy
        print(f"Epoch {epoch}/{n_epochs}: mean accuracy and val loss: {val_accuracy} {val_loss}")
        epoch += 1
    return model


def predict(model, x_batch, device):
    model.eval()
    x_batch = x_batch.to(device)
    with torch.no_grad():
        logits = model(x_batch)
    return logits.cpu().detach().numpy()


def get_predictions(model, dataloader, device):
    model.eval()
    predicted_labels = []
    for i, batch in enumerate(dataloader):
        x_batch = batch[0].to(device)
        with torch.no_grad():
            logits = model(x_batch)
            predicted_labels.append(logits)
    return torch.cat(predicted_labels)


def get_char_vocabulary(texts):
    return [key for key, _ in Counter("".join(texts)).most_common()]


def get_word_vocabulary(texts):
    return [key for key, _ in Counter(" ".join(texts).split()).most_common()]


def pattern_from_tokens(tokens):
    return r"(" + r"|".join([r"(" + r"|".join([re.escape(c) for c in token]) + r")" if len(token) > 1 else re.escape(token[0]) for token in tokens]) + r")"


def split_into_tokens(text, pattern):
    return [c for c in re.split(pattern, text) if c]


def int_to_one_hot(number, n_classes):
    return F.one_hot(torch.arange(n_classes), n_classes)[number]

