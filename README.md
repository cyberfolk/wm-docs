<img src="docs/img/logo.svg" align="right" height="70"/>

# WM-Docs

📅 **Initial commit**: 04/05/25  
🛠 **Stack**: Python, CSS, YAML, MD, MkDocs, GitHub Pages, GitHub Actions
🌐 **Site**: https://cyberfolk.github.io/wm-docs/

**WM-Docs** è un sito statico di documentazione creato con **MkDocs** e il tema **Material** for MkDocs. Il sito è
ospitato gratuitamente su **GitHub Pages** e configurato per il deploy automatico tramite **GitHub Actions** a ogni
push sul branch principale.

## Scelte tecniche di base

- **MkDocs** permette di scrivere documentazione in Markdown e generare un sito statico facilmente.
- **Tema Material**: Questo tema di MkDocs offre un aspetto moderno, supporta la navigazione con menu a sinistra, la
  ricerca integrata e molte funzionalità utili per documentazioni tecniche.
- **GitHub Pages**: Per pubblicare il sito statico abbiamo optato per GitHub Pages, un servizio gratuito e integrato con
  GitHub. In questo modo la documentazione è accessibile via web senza dover gestire server propri.
- **GitHub Actions**: Per evitare di dover eseguire manualmente il comando di deploy a ogni modifica, è stato
  configurato un _Workflow GitHub Actions_ che si occupa di costruire il sito statico e pubblicarlo automaticamente sul
  branch **gh-pages** a ogni push sul branch principale _(main)_. In questo modo il sito su GitHub Pages viene
  aggiornato in continuo _(Continuous Deployment)_.

## Creazione della struttura del progetto

Di seguito sono riportati i comandi e i passaggi principali eseguiti per creare da zero la struttura del progetto:

### 1. Inizializzazione dell'ambiente Python

È consigliato (anche se facoltativo) creare un ambiente virtuale Python per isolare le dipendenze. _Questo passo non è
obbligatorio, ma aiuta a mantenere pulito l’ambiente di sviluppo._

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 2. Installazione di MkDocs e Material

Abbiamo installato MkDocs e il tema Material tramite pip:

```bash
pip install mkdocs mkdocs-material
```

### 3. Creazione del progetto MkDocs

Il comando `mkdocs new .` (eseguito nella directory del repository) crea un nuovo progetto MkDocs nella cartella
corrente. In alternativa, `mkdocs new nome_progetto` creerebbe una sottocartella; Questo comando ha generato due
elementi fondamentali:

- Un file di configurazione `mkdocs.yml` con le opzioni di default.
- Una cartella `docs/` contenente un file `index.md` di esempio (home page della documentazione).

### 4. Configurazione di MkDocs

Dopo aver generato la struttura base, abbiamo modificato il file `mkdocs.yml` per personalizzare il sito:

- Impostazione di `site_name`: ad esempio, il nome del sito è stato cambiato in `"WM Docs"` (o un nome appropriato
  per il progetto).
- Configurazione del **tema Material**: nel file YAML è stata aggiunta/impostata la chiave `theme:` con
  nome `material`. In forma minima:

```yaml
theme:
  name: material
```

Questo attiva il tema Material for MkDocs. (Material permette anche molte configurazioni aggiuntive per colori,
font, ecc., che possono essere aggiunte in seguito secondo necessità).

- (Opzionale) **Configurazione plugin**: se si utilizzano plugin (come la ricerca, inclusa di default, o plugin di
  terze parti), vanno elencati nella sezione `plugins:` di `mkdocs.yml`. Ad esempio, per includere il plugin di
  cifratura contenuti, si potrebbe aggiungere:

```yaml
plugins:
  - search
  - encryptcontent:
      password: "miaPasswordDiEsempio"
```

*Nota:* Nel nostro progetto, il file `encryptcontent.cache` suggerisce che è stato installato il plugin
*mkdocs-encryptcontent-plugin* per proteggere alcune pagine con password. Tuttavia, al momento non è presente una
configurazione completa nel `mkdocs.yml` (non è ancora stata impostata una password globale o per pagina), quindi
il plugin risulta inattivo finché non viene configurato correttamente.

- Personalizzazione di altre impostazioni facoltative: ad esempio, è possibile
  impostare `site_description`, `site_author`, aggiungere un logo, modificare la struttura di navigazione (`nav:`)
  se ci sono più pagine. In questa fase iniziale, la configurazione è rimasta basilare (nome del sito e tema).

### 5. Modifica/aggiunta dei contenuti in Markdown

