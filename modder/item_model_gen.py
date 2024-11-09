import os
import json


modid = "magistuarmoryaddon"
images_dir = fr"/home/lut/Java/modding/Epic-Knights-Addon-1.20.2-crossversion/common/src/main/resources/assets/{modid}/textures/item"
models_dir = fr"/home/lut/Java/modding/Epic-Knights-Addon-1.20.2-crossversion/common/src/main/resources/assets/{modid}/models/item"
results_dir = "new_files"

modelnames = os.listdir(models_dir)
imagenames = os.listdir(images_dir)
for imagename in imagenames:
    name = os.path.splitext(imagename)[0]
    if name.endswith("overlay") or name + ".json" in modelnames:
        continue
    data = {
        "parent": "item/generated",
        "textures": {
            "layer0": f"{modid}:item/{name}"
        }
    }
    if name + "_overlay.png" in imagenames:
        data["textures"]["layer1"] = f"{modid}:item/{name}_overlay"
    with open(fr"{results_dir}/{name}.json", "w") as f:
        json.dump(data, f, indent=4)

