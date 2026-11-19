Serve a dire a Python che una cartella è un package, cioè un contenitore di moduli importabili.

Moduli e package
Un modulo è un singolo file .py (es. database.py).
Un package è una cartella di moduli. Per importare from fastapi_system_monitor.core.database import engine, Python deve trattare fastapi_system_monitor e core come package.

__init__.py è il file che lo dichiara. Può essere vuoto, e nel 90% dei casi lo è.

Cosa succede quando importi

Quando importi qualcosa dal package, Python esegue il suo __init__.py la prima volta, poi carica il modulo che hai chiesto. Con l’import sopra, esegue in ordine:

fastapi_system_monitor/__init__.py
core/__init__.py
database.py

Per questo il file può anche contenere codice, ad esempio per esporre nomi in modo più corto:

python
# core/__init__.py
from .database import engine, SessionDep
# ora funziona: from fastapi_system_monitor.core import engine

Se conosci Angular/Nest, è l’equivalente di un barrel file (index.ts). In Python però la convenzione è lasciarlo vuoto e importare dal modulo preciso: è più esplicito e si capisce subito dove vive ogni cosa. Evita di metterci logica pesante o effetti collaterali, perché gira a ogni primo import (è lo stesso problema del logging.basicConfig nel vecchio models.py).

È proprio obbligatorio?

Dalla 3.3 Python accetta anche cartelle senza il file (namespace package), ed è il motivo per cui il tuo app/ funzionava. Ma quel meccanismo serve a spezzare un unico package su più cartelle. Con __init__.py hai comportamenti più prevedibili: strumenti di test, IDE e packaging riconoscono subito i tuoi package.