Il file `docs/index.md` generato automaticamente contiene un testo
di benvenuto standard ("Welcome to MkDocs"). Lo abbiamo modificato inserendo il contenuto introduttivo reale della
nostra documentazione. Inoltre, sono state create altre pagine Markdown all’interno di `docs/` a seconda delle
necessità del progetto (ad esempio, creando nuovi file `.md` per diverse sezioni della documentazione). Ogni file
Markdown aggiunto nella cartella `docs/` rappresenta una pagina del sito; per organizzare la navigazione si può
modificare la sezione `nav` in `mkdocs.yml` elencando le pagine nell'ordine desiderato. Esempio di `mkdocs.yml` con
navigazione personalizzata:

```yaml
nav:
  - Home: index.md
  - Guida utente: user-guide.md
  - API: api.md
```

(Assicurarsi che i file `user-guide.md` e `api.md` esistano in `docs/` in questo esempio.)

### 6. Verifica in locale

Per controllare il risultato e sviluppare la documentazione in tempo reale, MkDocs offre un
server di sviluppo. Dopo aver scritto o modificato le pagine, si può lanciare:

```bash
mkdocs serve
```

Questo comando genera il sito statico e avvia un server locale (di default su `http://127.0.0.1:8000/`). Aprendo
quell’URL nel browser, è possibile navigare la documentazione in locale e vedere immediatamente le modifiche
apportate ai file Markdown. Il server di sviluppo aggiorna automaticamente le pagine a ogni salvataggio (live
reload), facilitando la stesura dei contenuti.

## Struttura del progetto

La struttura principale della repository WM Docs è la seguente:

- **`mkdocs.yml`** – Il file di configurazione principale di MkDocs. Qui risiedono tutte le impostazioni del sito:
  titolo, tema, plugin, navigazione, ecc. Ogni modifica a questo file richiede un rebuild del sito.
- **`requirements.txt`** – Elenco delle dipendenze Python del progetto. Include i pacchetti necessari perché MkDocs
  generi correttamente il sito. (Utile per installare tutto con `pip install -r requirements.txt` in ambienti nuovi).
- **`docs/`** – Cartella contenente i file Markdown della documentazione. Ogni `.md` in questa directory diventa una
  pagina del sito. Ad esempio, `docs/index.md` corrisponde alla home page.
- **`raw/`** – Cartella per dati "grezzi" o file di supporto (lo scopo preciso dipende dal progetto; potrebbe contenere
  sorgenti non processati direttamente da MkDocs, come script o file da elaborare separatamente, oppure risorse come
  immagini non destinate alla cartella `docs/`). Nel nostro caso attuale, questa cartella è presente ma il suo utilizzo
  non è ancora definito chiaramente.
- **`.github/workflows/`** – Directory contenente i file di configurazione per GitHub Actions. In particolare, il
  file `deploy.yml` all’interno di questa cartella definisce il workflow di deploy continuo su GitHub Pages (vedi
  sezione **Deploy automatico** per i dettagli).
- **`add_pwd.py`** – Script Python aggiuntivo presente nel repository. Il nome suggerisce che possa essere correlato
  alla gestione di password o credenziali (forse in relazione al plugin di cifratura dei contenuti). Potrebbe servire,
  ad esempio, per impostare una password cifrata da inserire nel sito; tuttavia, senza documentazione aggiuntiva, il suo
  utilizzo rimane da chiarire.
- **`encryptcontent.cache`** – File di cache generato dal plugin di cifratura (*mkdocs-encryptcontent-plugin*). Questo
  file viene creato automaticamente quando il plugin cifra i contenuti durante la build del sito. La sua presenza indica
  che il plugin è stato eseguito almeno una volta, anche se al momento la configurazione completa per proteggere le
  pagine non è attiva (nessuna password impostata in `mkdocs.yml`). In pratica, il file cache conserva informazioni per
  evitare di dover ricifrare tutto a ogni build, migliorando le performance.

*(Nota: eventuali altri file e cartelle, come ad esempio immagini o altri asset, dovranno essere inseriti nella
cartella `docs/` o sottocartelle, in modo che MkDocs li includa nel sito generato. Attualmente, la struttura è
essenziale come punto di partenza.)*

## Installazione delle dipendenze e avvio locale

Per chi vuole eseguire questo progetto in locale, i passi sono riassunti di seguito. Si assume che Git e Python siano
già installati sul sistema:

```bash
# Clona la repository
git clone https://github.com/cyberfolk/wm-docs.git
cd wm-docs

# (Opzionale) crea ed attiva un ambiente virtuale Python
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# Installa le dipendenze richieste
pip install -r requirements.txt

# Avvia il server di sviluppo MkDocs
mkdocs serve
```

