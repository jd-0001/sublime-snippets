import json, os

IGNORE_PKG_SETTINGS = [
    "Package Control.sublime-settings"
]

# #################################
# Helpers
# #################################


def ask_q(que):
    res =  input(que + " y/n: ")
    return "y" in res.lower()

def log_to_file(data):
    with open(f"{os.path.basename(__file__)}.log", "a") as log_file:
        log_file.write(data)
        print("\n\n")


# #################################
# Generate Installed Package List
# #################################

def gen_list_of_pkg():
    i_pack = None
    with open("Package Control.sublime-settings") as p:
        i_pack = json.loads(p.read())["installed_packages"]

    with open("installed-packages.json", "w") as i:
        i.write(json.dumps(i_pack))


# #################################
# Package Settings
# #################################

def zip_pkg_settings():
    from zipfile import ZipFile

    try:
        with ZipFile('pkg-settings.zip','w') as zip:
            for file in os.listdir(os.getcwd()):
                if file.endswith(".sublime-settings") and file not in IGNORE_PKG_SETTINGS:
                    zip.write(file)
    except Exception as e:
        log_to_file(e)


# #################################
# Main Function
# #################################

def main():

    print("Backing up installed packages...")
    gen_list_of_pkg()

    print("Below is list of ignored package settings:")
    for i in IGNORE_PKG_SETTINGS:
        print(i)

    if ask_q("Do you want me to backup above setting files? If not you have to manually create 'pkg-settings.zip' file."):
        zip_pkg_settings()


if __name__ == "__main__":
    main()