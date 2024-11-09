import os
import shutil
import re


class Platform:
    FABRIC = "fabric"
    FORGE = "forge"


projects_dir = "C:/Users/lut8/Java/modding/"
dest_dir = "C:/Users/lut8/OneDrive/Рабочий стол/"
project_name = "Epic-Knights-Addon"
mod_name = "Epic-Knights-Addon"
game_versions = ["1.19.2"]


# project_name = "Epic-Knights"
# mod_name = "Epic-Knights"
# game_versions = ["1.19.x"]


def get_project_dir(game_version):
    return f"{projects_dir}{project_name}-{game_version}-crossversion/"


def get_supported_game_version(archive_path):
    return re.search(r"\[(.+)]", archive_path).group(1)


def get_jar_name(platform, archive_base_name, mod_version, platform_format=False):
    supported_game_version = get_supported_game_version(archive_base_name)
    platform_info = ("-" + platform) if platform_format else ""
    return re.sub(supported_game_version, f"{supported_game_version}{platform_info}", archive_base_name) + "-" + mod_version


def get_jar_path(game_version, platform, archive_base_name, mod_version, platform_format=False):
    jar_dir = get_project_dir(game_version) + platform + "/build/libs/"
    return f"{jar_dir}{get_jar_name(platform, archive_base_name, mod_version, platform_format)}.jar"


def get_archive_base_name_and_mod_version(game_version):
    archive_base_name, mod_version = None, None
    with open(get_project_dir(game_version) + "gradle.properties") as f:
        for line in f:
            line = line.strip("\n")
            if re.fullmatch(r"archives_base_name *= *.+", line):
                archive_base_name = line.split("=")[1]
            elif re.fullmatch(r"mod_version *= *[0-9]+\.[0-9]+", line):
                mod_version = line.split("=")[1]
    if archive_base_name is None:
        raise KeyError("Archive base name not found")
    if mod_version is None:
        raise KeyError("Version not found")
    return archive_base_name, mod_version


def rename(path, new_path):
    if path != new_path and os.path.exists(new_path):
        os.remove(new_path)
    os.rename(path, new_path)


def copy(file_path, new_dir):
    new_path = new_dir + file_path.split("/")[-1]
    shutil.copy(file_path, new_path)
    return new_path


def reformat_jar(jar_path, platform):
    supported_game_version = get_supported_game_version(jar_path)
    new_path = re.sub(supported_game_version, f"{supported_game_version}-{platform}", jar_path)
    rename(jar_path, new_path)
    return new_path


def build(game_version):
    os.system("cd " + get_project_dir(game_version).replace("/", "\\") + " && gradlew build")


def main():
    for game_version in game_versions:
        # build(game_version)

        archive_base_name, mod_version = get_archive_base_name_and_mod_version(game_version)
        fabric_jar_path = get_jar_path(game_version, Platform.FABRIC, archive_base_name, mod_version)
        forge_jar_path = get_jar_path(game_version, Platform.FORGE, archive_base_name, mod_version)
        fabric_jar_path = copy(fabric_jar_path, dest_dir)
        reformat_jar(fabric_jar_path, Platform.FABRIC)
        forge_jar_path = copy(forge_jar_path, dest_dir)
        reformat_jar(forge_jar_path, Platform.FORGE)
        print(forge_jar_path)


if __name__ == "__main__":
    main()
