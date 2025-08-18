# Oggetto/Artefatto

> Elemento materiale significativo (spesso unico o raro) con **valore meccanico e/o simbolico** che può generare quest, cambiare relazioni o veicolare LoreItem

### ✅ Cosa è

- Unità atomica **materiale**: arma, reliquia, gemma, tomo, mappa, chiave, idolo, ecc.
- Può essere **unico** (artefatto) o **replicabile** (oggetto raro/comune); come per Mostro abbiamo “specie vs istanza”.

### 📌 Funzione nel gioco

- Colma un vuoto: molte **quest** e **lore** orbitano attorno a **cose** (non solo persone/luoghi).
- È un **pivot di gioco**: innesca scelte, conflitti tra fazioni, cambi di potere.

### 🔗 Schema minimo (campi suggeriti)

- `id`, `nome`, `categoria` (arma, reliquia, chiave, tomo, gemma…), `unico` (bool)
- `effetto_meccanico` (breve), `potere/limite` (tag), `costo/prezzo` (opz.)
- `simbolismo` (perché è desiderato: status, fede, mito)
- `rischi/maledizioni` (opz.)
- `provenienza` (fazione/insediamento/luogo), `stato` (smarrito, custodito, rotto)
- **Relazioni**: `rel_fazione_ids`, `rel_npc_ids`, `rel_poi_ids`, `rel_hex_ids`, `rel_lore_ids`, `rel_quest_ids`
- Pattern **specie/istanza** (opz.): `oggetto_tipo_id` ↔ `oggetto_istanza` (per l’Artefatto specifico)

### 🧭 Heuristica pratica

- Se l’oggetto **cambia l’equilibrio** tra fazioni o abilita nuove azioni dei PG → è entità.
- Se è solo colore (una coppa qualsiasi) → rimane dettaglio di descrizione, non entità.