Dopo aver eseguito `mkdocs serve`, aprire il browser all'indirizzo `http://127.0.0.1:8000/` per visualizzare la
documentazione. Ogni modifica ai file Markdown nella cartella `docs/` comporterà un aggiornamento automatico della
pagina nel browser (funzionalità di live reload offerta da MkDocs), rendendo facile iterare sulla documentazione.

Le **librerie Python (dipendenze)** necessarie, elencate anche in `requirements.txt`, includono almeno:

- `mkdocs` – Il motore principale per la generazione del sito statico a partire da Markdown.
- `mkdocs-material` – Il tema Material for MkDocs (inclusi i suoi pacchetti correlati). Installando questo, pip porterà
  anche le dipendenze specifiche del tema Material.
- `mkdocs-encryptcontent-plugin` – *(Opzionale)* Plugin per proteggere con password parti della documentazione. È stato
  aggiunto per sperimentare la cifratura di alcune pagine; se non si intende usarlo, questa dipendenza può essere
  omessa. **Importante**: per attivarlo realmente, occorre configurarlo in `mkdocs.yml` (come descritto sopra),
  altrimenti la sua presenza non influisce sul sito.
- Altri plugin o strumenti possono essere aggiunti in futuro secondo necessità (ad esempio plugin per breadcrumb,
  versionamento, search avanzata, ecc.). In tal caso andranno elencati nel `requirements.txt` e installati di
  conseguenza.

Assicurarsi di avere le versioni compatibili di questi pacchetti. Il file `requirements.txt` può bloccare versioni
specifiche se necessario (ad esempio `mkdocs-material>=9.0` per garantire una certa release del tema).

## Deploy automatico su GitHub Pages

Una volta che il sito statico è stato creato e versionato su GitHub, il passo successivo è pubblicarlo tramite GitHub
Pages e automatizzare questo processo. Nella nostra configurazione abbiamo implementato quanto segue:

- **Branch di pubblicazione `gh-pages`**: GitHub Pages per i progetti utilizza tipicamente un branch dedicato (
  chiamato `gh-pages`) per servire il contenuto del sito. Il comando `mkdocs gh-deploy` di MkDocs, quando eseguito,
  costruisce il sito (in locale) e pubblica automaticamente i file statici sul branch `gh-pages` del repository. Noi
  abbiamo deciso di non eseguire manualmente questo comando, ma di demandare il tutto a un workflow di GitHub Actions (
  CI/CD).
- **GitHub Actions Workflow (`.github/workflows/deploy.yml`)**: Nella cartella `.github/workflows` è presente il
  file `deploy.yml` che definisce il processo automatico di build e deploy. Ecco i punti salienti di questa
  configurazione:
    - **Trigger del workflow**: il workflow è impostato per avviarsi automaticamente a ogni push sul branch
      principale (`main`) della repository. In questo modo, ogni volta che la documentazione viene aggiornata e inviata
      su GitHub, parte una nuova build del sito.
    - **Checkout del codice**: lo step iniziale usa `actions/checkout` per recuperare il codice della repository
      all'interno dell’ambiente di CI.
    - **Setup di Python**: viene usato `actions/setup-python` per predisporre un interprete Python nell’ambiente GitHub
      Actions (ad es. Python 3.x necessario per MkDocs).
    - **Installazione delle dipendenze**: uno step esegue `pip install -r requirements.txt` per installare MkDocs, il
      tema Material e gli eventuali plugin all'interno dell’ambiente di build. In questo modo il runner Actions ha tutti
      gli strumenti per generare il sito.
    - **Build e deploy**:  Utilizzare `mkdocs gh-deploy` – Questo comando interno a MkDocs compila i file e li invia
      direttamente al branch `gh-pages`. Nel nostro workflow, è stato utilizzato con l'opzione `-force` (forza la
      sovrascrittura del branch gh-pages) e viene eseguito con le credenziali fornite da GitHub Actions. Affinché ciò
      funzioni, è fondamentale impostare i permessi adeguati: nel file YAML del workflow, sotto la chiave `permissions`,
      abbiamo specificato `contents: write` per consentire al token `GITHUB_TOKEN` di effettuare push sul repository.
      Inoltre, prima di eseguire `gh-deploy`, viene configurato il nome utente ed email git dell'agente (
      tipicamente `github-actions[bot]`) per il commit automatico.
    - **Cache (ottimizzazione)**: Il workflow potrebbe includere uno step di caching (ad esempio usando `actions/cache`)
      per memorizzare la cache di MkDocs/Material tra una build e l'altra, velocizzando i tempi. Nel file `deploy.yml`
      abbiamo inserito un esempio di cache basata sulla settimana corrente, utile soprattutto se la documentazione
      cresce di dimensioni o utilizza plugin che beneficiano della cache (il tema Material stesso sfrutta `.cache`).
      Questo passaggio è facoltativo ma consigliato per progetti più grandi.
    - **Ambiente di Pages (facoltativo)**: GitHub offre la possibilità di dichiarare un ambiente di deployment "GitHub
      Pages". In configurazioni più nuove, potremmo usare il workflow predefinito di Pages o aggiungere `deployments`
      per marcare il deploy. Nel nostro setup attuale, abbiamo gestito manualmente il push su `gh-pages`.
