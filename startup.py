import subprocess
import os

def Deutsch():
    aurhelper_deu = input(
        """Bitte wähle deinen Package manager.
1. Yay
2. Paru
3. pamac
              
Bitte die nummer eingeben: """
    )

    # Write AUR helper choice to file
    with open("settings/aur-helper.txt", "w") as aur_helper_file:
        if aurhelper_deu == "1":
            aur_helper_file.write("yay")
        elif aurhelper_deu == "2":
            aur_helper_file.write("paru")
        elif aurhelper_deu == "3":
            aur_helper_file.write("pamac")
        else:
            print("Ungültige Eingabe. Yay wird als Standard verwendet.")
            aur_helper_file.write("yay")

    # Set first-setup to false after completion
    with open("settings/first-setup.txt", "w") as first_setup_file:
        first_setup_file.write("false")

    with open("settings/aur-helper.txt", "r") as check_aur_helper:
        get_checker_filer = check_aur_helper.read().strip()

    if get_checker_filer == "yay":
        os.system('python3 AUR-Helpers/yay.py')
      
    elif get_checker_filer == "paru":
        os.system('python3 AUR-Helpers/paru.py')
      
    elif get_checker_filer == "pamac":
        os.system('python3 AUR-Helpers/pamac.py')


def English():
    aurhelper_eng = input(
        """Please choose your package manager.
1. Yay
2. Paru
3. pamac
              
Please enter the number: """
    )

    # Write AUR helper choice to file
    with open("settings/aur-helper.txt", "w") as aur_helper_file:
        if aurhelper_eng == "1":
            aur_helper_file.write("yay")
        elif aurhelper_eng == "2":
            aur_helper_file.write("paru")
        elif aurhelper_eng == "3":
            aur_helper_file.write("pamac")
        else:
            print("Invalid input. Using yay as default.")
            aur_helper_file.write("yay")

    # Set first-setup to false after completion
    with open("settings/first-setup.txt", "w") as first_setup_file:
        first_setup_file.write("false")


class Banners:
    setup = """
    
███████╗██╗██████╗ ███████╗████████╗    ███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██║██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
█████╗  ██║██████╔╝███████╗   ██║       ███████╗█████╗     ██║   ██║   ██║██████╔╝
██╔══╝  ██║██╔══██╗╚════██║   ██║       ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
██║     ██║██║  ██║███████║   ██║       ███████║███████╗   ██║   ╚██████╔╝██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
                                                                                  
"""


with open("settings/first-setup.txt", "r") as first_setup_file:
    get_setup_file = first_setup_file.read().strip()

if get_setup_file == "true":
    print(Banners.setup)

    print("Welcome, this is you're first Setup. I hope. Lets Begin!")

    set_language = input(
        """Please select an Language. Input an Country Code listed above.
                         1. DE
                         2. EN
    """
    )

    if set_language.lower() == "en":
        language = open("settings/language.txt", "w")
        language.write("en")
        language.close()
        English()
    elif set_language.lower() == "de":
        language = open("settings/language.txt", "w")
        language.write("de")
        language.close()
        Deutsch()
elif get_setup_file == "false":
    with open("settings/aur-helper.txt", "r") as get_helper:
        check_helper = get_helper.read().strip()

        if check_helper == "yay":
            os.system('python3 AUR-Helpers/yay.py')
        
        elif check_helper == "pamac":
            os.system('python3 AUR-Helpers/pamac.py')

        elif check_helper == "paru":
            os.system('python3 AUR-Helpers/paru.py')