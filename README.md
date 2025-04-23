# Update-Helper

Ein einfaches Tool zur Verwaltung von System-Updates mit verschiedenen AUR-Helfern.

## Beschreibung

Update-Helper ist ein Dienstprogramm für Arch Linux und verwandte Distributionen, das den Prozess der Systemaktualisierung mit verschiedenen AUR-Helfern (Yay, Paru, Pamac) vereinfacht.

## Installation

1. Klone das Repository oder lade die Dateien herunter
2. Stelle sicher, dass die erforderlichen Verzeichnisse und Dateien vorhanden sind:
   - `settings/` Verzeichnis
   - `AUR-Helpers/` Verzeichnis mit den entsprechenden Python-Skripten

## Verwendung

### Erster Start

- Sicherstellen das du Python3 hast.
- dann fuehre diesen Command aus: ```python3 startup.py```

Beim ersten Start führt das Programm durch eine Einrichtung:
1. Sprachauswahl (Deutsch oder Englisch)
2. Auswahl des bevorzugten AUR-Helfers (Yay, Paru oder Pamac)

### Desktop-Datei einrichten

Um den Update-Helper einfach starten zu können, erstelle eine Desktop-Datei:

1. Kopiere die `updater.desktop` Datei in das lokale Anwendungsverzeichnis:
   ```
   cp updater.desktop ~/.local/share/applications/
   ```

2. Bearbeite die Datei, um den korrekten Pfad anzugeben:
   - Setze `Path=/pfad/zum/update-helper`
   - Setze `Exec=python3 /pfad/zum/update-helper/startup.py`
   - Setze `Icon=/pfad/zum/icon` (optional)

3. Mache die Desktop-Datei ausführbar:
   ```
   chmod +x ~/.local/share/applications/updater.desktop
   ```

Alternativ für systemweite Installation:
1. Kopiere die Dateien nach `/opt/Update-Helper/`
2. Kopiere die Desktop-Datei nach `/usr/share/applications/`

## Du hast einen Fehler gefunden oder ein Verbesserung Vorschlag? Melde dich gerne bei mir!
---

# Update-Helper

A simple tool for managing system updates with various AUR helpers.

## Description

Update-Helper is a utility for Arch Linux and related distributions that simplifies the process of system updating using various AUR helpers (Yay, Paru, Pamac).

## Installation

1. Clone the repository or download the files
2. Ensure the required directories and files are present:
   - `settings/` directory
   - `AUR-Helpers/` directory with the appropriate Python scripts

## Usage

### First Run

- Have python3 installed
- run the command: ```python3 startup.py```

On first run, the program guides you through a setup process:
1. Language selection (German or English)
2. Selection of preferred AUR helper (Yay, Paru, or Pamac)

### Setting up the Desktop File

To easily launch the Update-Helper, set up a desktop file:

1. Copy the `updater.desktop` file to the local applications directory:
   ```
   cp updater.desktop ~/.local/share/applications/
   ```

2. Edit the file to specify the correct path:
   - Set `Path=/path/to/update-helper`
   - Set `Exec=python3 /path/to/update-helper/startup.py`
   - Set `Icon=/path/to/icon` (optional)

3. Make the desktop file executable:
   ```
   chmod +x ~/.local/share/applications/updater.desktop
   ```

Alternatively, for system-wide installation:
1. Copy the files to `/opt/Update-Helper/`
2. Copy the desktop file to `/usr/share/applications/`


### Pamac currently not Supported.
