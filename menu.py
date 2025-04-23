import subprocess
import os

class NormalBanners:
    yay = """

██╗   ██╗ █████╗ ██╗   ██╗
╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝
 ╚████╔╝ ███████║ ╚████╔╝ 
  ╚██╔╝  ██╔══██║  ╚██╔╝  
   ██║   ██║  ██║   ██║   
   ╚═╝   ╚═╝  ╚═╝   ╚═╝   
                          
"""

    paru = """

██████╗  █████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██║   ██║
██████╔╝███████║██████╔╝██║   ██║
██╔═══╝ ██╔══██║██╔══██╗██║   ██║
██║     ██║  ██║██║  ██║╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                 
"""

    pamac = """

██████╗  █████╗ ███╗   ███╗ █████╗  ██████╗
██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔════╝
██████╔╝███████║██╔████╔██║███████║██║     
██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══██║██║     
██║     ██║  ██║██║ ╚═╝ ██║██║  ██║╚██████╗
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝
                                           
"""

class DE_BANNERS:
    Start_Menu = """

 ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗███╗   ██╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝████╗  ██║
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║█████╗  ██╔██╗ ██║
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║╚██╗██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████╗██║ ╚████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝
                                                                  
"""

    Sprache_Menu = """

███████╗██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝
███████╗██████╔╝██████╔╝███████║██║     ███████║█████╗  
╚════██║██╔═══╝ ██╔══██╗██╔══██║██║     ██╔══██║██╔══╝  
███████║██║     ██║  ██║██║  ██║╚██████╗██║  ██║███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
                                                        
"""

    Einstellungen_Menu = """

███████╗██╗███╗   ██╗███████╗████████╗███████╗██╗     ██╗     ██╗   ██╗███╗   ██╗ ██████╗ ███████╗███╗   ██╗
██╔════╝██║████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██║   ██║████╗  ██║██╔════╝ ██╔════╝████╗  ██║
█████╗  ██║██╔██╗ ██║███████╗   ██║   █████╗  ██║     ██║     ██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ██║██║╚██╗██║╚════██║   ██║   ██╔══╝  ██║     ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║██║ ╚████║███████║   ██║   ███████╗███████╗███████╗╚██████╔╝██║ ╚████║╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                                                            
"""

    AurHelper_Menu = """

 █████╗ ██╗   ██╗██████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██║   ██║██╔══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║██║   ██║██████╔╝    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║██║   ██║██╔══██╗    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║  ██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                             
"""

    EinstellungenEnt_Menu = """

███████╗██╗███╗   ██╗███████╗████████╗███████╗██╗     ██╗     ██╗   ██╗███╗   ██╗ ██████╗ ███████╗███╗   ██╗    ███████╗███╗   ██╗████████╗███████╗███████╗██████╗ ███╗   ██╗███████╗███╗   ██╗
██╔════╝██║████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██║   ██║████╗  ██║██╔════╝ ██╔════╝████╗  ██║    ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝████╗  ██║
█████╗  ██║██╔██╗ ██║███████╗   ██║   █████╗  ██║     ██║     ██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██╔██╗ ██║    █████╗  ██╔██╗ ██║   ██║   █████╗  █████╗  ██████╔╝██╔██╗ ██║█████╗  ██╔██╗ ██║
██╔══╝  ██║██║╚██╗██║╚════██║   ██║   ██╔══╝  ██║     ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║╚██╗██║    ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝  ██║╚██╗██║
███████╗██║██║ ╚████║███████║   ██║   ███████╗███████╗███████╗╚██████╔╝██║ ╚████║╚██████╔╝███████╗██║ ╚████║    ███████╗██║ ╚████║   ██║   ██║     ███████╗██║  ██║██║ ╚████║███████╗██║ ╚████║
╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝
                                                                                                                                                                                               
"""


