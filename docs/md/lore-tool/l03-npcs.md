# NPCs

> Individuo significativo non giocante (ha identità, motivazione e impatto narrativo sui PG).

---

### ✅ Cosa è

- È un **singolo individuo** distinto dalle comparse.
- Ha un **ruolo narrativo rilevante**: l’interazione con lui produce conseguenze tangibili (informazioni, emozioni, ricompense, ostacoli).
- Funziona come **attante** (Greimas) o **archetipo** (Viaggio dell’Eroe): mentore, antagonista, aiutante, guardiano della soglia…
- **Campo chiave Odoo** → `is_npc = True`.

## 🔑 Attributi Narrativi

- **Identità** → nome, aspetto, ruolo sociale (`titles`, `appearance`, `social_role`).
- **Motivazione** (`motivation`).
- **Bisogni / Offerte** (`needs`, `offers`).
- **Relazione con i PG** (`pc_relation`).

### 🔗 Relazioni con le altre entità

- **Fazioni** (`faction_npc_ids`) → possono esserne membri, leader, emissari o oppositori.
- **Insediamenti** (`settlement_npc_ids`) → vivono o agiscono nella vita sociale.
- **Quest** (`quest_npc_ids`) → affidano missioni, ostacolano, o sono obiettivi narrativi.
- **POI** (`poi_npc_ids`) → legati a luoghi specifici (taverne, templi, covi).
- **Lore Item** (`lore_item_npc_ids`) → leggende, tradizioni, credenze che incarnano.
- **Artefatti** (`artifact_npc_ids`) → custodi, ricercatori o creatori di reliquie.
- **Creature base** (`creature_npc_ids`) → gregari, scorte, sottoposti.
- **Mostri Leggendari** (`monster_npc_ids`) → possono servire, opporsi o collaborare con un ML.
- **Hex** → agiscono in aree specifiche della mappa, determinandone la vita sociale.

### 🔄 Modello polimorfico

Questa entità narrativa utilizza il modello `creature.creature`, il quale viene usato anche per **Creature Base** e **Mostri Leggendari**.  
La natura del modello è **polimorfica** e viene gestita dai seguenti flag:

- `is_legendary = True` → Mostro Leggendario
- `is_npc = True` → NPC
- entrambi attivi → creatura **sia ML che NPC** (es. drago antico parlante, lich sovrano).

### 📌 Funzione nel gioco

- **Generatori di interazioni**: forniscono informazioni, risorse, ostacoli o legami emotivi.
- **Specchi dei PG**: riflettono valori, conflitti, scelte morali.
- **Motori narrativi**: avviano quest, intrecciano fazioni, influenzano gli esiti delle storie.

### 🌍 Esempi

- **Lyara, guaritrice del villaggio** → NPC puro, legata a un insediamento.
- **Signore dei banditi** → NPC che diventa anche *Fazione*.
- **Drago parlante** → NPC + ML, con influenza epocale e sociale.
- **Lich consigliere** → NPC + ML, volto e guida di un culto oscuro.