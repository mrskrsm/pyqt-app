# REQUIREMENTS
- Python 3.x
- Docker Desktop
- Hardware Virtualization attiva (per controllare, apri Gestione Attività > Prestazioni > CPU)

# SETTAGGIO
Clona/scarica questa repo e scarica l'unica dependency (`pip install -r requirements.txt`).

I file indispensabili sono quelli dentro la cartella `pyqt_project`.

Apri Docker Desktop e aspetta che Docker Engine sia online.

Apri un terminale e inserisci questi comandi:

`docker pull downloads.unstructured.io/unstructured-io/unstructured:latest`

`docker run -dt -v <pathToRepoRoot>/pyqt_project:/home/notebook-user/pyqt_project --name unstructured downloads.unstructured.io/unstructured-io/unstructured:latest`

Ora, tutti i file che sono presenti nella cartella pyqt_project saranno presenti dentro il container appena creato.

Per avviare l'applicazione, `python main.py` dalla cartella contenente main.py.

# FYI
Gli script vanno molto sul generico, di conseguenza l'esportazione sarà sporca. Fare le opportune modifiche a gli script o modificare manualmente i file .txt di output dovrebbe essere sufficiente a risolvere questo problema.

Ad ogni esportazione completata, pulire la cartella `utils` da qualsiasi file (tranne 2 file, esattamente 1 file pdf e 1 file docx. Scegli tu se togliere o no)