class EN_BANNERS:
    Start_Menu = """

 ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                        
"""

    Language_Menu = """

██╗      █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗  ██████╗ ███████╗
██║     ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔══██╗██╔════╝ ██╔════╝
██║     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████║██║  ███╗█████╗  
██║     ██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔══██║██║   ██║██╔══╝  
███████╗██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                     
"""

    Settings_Menu = """

███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                
"""

    AurHelp_Menu = """

 █████╗ ██╗   ██╗██████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██║   ██║██╔══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║██║   ██║██████╔╝    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║██║   ██║██╔══██╗    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║  ██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                             
"""

    SettingsDelete_Menu = """

██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗    ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝    ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗      ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝      ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗    ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝    ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                                                                         
"""


def Settings():
    os.system("clear")
    print(EN_BANNERS.Settings_Menu)
    Settings_Selection = input(
        """Settings
1. Language
2. AUR Helper
3. Reset Settings
4. Back to Options
Input an Number to select an Setting: """
    )

    if Settings_Selection == "1":
        os.system("clear")
        print(EN_BANNERS.Language_Menu)
        LanguageEN_Select = input(
            """Select Language
1. DE
2. EN
Input an Number to select an Language: """
        )
        if LanguageEN_Select == "1":
            with open("settings/language.txt", "w") as language_DE:
                language_DE.write("de")
                language_DE.close()

            print("Successfully. Restarting Script.")
            os.system("clear")
            os.system("python3 startup.py")

        elif LanguageEN_Select == "2":
            with open("settings/language.txt", "w") as language_EN:
                language_EN.write("en")
                language_EN.close()

            print("Successfully. Restarting Script.")
            os.system("python3 startup.py")

            
    elif Settings_Selection == "2":
        os.system("clear")
        print(EN_BANNERS.AurHelp_Menu)
        AUREN_select = input(
            """Select an new Aur Helper.
1. yay
2. paru
3. pamac
Input an number to select an Aur Helper: """
        )

        if AUREN_select == "1":
            os.system("clear")
            print(NormalBanners.yay)

            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("yay")
                aur_helper.close()

                os.system("clear")
                EN_Menu()

        elif AUREN_select == "2":
            os.system("clear")
            print(NormalBanners.paru)

            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("paru")
                aur_helper.close()

                os.system("clear")
                EN_Menu()
        
        elif AUREN_select == "3":
            os.system("clear")
            print(NormalBanners.pamac)

            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("pamac")
                aur_helper.close()

                os.system("clear")
                EN_Menu()

        
    elif Settings_Selection == "3":
        os.system("clear")
        print(EN_BANNERS.SettingsDelete_Menu)
        are_you_sure = input("Are you sure? you cant undo this Proccess (y/n): ")
        if are_you_sure == "y".lower():
            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("Unknown")
                aur_helper.close()

            with open("settings/first-setup.txt", "w") as first_setup:
                first_setup.write("true")
                first_setup.close()

            with open("settings/language.txt", "w") as language:
                language.write("de")
                language.close

            print("Settings Reseted.")
            end = input(
                "Press any button to go back to the Setup or type 'exit' to exit the Program."
            )

            if end != "exit" and end != None:
                os.system("python3 startup.py")
            elif end != None and end == "exit":
                exit()

    elif Settings_Selection == "4":
        os.system("clear")
        EN_Menu()


