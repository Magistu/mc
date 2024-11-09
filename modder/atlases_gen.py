import json

from sklearn.metrics import roc_auc_score

materials = ("wood", "stone", "gold", "iron", "diamond", "netherite", "tin", "copper", "silver", "bronze", "steel")
shields_0 = ("heatershield", "tartsche", "ellipticalshield", "roundshield", "pavese", "kiteshield")
shields_1 = ("target", "buckler", "rondache")

results_dir = "../files_processing/new_files"


def main():
    roc_auc_score
    
    shield_patterns = {"sources": []}
    for shield in shields_0:
        for material in materials:
            shield_patterns["sources"] += [
                {
                    "type": "single",
                    "resource": "magistuarmory:entity/" + material + "_" + shield + "_pattern"
                },
                {
                    "type": "single",
                    "resource": "magistuarmory:entity/" + material + "_" + shield + "_nopattern"
                },
                {
                    "type": "directory",
                    "source": "entity/" + shield,
                    "prefix": "entity/" + shield + "/"
                }
            ]

    for shield in shields_1:
        for material in materials:
            shield_patterns["sources"] += [
                {
                    "type": "single",
                    "resource": "magistuarmory:entity/" + material + "_" + shield + "_nopattern"
                }
            ]

    shield_patterns["sources"] += [
        {
            "type": "single",
            "resource": "magistuarmory:entity/corruptedroundshield_nopattern"
        }
    ]

    shield_patterns["sources"] += [
        {
            "type": "directory",
            "source": "entity/shield",
            "prefix": "entity/shield/"
        }
    ]

    with open(results_dir + "/shield_patterns.json", "w") as f:
        json.dump(shield_patterns, f)

    banner_patterns = {"sources": []}

    banner_patterns["sources"] += [
        {
            "type": "directory",
            "source": "magistuarmory:entity/banner",
            "prefix": "magistuarmory:entity/banner/"
        }
    ]

    with open(results_dir + "/banner_patterns.json", "w") as f:
        json.dump(banner_patterns, f)


if __name__ == "__main__":
    main()
