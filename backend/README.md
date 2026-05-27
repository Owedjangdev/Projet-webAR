# Backend WebAR

Backend FastAPI du projet WebAR par QR code.

## Objectif semaine 1

Créer une API connectée à MySQL capable de retourner une expérience WebAR au frontend.

Endpoint principal :

```http
GET /api/v1/experience/{experience_id}
```

Exemple :

```http
GET /api/v1/experience/exp_001
```

## Installation locale

Activer l'environnement virtuel :

```bash
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer le fichier `.env` :

```bash
cp .env.example .env
```

Lancer le serveur :

```bash
uvicorn app.main:app --reload
```

Documentation API :

```text
http://localhost:8000/docs
```