def Einstellungen():
    os.system("clear")
    print(DE_BANNERS.Einstellungen_Menu)
    Einstellungen_Selection = input(
        """Einstellungen
1. Sprache
2. AUR Helper
3. Einstellungen Löschen
4. Zu Optionen
Schreibe die Nummer um die Einstellung zu wählen: """
    )

    if Einstellungen_Selection == "1":
        os.system("clear")
        print(DE_BANNERS.Sprache_Menu)
        SpracheDE_select = input(
            """Sprache auswählen
1. DE
2. EN
Schreibe die Nummer um die Sprache zu wählen: """
        )
        if SpracheDE_select == "1":
            with open("settings/language.txt", "w") as language_DE:
                language_DE.write("de")
                language_DE.close()

            print("Erfolgreich. Starte Skript neu.")
            os.system("clear")
            os.system("python3 startup.py")

        elif SpracheDE_select == "2":
            with open("settings/language.txt", "w") as language_EN:
                language_EN.write("en")
                language_EN.close()

            print("Successfully. Restarting Script.")
            os.system("python3 startup.py")

            
    elif Einstellungen_Selection == "2":
        os.system("clear")
        print(DE_BANNERS.AurHelper_Menu)
        AURDE_select = input(
            """wähle einen neuen Aur Helper.
1. yay
2. paru
3. pamac
Schreibe die nummer um denn Aur Helper zu wählen: """
        )

        if AURDE_select == "1":
            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("yay")
                aur_helper.close()

                os.system("clear")
                DE_Menu()
        elif AURDE_select == "2":
            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("paru")
                aur_helper.close()
                
                os.system("clear")
                DE_Menu()
        elif AURDE_select == "3":
            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("pamac")
                aur_helper.close()

                os.system("clear")
                DE_Menu()

    elif Einstellungen_Selection == "3":
        os.system("clear")
        print(DE_BANNERS.EinstellungenEnt_Menu)
        bist_du_sicher = input(
            "Bist du dir sicher? Dieser vorgang kann nicht mehr rückgängig gemacht werden (y/n): "
        )

        if bist_du_sicher == "y".lower():
            with open("settings/aur-helper.txt", "w") as aur_helper:
                aur_helper.write("Unknown")
                aur_helper.close()

            with open("settings/first-setup.txt", "w") as first_setup:
                first_setup.write("true")
                first_setup.close()

            with open("settings/language.txt", "w") as language:
                language.write("de")
                language.close()

    elif Einstellungen_Selection == "4":
        os.system("clear")
        DE_Menu()


def DE_Menu():
    print(DE_BANNERS.Start_Menu)
    DE_MENU_OPTION = input(
        """Options Menü
1. Einstellungen
2. System Updaten
3. Credits
4. Wiki
Schreibe die Nummer um die Option zu wählen: """
    )

    if DE_MENU_OPTION == "1":
        Einstellungen()

    elif DE_MENU_OPTION == "2":
        with open("settings/aur-helper.txt", "r") as aurhelper_de:
            aurhelperde_selection = aurhelper_de.read().strip()

        if aurhelperde_selection == "yay":
            os.system("python3 AUR-Helpers/yay.py")

        elif aurhelperde_selection == "paru":
            os.system("python3 AUR-Helpers/paru.py")

        elif aurhelperde_selection == "pamac":
            os.system("python3 AUR-Helpers/pamac.py")

    elif DE_MENU_OPTION == "3":
        print("the_use. (bin alleine :( )")

    elif DE_MENU_OPTION == "4":
        print("https://https://github.com/dev-print/Update-Helper/wiki")
        print("Drücke ctrl/strg und clicke auf denn Link.")
        ende = input("drücke eine Taste um die Optionen zu zeigen.")

        if ende != None:
            os.system("clear")
            DE_Menu()


def EN_Menu():
    print(EN_BANNERS.Start_Menu)
    EN_MENU_OPTIONS = input(
        """Option Menu
1. Settings
2. Update System
3. Credits
4. Wiki
Input number to select Option: """
    )

    if EN_MENU_OPTIONS == "1":
        Settings()
    elif EN_MENU_OPTIONS == "2":
        with open("settings/aur-helper.txt", "r") as aurhelper_en:
            aurhelperen_selection = aurhelper_en.read().strip()

        if aurhelperen_selection == "yay":
            os.system("python3 AUR-Helpers/yay.py")

        elif aurhelperen_selection == "paru":
            os.system("python3 AUR-Helpers/paru.py")

        elif aurhelperen_selection == "pamac":
            os.system("python3 AUR-Helpers/pamac.py")

    elif EN_MENU_OPTIONS == "3":
        print("the_use. (Alone on this one :[ )")

    elif EN_MENU_OPTIONS == "4":
        print("https://https://github.com/dev-print/Update-Helper/wiki")
        print("pres ctrl and click on the link to open it in you're Browser.")
        end = input("Press an Button to go back to the Options.")

        if end != None:
            os.system("clear")
            EN_Menu()


with open("settings/language.txt", "r") as language:
    language_selected = language.read().strip()

if language_selected == "de":
    os.system("clear")
    DE_Menu()
elif language_selected == "en":
    os.system("clear")
    EN_Menu()
