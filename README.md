# Forum Controller Doktor

**⚠️ Archiv-Repository** - Dieses Projekt wurde nie fertiggestellt und nie veröffentlicht.

## Beschreibung

Dieses Repository enthält den Quellcode für eine geplante Forum-Erweiterung des Gewerbes **Controller Doktor** (Unternehmen meines Vaters). Das Projekt sollte eine Community-Plattform bereitstellen, wurde aber nie fertiggestellt.

Das Projekt wurde mit Hilfe von KI entwickelt, kam aber über die Entwicklungsphase nie hinaus und wurde nie öffentlich veröffentlicht.

## Ursprüngliche Vision

Das Forum sollte als Erweiterung zu Controller Doktor dienen und eine Kommunikationsplattform für die Community bieten. Es basiert auf Django und wurde als Full-Stack-Web-Anwendung konzipiert.

## Technologie-Stack

- **Python** (3%)
- **HTML** (33,3%)
- **JavaScript** (32,8%)
- **CSS** (28,5%)
- **SCSS** (2,4%)

Das Projekt basiert auf Django mit Gunicorn als WSGI-Server.

## Projektstruktur

```
forum_Controllerdoktor/
├── Forum_home/          # Frontend-Templates und statische Dateien
├── forum_controllerdoktor/  # Django-Anwendung
├── staticfiles/         # Statische Ressourcen
├── manage.py            # Django Management
└── ervice - Gunicorn Django Forum  # Gunicorn Konfiguration
```

## Status

🛑 **Archiviert - Nicht aktiv**
- Projekt wurde nie fertiggestellt
- Website ist offline
- Keine aktive Entwicklung oder Wartung

## Installation & Entwicklung

Falls du das Projekt lokal inspizieren oder weiterentwickeln möchtest:

1. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

2. **Django starten**
   ```bash
   python manage.py runserver
   ```

3. **Mit Gunicorn deployen**
   ```bash
   gunicorn forum_controllerdoktor.wsgi:application
   ```

## Lizenz

Keine spezifische Lizenz definiert.

---

**Hinweis:** Dieses Repository ist ein Archiv eines experimentellen Projekts. Es enthält Code, der mit KI-Unterstützung entwickelt wurde, aber nie zur Produktion ging.
