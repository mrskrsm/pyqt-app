# REQUIREMENTS
- Python 3.x
- Git
- Docker Desktop
- Hardware Virtualization attiva (per controllare, apri Gestione Attività > Prestazioni > CPU)

# SETTAGGIO
Clona questa repo e scarica l'unica dependency (`pip install -r requirements.txt`)

Apri Docker Desktop e aspetta che Docker Engine sia online.

Apri un terminale e inserisci questi comandi:

`docker pull downloads.unstructured.io/unstructured-io/unstructured:latest`

`docker run -dt -v --name unstructured downloads.unstructured.io/unstructured-io/unstructured:latest`