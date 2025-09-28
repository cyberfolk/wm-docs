# **ML | Mostro Leggendario**

> Creatura unica o straordinariamente potente che caratterizza un esagono (o più) con la sua presenza, diventando una **minaccia ecologica**, un **simbolo narrativo** o una **sfida epocale**.

---

### ✅ Cosa è

- Rappresenta **creature iconiche** che trascendono l’idea di “mostro casuale”.
- Sono entità che **definiscono il territorio**: la loro sola esistenza plasma l’ambiente circostante (es. un drago rosso che incenerisce vallate intere).
- Servono come **punti di riferimento narrativi**: non un incontro qualunque, ma “il mostro di quella regione”.
- **Campo chiave Odoo** → `is_legendary` = True

### 🔗 Relazioni con le altre entità

- **Fazioni** (`faction_monster_ids`) → la creatura può guidare o essere temuta da una fazione (*es. culto draconico, orde non-morte*).
- **NPC** (`npc_monster_ids`) → individui che interagiscono col mostro (alleati, rivali, emissari).
- **Quest** (`quest_monster_ids`) → missioni di rilievo legate al ML (caccia, sopravvivenza, trattative, vendette).
- **POI** (`poi_monster_ids`) → luoghi simbolici influenzati dal ML (tane, rovine, templi profanati).
- **Insediamenti** (`settlement_monster_ids`) → comunità sotto la sua minaccia o dominio.
- **Lore Item** (`lore_item_monster_ids`) → miti, profezie o leggende che circolano sul suo conto.
- **Artefatti** (`artifact_monster_ids`) → oggetti legati alla sua origine, potere o possibile sconfitta.
- **Creature base** (`creature_monster_ids`) → specie subordinate o servitrici che popolano il suo seguito.
- **Mostri Leggendari** (`monster_monster_ids`) → legami con altri ML (alleanze, rivalità, stirpi condivise).
- **Hex** → un ML può estendere la sua influenza oltre un esagono, ma ha sempre un *cuore narrativo* localizzato.

### 🔄 Modello polimorfico

Questa entità narrativa utilizza il modello `creature.creature`, il quale viene usato anche per **Creature Base** e **NPC**.  
La natura del modello è **polimorfica** e viene gestita dai seguenti flag:

- `is_legendary = True` → Mostro Leggendario
- `is_npc = True` → NPC
- entrambi attivi → creatura **sia ML che NPC** (es. drago antico parlante, lich sovrano).

### 📌 Funzione nel gioco

- Fornisce **sfide memorabili** e **rischi estremi**.
- Incapsula l’idea di “leggenda vivente” → i PG sentono parlare della creatura prima di incontrarla.
- Serve come **ancora narrativa**: qualcosa che “fa parlare di sé” in tutto il territorio.

### 🧭 Heuristica pratica

- **ML puro** → solo minaccia ecologica (es. Tarrasque).
- **ML + NPC** → se è socialmente interagibile (es. drago parlante, lich).
- **ML + Fazione** → se guida seguaci o culti.

### 🌍 Esempi

- **Tarrasque** → puro esempio di mostro epocale.
- **Drago rosso antico** → può essere *ML* puro, oppure anche *NPC/Fazione* se lo giochi con intelligenza e seguaci.
- **Kraken** → influenza mari ed esagoni costieri.
- **Lich leggendario** → minaccia sovrannaturale, spesso anche *NPC* e *Fazione*.
- **Leviatano elementale** → incarnazione di una forza primordiale