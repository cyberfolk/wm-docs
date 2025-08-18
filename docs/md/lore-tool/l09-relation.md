# Relazioni Narrative

> **Arco direzionale tipizzato** tra due entità narrative che descrive in che rapporto stanno (alleanza, ostilità, appartenenza, controllo, smentita, ecc.).

### ✅ Cosa è

- Un **arco** (edge) **direzionale** e **tipizzato** tra **due entità** qualunque del tuo vocabolario (Fazione, NPC, Insediamento, POI, Hex, Lore, Quest, Oggetto, Mostro).
- È **atomico**: una singola affermazione del tipo “A → [relazione] → B”.

### 📌 Funzione nel gioco

- Evita di gonfiare ogni entità con campi ad hoc; centralizza la **rete** in un solo modello.
- Consente **query e prompt** basati su pattern (“tutte le fazioni che **controllano** un insediamento con un **oggetto** custodito da un **NPC** ostile ai PG”).

### 🔗 Schema minimo (campi suggeriti)

- `src_model`, `src_id` (polimorfico), `dst_model`, `dst_id` (polimorfico)
- `attendibilità` (voce/comune/autorevole/canonico) — utile con Lore
- `fonte` (NPC/Fazione/Lore), `nota` (breve), `periodo` (da–a), `peso`/`intensità` (1–5)
- **Vincoli**: unicità logica (src, rtype, dst); opzionale `inverse_rtype` per creare l’arco opposto
