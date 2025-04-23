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
    git clone [https://github.com/your-username/update-helper.git](https://github.com/your-username/update-helper.git)
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

Wenn du einen Fehler findest oder einen Verbesserungsvorschlag hast, melde dich bitte im [Issue Tracker](https://github.com/your-username/update-helper/issues) des Projekts.