- **Abilitazione di GitHub Pages**: Affinché il sito sia effettivamente servito, bisogna abilitare GitHub Pages nelle
  impostazioni del repository:
    - Andare su **Settings** > **Pages** della repository su GitHub.
    - Selezionare come sorgente il branch `gh-pages` e la directory `/ (root)`. (Di solito, dopo il primo deploy, GitHub
      rileva automaticamente il branch `gh-pages` creato dal workflow. Assicurarsi comunque che sia selezionato
      correttamente).
    - Salvare. GitHub assegnerà un URL al sito, tipicamente del formato `https://<username>.github.io/<nome-repo>/`. Per
      questo progetto, l’URL atteso è **https://cyberfolk.github.io/wm-docs/** una volta che Pages è attivo e il
      contenuto è stato pubblicato.
    - **Nota**: In alternativa, GitHub ha introdotto una modalità di pubblicazione via GitHub Actions senza dover
      specificare manualmente il branch (basta un file `pages.yml` dedicato). Nel nostro caso abbiamo usato il
      branch `gh-pages` tradizionale. L'importante è che dopo il primo deploy, la pagina GitHub Pages sia attiva;
      potrebbe volerci qualche minuto perché il sito diventi raggiungibile la prima volta.
- **Verifica del deploy**: Dopo che il workflow di Actions è eseguito (è possibile seguirne l'esecuzione nella tab *
  *Actions** su GitHub), controllare sotto **Settings > Pages** che lo stato sia "Deployed" e visitare l'URL pubblico.
  Ogni volta che nuove modifiche vengono pushate su `main`, il workflow ri-pubblicherà il sito. È buona pratica
  controllare gli eventuali messaggi di errore nel log di Actions in caso di fallimento (ad esempio, errori di sintassi
  in `mkdocs.yml` o problemi con le dipendenze possono far fallire la build).

## Considerazioni sulla cifratura dei contenuti (opzionale)

Come accennato, abbiamo incluso il plugin **mkdocs-encryptcontent-plugin** per valutare la possibilità di proteggere con
password alcune sezioni della documentazione. L'idea sarebbe di richiedere una password all’utente per visualizzare
specifiche pagine considerate riservate. Attualmente, però, questa funzionalità non è completamente configurata. Per
attivarla occorre:

- Impostare nel `mkdocs.yml` la sezione `plugins` con `encryptcontent` e specificare almeno una password (globale o per
  pagina). Ad esempio:

    ```yaml
    plugins:
      - encryptcontent:
          global_password: "inserireQuiUnaPasswordSicura"
          pages:
            - "pagina_riservata.md"
    ```

  (Oppure, definire password diverse per pagine diverse secondo la documentazione del plugin).

- Rigenerare il sito. Il plugin cifrerà i contenuti indicati creando/aggiornando il file `encryptcontent.cache` con i
  dati crittografici.
- Quando un utente visita la pagina protetta sul sito, gli verrà chiesta la password per decifrare e vedere il
  contenuto.

Nel nostro repository, il plugin è installato e il file di cache presente indica un tentativo d’uso, ma non essendoci
ancora configurazione nel `mkdocs.yml`, attualmente nessuna pagina è effettivamente protetta. Questa parte rimane quindi
**un promemoria per sviluppi futuri**: qualora si voglia rendere privata parte della documentazione, abbiamo già gli
strumenti pronti (basterà completare la configurazione come sopra). Se invece la documentazione resta completamente
pubblica, il plugin può essere rimosso dalle dipendenze per semplicità.

## Conclusione

In sintesi, **WM Docs** è stato creato con l'intento di avere una documentazione semplice da mantenere e sempre
aggiornata. Grazie a MkDocs Material, il sito ha un aspetto professionale e responsive senza sforzo, e la scrittura in
Markdown permette di concentrarsi sui contenuti. L’integrazione con GitHub Pages e Actions garantisce che ogni
aggiornamento venga pubblicato automaticamente, riducendo il rischio di discrepanze tra ciò che è nel repository e ciò
che è online.

