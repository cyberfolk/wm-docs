<img src="raw/loghi/logo2.svg" align="right" height="70"/>

# WM Docs

? **Initial commit**: 04/05/25  
? **Stack**: Python, CSS, YAML, MD, mkdocs

## ? Struttura del progetto

- `mkdocs.yml`: file di configurazione principale di MkDocs.
- `requirements.txt`: elenco delle dipendenze Python.
- `docs/`: cartella con i file Markdown della documentazione.
- `raw/`: cartella per dati grezzi o file di supporto (scopo non definito).
- `.github/workflows/`: file YAML per GitHub Actions.
- `add_pwd.py`: script Python (possibile gestione password o credenziali).
- `encryptcontent.cache`: file cache generato dal plugin per cifratura.

## ?? Installazione e avvio

```bash
git clone https://github.com/cyberfolk/wm-docs.git
cd wm-docs

# (Opzionale) crea ambiente virtuale
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt

# Avvia server di sviluppo
mkdocs serve
```

Apri il browser su `http://127.0.0.1:8000/` per visualizzare la documentazione.

## ? Deployment su GitHub Pages

Il progetto include GitHub Actions per il deployment automatico. 
Verifica che il branch `gh-pages` sia abilitato nelle impostazioni della repository.

## ? Cifratura dei contenuti

Il file `encryptcontent.cache` indica l'uso di `mkdocs-encryptcontent-plugin`, ma la configurazione completa non è esplicitata in `mkdocs.yml`.

## ? Note finali

- La repository manca di un `README.md` esplicativo.
- Sarebbe utile aggiungere istruzioni e descrizioni più dettagliate per chiarire lo scopo del progetto.
