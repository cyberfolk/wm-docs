# Entità Narrative

> Presentate nella forma **Prefisso** | **Nome**


**FZ** | **[Fazioni](l01-fazioni.md)**: *Organizzazione con identità sociale o ideologica, composta da agenti coordinati e dotata di volontà, obiettivi e capacità di influenza sul mondo.*

**IN** | **[Insediamenti](l02-insediamenti.md)**: *Comunità abitata (villaggio, città, capitale, megalopoli) intesa come spazio sociale e geografico, non politico.*

**NPC** | **[NPCs](l03-npcs.md)**: *Individuo significativo non giocante (ha identità, motivazione e impatto narrativo sui PG).*

**HEX** | **[Regioni](l10n-hex.md)**: *Unità geografica di mappa esagonale che rappresenta un’area esplorabile, con bioma, clima e possibili incontri; può contenere Punti d’interesse e insediamenti.*

**POI**  | **[Punto d’Interesse](l04-poi.md)**: *Sito localizzato e puntuale (naturale o artificiale), distinto da un insediamento, con cui i PG possono interagire come punto d’interesse narrativo.*

**ML** | **[Mostro Leggendario](l07-monster.md)**: *Creatura unica o straordinariamente potente che caratterizza un esagono (o più) con la sua presenza, diventando una minaccia ecologica, un simbolo narrativo o sfida epocale.*

**RN** | **[Relazioni Narrative](l09-relation.md)**: *Arco direzionale tipizzato tra due entità narrative che descrive in che rapporto stanno (alleanza, ostilità, appartenenza, controllo, smentita, ecc.).*

**AR** | **[Artefatto](l08-artifact.md)**: *Elemento materiale significativo (spesso unico o raro) con valore meccanico e/o simbolico che può generare quest, cambiare relazioni o veicolare LoreItem.*

**LI** | **[Lore Item](l05-lore-item.md)**: *Unità minima di tradizione o credenza (leggenda, diceria, mito, festa, paura, gioia, terrore).*

**Q** | **[Quest](l06-quest.md)**: *Missione che i PG possono intraprendere, sempre caratterizzato da Hook e Obiettivo, con possibilità di includere Passaggi chiave, Ricompense e Rischi (anche se a volte impliciti).*

## Nomenclatura

- **Formato:** `<PREFISSO><slug>` — lo slug è **minuscolo**, con trattini `_` o , senza spazi/accents: `POI_ponte_nero`, `FZ_fronda_sorgiva`.
- **Univocità:** mantieni gli ID stabili; niente duplicati. Se serve, aggiungi suffissi: `POI_ponte_nero_b03`.
- **Scope:** se l’entità esiste in più esagoni, **riusa lo stesso ID** e collegala via `relazioni`.
- **Prefissi liberi:** usiamo quelli proposti sopra; puoi introdurre lievi varianti coerenti se davvero necessario (ma sconsigliato).
