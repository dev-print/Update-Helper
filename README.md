# Update-Helper

Ein einfaches Werkzeug zur Verwaltung von Systemaktualisierungen mit verschiedenen AUR-Helfern.

## Beschreibung

Update-Helper ist ein Dienstprogramm für Arch Linux und verwandte Distributionen, das den Prozess der Systemaktualisierung mit verschiedenen AUR-Helfern (Yay, Paru) vereinfacht. Es bietet eine benutzerfreundliche Schnittstelle, um AUR-Pakete einfach zu aktualisieren.

## Funktionen

* **Unterstützung für mehrere AUR-Helfer:** Funktioniert mit Yay und Paru.
* **Einfache Einrichtung:** Einmalige Einrichtung mit Sprachauswahl und AUR-Helfer-Auswahl.
* **Desktop-Integration:** Option zur Erstellung einer Desktop-Datei für einfachen Start.
* **Systemweite Installation möglich:** Kann sowohl lokal als auch systemweit installiert werden.

## Installation

1.  **Repository klonen oder Dateien herunterladen:**

    Klone das Repository mit Git:

    ```bash
    git clone [https://github.com/dev-print/update-helper.git](https://github.com/dev-print/update-helper.git)
    cd update-helper
    ```

    Oder lade die Dateien als ZIP-Archiv herunter und entpacke sie.

2.  **Verzeichnisse und Dateien sicherstellen:**

    Stelle sicher, dass die folgenden Verzeichnisse und Dateien vorhanden sind:

    * `settings/` Verzeichnis
    * `AUR-Helpers/` Verzeichnis mit den entsprechenden Python-Skripten

## Verwendung

### Erster Start

1.  **Python 3 installieren:**

    Stelle sicher, dass Python 3 auf deinem System installiert ist.

2.  **Skript ausführen:**

    Führe das `startup.py` Skript aus:

    ```bash
    python3 startup.py
    ```

    Beim ersten Start wirst du durch einen Einrichtungsprozess geführt:

    1.  Sprachauswahl (Deutsch oder Englisch)
    2.  Auswahl des bevorzugten AUR-Helfers (Yay oder Paru)

### Desktop-Datei einrichten

Um den Update-Helper einfach über dein Desktop-Menü zu starten, kannst du eine Desktop-Datei einrichten:

1.  **Datei kopieren:**

    Kopiere die `updater.desktop` Datei in das lokale Anwendungsverzeichnis:

    ```bash
    cp updater.desktop ~/.local/share/applications/
    ```

2.  **Datei bearbeiten:**

    Bearbeite die Datei `~/.local/share/applications/updater.desktop` mit einem Texteditor, um die korrekten Pfade anzugeben:

    * Setze `Path=/pfad/zum/update-helper` (z.B. `/home/benutzername/update-helper`)
    * Setze `Exec=python3 /pfad/zum/update-helper/startup.py` (z.B. `/home/benutzername/update-helper/startup.py`)
    * Setze `Icon=/pfad/zum/icon` (optional, Pfad zu einem Icon-Bild)

3.  **Datei ausführbar machen:**

    Mache die Desktop-Datei ausführbar:

    ```bash
    chmod +x ~/.local/share/applications/updater.desktop
    ```

### Systemweite Installation

Für eine systemweite Installation:

1.  **Dateien kopieren:**

    Kopiere die Dateien nach `/opt/Update-Helper/`:

    ```bash
    sudo cp -r . /opt/Update-Helper/
    ```

2.  **Desktop-Datei kopieren:**

    Kopiere die Desktop-Datei nach `/usr/share/applications/`:

    ```bash
    sudo cp updater.desktop /usr/share/applications/
    ```

    Passe die Pfade in der `updater.desktop` Datei entsprechend an (wie oben beschrieben).

### Pamac

**Pamac wird derzeit nicht unterstützt.** Dieses Tool ist auf die Verwendung von Yay und Paru beschränkt.

## Fehler melden und Vorschläge machen

Wenn du einen Fehler findest oder einen Verbesserungsvorschlag hast, melde dich bitte im [Issue Tracker](https://github.com/dev-print/update-helper/issues) des Projekts.

## Notizen

Hier kannst du deine persönlichen Notizen einfügen:
---

# Update-Helper

A simple tool for managing system updates with various AUR helpers.

## Description

Update-Helper is a utility for Arch Linux and related distributions that simplifies the process of system updating using various AUR helpers (Yay, Paru). It provides a user-friendly interface to easily update AUR packages.

## Features

* **Multiple AUR helper support:** Works with Yay and Paru.
* **Easy setup:** One-time setup with language selection and AUR helper choice.
* **Desktop integration:** Option to create a desktop file for easy launching.
* **System-wide installation possible:** Can be installed locally or system-wide.

## Installation

1.  **Clone repository or download files:**

    Clone the repository with Git:

    ```bash
    git clone [https://github.com/dev-print/update-helper.git](https://github.com/dev-print/update-helper.git)
    cd update-helper
    ```

    Or download the files as a ZIP archive and extract them.

2.  **Ensure directories and files are present:**

    Make sure the following directories and files exist:

    * `settings/` directory
    * `AUR-Helpers/` directory with the appropriate Python scripts

## Usage

### First Run

1.  **Install Python 3:**

    Ensure that Python 3 is installed on your system.

2.  **Run the script:**

    Execute the `startup.py` script:

    ```bash
    python3 startup.py
    ```

    On the first run, you will be guided through a setup process:

    1.  Language selection (German or English)
    2.  Selection of preferred AUR helper (Yay or Paru)

### Setting up the Desktop File

To easily launch Update-Helper from your desktop menu, you can set up a desktop file:

1.  **Copy the file:**

    Copy the `updater.desktop` file to the local applications directory:

    ```bash
    cp updater.desktop ~/.local/share/applications/
    ```

2.  **Edit the file:**

    Edit the `~/.local/share/applications/updater.desktop` file with a text editor to specify the correct paths:

    * Set `Path=/path/to/update-helper` (e.g., `/home/username/update-helper`)
    * Set `Exec=python3 /path/to/update-helper/startup.py` (e.g., `/home/username/update-helper/startup.py`)
    * Set `Icon=/path/to/icon` (optional, path to an icon image)

3.  **Make the file executable:**

    Make the desktop file executable:

    ```bash
    chmod +x ~/.local/share/applications/updater.desktop
    ```

### System-wide Installation

For a system-wide installation:

1.  **Copy the files:**

    Copy the files to `/opt/Update-Helper/`:

    ```bash
    sudo cp -r . /opt/Update-Helper/
    ```

2.  **Copy the desktop file:**

    Copy the desktop file to `/usr/share/applications/`:

    ```bash
    sudo cp updater.desktop /usr/share/applications/
    ```

    Adjust the paths in the `updater.desktop` file accordingly (as described above).

### Pamac

**Pamac is currently not supported.** This tool is limited to using Yay and Paru.

## Report Bugs and Suggestions

If you find a bug or have a suggestion for improvement, please report it in the project's [Issue Tracker](https://github.com/dev-print/update-helper/issues).

### Todos
1. Add something like noprogressbar to paru.
2. add more menu options to change the settings and more.
3. IDK
