# Forum Controller Doktor

**⚠️ Archiv-Repository** - Diese Website ist offline und wird nicht mehr aktiv gepflegt.

## Beschreibung

Version Kontrolle für ein Django-basiertes Forum-Projekt. Dieses Repository enthält den quellcode des Controllerdoktor Forums, das sich nicht mehr im aktiven Betrieb befindet.

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

🛑 **Offline seit längerer Zeit** - Die Website ist nicht mehr erreichbar. Dieses Repository dient nur noch Archivierungszwecken.

## Installation & Entwicklung

Falls du das Projekt lokal revivieren möchtest:

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

**Hinweis:** Dieses Repository enthält archivierte Daten eines Projekts, das sich nicht mehr im aktiven Betrieb befindet.
