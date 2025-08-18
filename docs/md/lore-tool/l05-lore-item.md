# Lore Item

> Unità minima di tradizione o credenza (leggenda, diceria, mito, festa, paura, gioia, terrore).

---

### ✅ Cosa è
- Un **enunciato atomico** di lore (1–3 frasi) con **funzione in gioco**.
- Classificabile per **tipo** (*leggenda, diceria, credenza, mito, paura, gioia, festa, terrore*).
- **Riusabile** e **collegabile** ad altre entità (Fazione, NPC, POI, Hex, ML, Quest) e ad altri Lore Item.

---

### 🚫 Cosa non è
- Non è un **tema generico** (“la verità sull’universo”).
- Non è solo **colore** senza implicazioni di gioco.
- Non è un **riassunto enciclopedico**: se comunica più di un’idea, va diviso in più Lore Item.

---

### 🔑 Attributi minimi (schema atomico)
- `titolo_breve` (≤ 8 parole)
- `tipo`: `leggenda | diceria | credenza | mito | paura | gioia | festa | terrore`
- `enunciato` (1–3 frasi, chiaro nell’impatto sui PG)
- `strato`: `autoctono | cosmico`
- `prospettiva`: `in-world | extra-diegetica`
- `attendibilità`: `voce | comune | autorevole | canonico`
- `provenienza` (fonte/comunità)
- `circolazione`: `segreta | ristretta | diffusa`
- `volatilità`: `effimera | stabile | ritualizzata`
- `periodo` (opz., utile per *feste*)
- `funzione_narrativa` (tag: es. *presagio, identitaria, minaccia, conforto, prova, hook*)
- `motivi/temi` (tag)
- **Relazioni**:
  - `collega_lore_ids` (self M2M, per corpus/insiemi)
  - `rel_fazione_ids`, `rel_npc_ids`, `rel_poi_ids`, `rel_hex_ids`, `rel_mostro_ids`, `rel_quest_ids`

---

### 📋 Profili per tipo (opzionali)
- **Diceria** → `fonte_specifica`, `grado_distorsione (1–5)`, `ultima_verifica`
- **Festa/Gioia** → `ricorrenza`, `rito_gesti`, `oggetti_simbolici`, `ricompense_sociali`
- **Paura/Terrore** → `triggers`, `conseguenze_sociali`, `segnali_preparatori`
- **Mito/Leggenda** → `archetipo (Campbell/Vogler)`, `funzione_proppiana`, `antagonista/soglia`
- **Credenza** → `precetto/precauzione`, `tabù`, `sanzione`

> I profili attivano **campi facoltativi** senza rompere il modello unico.

---

### 🔗 Relazioni con altre entità
- **Fazioni/NPC**: origine, custodia, propaganda, repressione.
- **POI/Hex**: localizzazione, diffusione regionale.
- **ML**: origine di miti/paure; segna “territori del mostro”.
- **Quest**: un Lore Item può **generare** o **spiegare** una missione.

---

### 📌 Funzione nel gioco
- Alimenta **hook**, anticipazioni, timori e rituali.
- Crea **coerenza culturale** fra aree/insediamenti.
- Offre **maniglie operative** per improvvisare o preparare sessioni.

---

### 🧭 Heuristica pratica
- **Atomicità**: un’idea = un record. Se sono due idee, sono due Lore Item.
- **Strato esplicito**: marca `autoctono` vs `cosmico` per chiarezza epistemica.
- **Prospettiva chiara**: ciò che “si crede” (in-world) vs ciò che “è” (meta).
- **Agganciabilità**: ogni record dovrebbe poter diventare azione in gioco.
- **Collegabilità**: usa `collega_lore_ids` per corpus/dottrine/cicli.

---

### ⚖️ Vantaggi della definizione
1. **Uniformità**: un unico modello per tutte le forme di tradizione/credenza.
2. **Modularità**: facile riuso e ricomposizione in corpus tematici.
3. **Query potenti**: filtri per tipo, strato, funzione, area, attendibilità.

---

### 🌰 Esempi rapidi
- **Diceria (autoctono)**: “Nel Bosco Cavo, i fuochi fatui guidano ai tumuli.” (funzione: *presagio*)
- **Festa (autoctono)**: “Ogni solstizio si getta il pane nel fiume: promette raccolti.” (funzione: *rituale identitario*)
- **Mito (cosmico)**: “Le Gemme cantano sotto le montagne: chi le ode non invecchia.” (funzione: *hook/minaccia*)
- **Paura (autoctono)**: “Non nominare i Senza-Volto dopo il tramonto: ti ascoltano.” (funzione: *minaccia/tabù*)

---
