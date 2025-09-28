# Hex

> Unità geografica di mappa esagonale che rappresenta un’area esplorabile, con bioma, clima e possibili incontri; può contenere Punti d’interesse e insediamenti.

### ✅ Cosa è

- Un **modulo geografico**: la cella base della mappa esagonale.
- Serve a organizzare lo spazio di gioco in modo funzionale all’esplorazione e alla gestione del tempo/risorse.
- Ogni hex ha dimensione fissa (es. 18 km) e rappresenta un territorio coerente.

### 🚫 Cosa non è

- **Non è un Luogo** → un hex è cornice spaziale mentre il POI è un punto preciso dentro l’hex.
- **Non è un Insediamento** → può contenerne, ma non coincide con una comunità abitata.

## 🔑 Attributi Narrativi

- **Codice e Nome** (`code`, `name`) → identificativo esagonale, derivato dal sistema di mappa/quadranti.
- **Quadrante / Mappa** (`quad_id`, `map_id`) → appartenenza a un settore della mappa.
- **Coordinate** (`row`, `col`) → posizione nella griglia.
- **Status** (`status`) →
    - `grid` = hex attivo in una mappa/quadrante.
    - `script` = hex scollegato, usato per bozze o lore provvisoria.
- **Confini** (`border_N`, `border_NE`, `border_SE`, `border_S`, `border_SW`, `border_NW`) → esagoni adiacenti.
- **Bioma** (`biome_id`) → tipo di ambiente (foresta, tundra, deserto…).
- **SML** (`sml`) → difficoltà dell’esagono (scontro mortale per 4 PG di livello pari a SML).
- **Descrizione** (`description`) → testo libero, HTML.
- **Immagini** (`image`, `image_gallery_ids`).
- **Completamento** (`completion_percentage`) → percentuale automatica di compilazione dei campi.

### 🔗 Relazioni con altre entità

- **POI** (`poi_id`, `poi_ids`) → punti d’interesse principali e secondari.
- **Insediamenti** (`settlement_ids`) → comunità dentro o collegate all’esagono.
- **Mostro Leggendario** (`monster_id`, `monster_ids`) → creatura iconica che caratterizza l’hex.
- **Creature base** (`creature_ids`) → fauna o popolazione generica.
- **NPC** (`npc_ids`) → personaggi rilevanti legati alla zona.
- **Fazioni** (`faction_ids`) → gruppi che controllano o influenzano l’area.
- **Artefatti** (`artifact_ids`) → reliquie o oggetti nascosti nell’hex.
- **Lore Item** (`lore_item_ids`) → leggende, paure, credenze legate al territorio.
- **Quest** (`quest_ids`) → missioni che hanno come scenario l’hex.
- **Incontri**:
    - **Selvaggi** (`wild_encounter_ids`) → scontri ricorrenti collegati al bioma.
    - **Casuali** (`encounter_encounter_ids`) → eventi o incontri generati in quel territorio.

### 📌 Funzione nel gioco

- Rende l’esplorazione **concreta e gestibile** → ogni movimento sulla mappa consuma tempo/risorse.
- Fornisce una struttura modulare → facile da compilare e ampliare.
- Permette di bilanciare la distribuzione di **luoghi**, **incontri** e **fazioni** sul territorio.
- Favorisce la **narrazione emergente**: spostandosi da un hex all’altro i PG costruiscono il loro viaggio.

### 🧭 Heuristica pratica

- Ogni Hex dovrebbe avere **almeno un Luogo significativo** (anche piccolo o nascosto).
- Può contenere **più POI**, ma uno solo dovrebbe essere il **focus principale**.
- Può essere caratterizzato da una **Mostro Leggendario (ML)** che influenza l’ambiente circostante.
- Deve avere una coerenza ambientale → non mescolare troppi biomi/temi in un unico hex.

### 🌍 Esempi di Hex

- **Foresta nebbiosa** (bioma: bosco umido, clima: piovoso, luogo: altare dimenticato, incontro: spiriti ostili).
- **Steppe ventose** (bioma: prateria, luogo: tumuli antichi, insediamento: tribù nomade, mostro leggendario: kraken della terra).
- **Montagne innevate** (bioma: alpino, luogo: monastero abbandonato, creatura leggendaria: drago bianco).
