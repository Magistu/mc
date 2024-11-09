import json
import os


def main():
    for file in os.listdir("../files_processing/files_backup"):
        if os.path.splitext(file)[1] != ".json":
            continue

        with open("files/" + file, "r") as fin, open("new_files/" + file, "w") as fout:
            data = json.load(fin)

            data["template"] = {"item": "minecraft:netherite_upgrade_smithing_template"}
            data["type"] = "minecraft:smithing_transform"
        
            json.dump(data, fout, indent=4)


if __name__ == "__main__":
    main()
