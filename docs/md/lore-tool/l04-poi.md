# POI | Punto d’Interesse

> Sito localizzato e puntuale (naturale o artificiale), distinto da un insediamento, con cui i PG possono interagire come punto d’interesse narrativo.

### ✅ Cosa è

- Un **punto di interesse (POI) fisso** sulla mappa, **localizzato e di scala ridotta**, con cui i PG possono interagire.
- Può essere:
    - **Naturale** → vetta, cascata, altare nel bosco, grotta.
    - **Artificiale** → ponte, rovina, tempio, dungeon, torre isolata.
- Deve essere **narrativamente significativo** → genera interazioni, quest, o lore item.

### 🚫 Cosa non è

- **Non è un Hex** → gli hex sono celle della mappa, contenitori geografici; il POI è il nodo preciso dentro un hex.
- **Non è un Insediamento** → niente comunità abitata (quindi via “villaggio” dall’elenco esempi).
- **Non è mobile** → una carovana o una nave non sono luoghi, perché non sono fissi.
- **Non è generico** → un campo o una pietra qualsiasi non sono luoghi narrativi.

### 🔑 Attributi Narrativi

[TODO]

### 🔗 Relazioni con le altre entità

- **Quest** (`quest_ids`) → missioni con obiettivo o scena chiave nel POI.
- **Fazioni** (`faction_ids`) → possono controllarlo o presidiarlo.
- **Insediamenti** (`settlement_ids`) → collegati al POI o che ne dipendono.
- **Lore Item** (`lore_item_ids`) → miti, leggende e credenze legati al sito.
- **Artefatti** (`artifact_ids`) → reliquie custodite o nascoste.
- **Creature** (`creature_ids`) → abitanti o bestie comuni del luogo.
- **NPC** (`npc_ids`) → personaggi che lo occupano o lo presidiano.
- **Mostri Leggendari** (`monster_ids`) → entità epocali che possono dimorarvi.
- **Hex** → ogni hex può contenere 1 POI principale (più eventuali secondari).

### 📌 Funzione nel gioco

- Fornisce **nodi puntuali** che arricchiscono la mappa oltre agli insediamenti.
- Genera **hook narrativi**: un POI è sempre qualcosa di cui i PG sentono parlare o che scelgono di esplorare.
- Consente **varietà di design**: rovine, luoghi naturali, dungeon, strutture isolate.

### 🌍 Esempi

- **Naturale** → “Cascata della Memoria”, chi si bagna dimentica un ricordo.
- **Artificiale** → “Ponte dei Briganti”, controllato da una fazione criminale.
- **Misto** → “Tempio sotterraneo in rovina”, con culto decaduto e mostro leggendario dormiente.