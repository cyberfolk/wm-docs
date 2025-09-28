# Insediamenti

> Comunità abitata (villaggio, città, capitale, megalopoli) intesa come spazio sociale e geografico, non politico.

### ✅ Cosa è

- Un **luogo abitato stabilmente** da una comunità.
- Una **zona abitabile** dove i PG possono interagire con NPC in prevalenza non ostili.
- Comprende vari livelli di grandezza: dal piccolo villaggio rurale fino alla megalopoli.
- È un **contenitore sociale e geografico**, ma **non politico** (il potere appartiene alle Fazioni).

### 🚫 Cosa non è

- **Non è una fazione** → un regno, un impero, una provincia sono entità politiche/amministrative, quindi da classificare sotto “Fazione”.
- **Non è un semplice POI** → rovine, città fantasma, basi abbandonate, castelli isolati senza comunità attiva vanno sotto “POI”.

## 🔑 Attributi Narrativi

- **Scala** (`scale`) → dimensione dell’insediamento (*borgo, villaggio, città, capitale, megalopoli…*).
- **Atteggiamento** (`attitude`) → disposizione della comunità verso estranei (*amichevole, neutrale, ostile*).
- **Bisogni** (`needs`) → ciò che manca o che la comunità richiede (cibo, difesa, commercio).
- **Offre** (`offers`) → risorse o opportunità che mette a disposizione (mercato, artigianato, informazioni).

### 🔗 Relazioni con le altre entità

- **Fazioni** (`faction_ids`) → possono controllare o influenzare l’insediamento (governo, occupazione, protezione).
- **NPC** (`npc_ids`) → vivono o agiscono negli insediamenti, incarnandone la vita sociale.
- **Quest** (`quest_ids`) → spesso partono o si sviluppano dentro un insediamento (richieste, voci di mercato, missioni).
- **POI** (`poi_ids`) → punti d’interesse interni o collegati (piazze, rovine inglobate, templi).
- **Lore Item** (`lore_item_ids`) → feste, credenze, miti urbani collegati all’insediamento.
- **Artefatti** (`artifact_ids`) → oggetti rari custoditi o contesi nella comunità.
- **Creature** (`creature_ids`) → popolazione “base” (es. bestiario, fauna antropica).
- **Mostri Leggendari** (`monster_ids`) → minacce o entità epocali che incombono sulla città.
- **Hex** → un insediamento occupa uno o più esagoni della mappa (relazione indiretta via `hex`).

