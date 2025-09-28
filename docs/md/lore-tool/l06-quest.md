# Quest

> Missione che i PG possono intraprendere, sempre caratterizzato da **Hook** e **Obiettivo**, con possibilità di includere **Passaggi chiave**, **Ricompense** e **Rischi** (anche se a volte impliciti).


---

### ✅ Cosa è

- Una **unità narrativa azionabile**: qualcosa che i PG possono scegliere di fare, non solo un tema o uno stato del mondo.
- Può nascere da **qualsiasi entità narrativa** (*NPC, Fazione, Mostro, Insediamento, Hex, POI, Artefatto, Lore Item*).
- È distinta dal puro contesto: *“la città è in guerra”* è uno stato del mondo, mentre *“difendere le mura entro l’alba”* è una quest.

### 🚫 Cosa non è

- **Non è un tema** → *“scoprire la verità sull’universo”* è troppo astratto.
- **Non è uno stato del mondo** → *“la città è in guerra”* è contesto, non un compito.
- **Non è solo colore** → una festa è *Lore*, diventa quest solo se implica un compito: *“offrire un dono entro il tramonto”*.

## 🔑 Attributi Narrativi

- **Stato** (`state`) → andamento della missione (*ongoing, completed, failed*…).
- **Hook** (`hook`) → gancio narrativo che cattura l’interesse dei PG.
- **Obiettivo** (`objective`) → compito chiaro e raggiungibile.
- **Passaggi chiave** (`key_steps`) → micro-task o fasi intermedie.
- **Ricompense** (`rewards`) → benefici concreti o simbolici per i PG.
- **Rischi** (`risks`) → cosa succede in caso di fallimento o abbandono.

### 🔗 Relazioni con le altre entità

- **NPC** (`npc_ids`) → volti e mandanti delle missioni.
- **Fazioni** (`faction_ids`) → commissionano, ostacolano o influenzano la quest.
- **Insediamenti** (`settlement_ids`) → generano missioni legate ai bisogni della comunità.
- **POI** (`poi_ids`) → luoghi che diventano obiettivi narrativi.
- **Lore Item** (`lore_item_ids`) → voci, dicerie o miti che si trasformano in missioni.
- **Artefatti** (`artifact_ids`) → reliquie da trovare, proteggere o distruggere.
- **Creature** (`creature_ids`) → sfide o alleati nel corso della quest.
- **Mostri Leggendari** (`monster_ids`) → spesso al centro di missioni epiche.

### 📌 Funzione nel gioco

- Introduce **obiettivi concreti** che guidano l’azione dei PG.
- Genera **sfide, rischi e ricompense** che alimentano il ciclo di gioco.
- Collega in maniera **dinamica** tutte le altre entità narrative (luoghi, fazioni, NPC, lore).
