# fastapi-system-monitor

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)

## 📌 Panoramica & Obiettivi
`fastapi-system-monitor` evolve il precedente sistema di monitoraggio basato su file CSV in un backend moderno, scalabile e interattivo. L'obiettivo principale è esporre le metriche di sistema tramite un'architettura **RESTful**, sfruttando la validazione rigorosa dei dati e l'interfaccia di documentazione automatica.

### Obiettivi chiave:
* **Transizione da File a API**: Abbandonare la persistenza locale su CSV a favore di un'architettura orientata ai servizi (pronta per l'integrazione con un database relazionale).
* **Documentazione Automatica**: Sfruttare la generazione nativa delle specifiche OpenAPI (Swagger UI) per testare gli endpoint in tempo reale.
* **Validazione Robusta**: Utilizzare Pydantic per garantire che i payload di richieste e risposte rispettino schemi di dati rigorosi e tipizzati.

## 🛠️ Tech Stack
* **Linguaggio**: Python 3.13
* **Framework Web**: FastAPI
* **Server ASGI**: Uvicorn
* **Raccolta Dati**: Psutil
* **Validazione Dati**: Pydantic
* **Documentazione API**: Swagger UI & ReDoc

## 📂 Project Structure
```text
fastapi-system-monitor/
│
├── main.py                # Punto di ingresso dell'applicazione e rotte API
├── pyproject.toml         # Gestione delle dipendenze e configurazione (uv)
└── README.md              # Documentazione del progetto