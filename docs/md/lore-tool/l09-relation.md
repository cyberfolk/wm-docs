# RN | Relazioni Narrative

> Arco direzionale tipizzato tra due entità narrative che descrive in che rapporto stanno (alleanza, ostilità, appartenenza, controllo, smentita, ecc.).

### ✅ Cosa è

- Un **arco** (*edge*) **direzionale** e **tipizzato** tra **due entità narrative**.
- È **atomico**: una singola affermazione del tipo “A → [relazione] → B”.

### 🔑 Attributi Narrativi

- **Descrizione** (`description`) → testo libero che spiega la relazione.
- **Origine** (`source_ref`, `source_model`, `source_id`) → entità di partenza dell’arco.
- **Destinazione** (`target_ref`, `target_model`, `target_id`) → entità di arrivo dell’arco.
- **Nome computato** (`name`) → formato leggibile: “A → B”.
- **Direzionalità** (`is_directional`) → di default vero (A → B ≠ B → A).
- **Sequenza** (`sequence`) → per ordinare più relazioni simili.

### 🔗 Integrazione con le altre entità

- Ogni entità narrativa (Fazione, Insediamento, NPC, ML, POI, Quest, Lore Item, Artefatto, ecc.) eredita il **`narrative.relation.mixin`**.
- Questo mixin aggiunge:
    - **Contatore relazioni** (`narrative_relations_count`).
    - **Azione** `action_open_narratives()` → apre tutte le relazioni che coinvolgono il record.
    - **Azione** `action_add_outgoing_narrative()` → crea una relazione con il record come sorgente.
    - **Azione** `action_add_incoming_narrative()` → crea una relazione con il record come destinazione.

### 📌 Funzione nel gioco

Permette di modellare **graficamente** e **concettualmente** la **rete narrativa** che lega tutte le entità.
