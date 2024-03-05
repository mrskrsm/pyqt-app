# REQUIREMENTS
- Python 3.x
- Git
- Docker Desktop
- Hardware Virtualization attiva (per controllare, apri Gestione Attività > Prestazioni > CPU)

# SETTAGGIO
Clona questa repo e scarica l'unica dependency (`pip install -r requirements.txt`).

I file indispensabili sono quelli dentro la cartella `pyqt_project`.

Apri Docker Desktop e aspetta che Docker Engine sia online.

Apri un terminale e inserisci questi comandi:

`docker pull downloads.unstructured.io/unstructured-io/unstructured:latest`

`docker run -dt -v <pathToRepoRoot>/pyqt_project:/home/notebook-user/pyqt_project --name unstructured downloads.unstructured.io/unstructured-io/unstructured:latest`

Ora, tutti i file che sono presenti nella cartella pyqt_project saranno presenti dentro il container appena creato.

Per avviare l'applicazione, `python main.py` dalla cartella contenente main.py.