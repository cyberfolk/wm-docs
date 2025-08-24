---
password: VAI VIA
---

# Nomenclatura Esagoni

## Formato degli identificatori

**ID tecnico** (univoco)

```
HX-[MA]-[Q]-[R].[I]-[BIO]-SML[X]
```

**Alias breve**

```
[MA]-[Q]-[R].[I]
```

**Titolo umano**

```
[Alias breve] — [Bioma leggibile] (SML[X])
```

**Sottotitolo discorsivo**

Una riga che *“spiega a parole”* cosa c’è nell’esagono.

---

## Campi e valori ammessi

* **\[MA] MacroArea**
  `C` (Centro), `I01…I08` = interne, `E01…O16` = esterne. 

* **\[Q] Quadrante**
  Lettera maiuscola `A…U`.

* **\[R] Raggio/Anello**
  `0` = centro del quadrante; `1` = primo anello (6 esagoni); `2` = secondo anello (12 esagoni).

* **\[I] Indice nell’anello**
  Per `R=1`: `1…6` — Per `R=2`: `1…12`.
  **Orientamento:** si parte da **Nord** e si procede **orario**.

* **\[BIO] Bioma (3 lettere)**
  `FOR` (foresta), `DES` (deserto), `PAL` (palude), `MON` (montagna),
  `COL` (collina), `PAS` (pianure/pascoli), `CST` (costa), `LAC` (lago),
  `ART` (artico), `URB` (urbano/rovine), `WLD` (selvaggio/misto).
  *(Estendibile; mantieni 3 lettere.)*

* **SML\[X]**
  **Obbligatorio**. Se assente, **interrompi la generazione** e richiedi di ripassare lo YAML “con SML”.

* **Discorsivo**
  Campo testo obbligatorio (1–2 frasi, niente spoiler di *Lore Alta*).
  *Applica la blacklist LA→LB (es.: “gemma cosmica” → “reliquia locale”).*

---

## Regole di validazione

**Slug completo (ID tecnico):**

```
^HX-(?:C|I0[1-8]|O0[1-9]|O1[0-6])-[A-U]-(?:0\.0|1\.[1-6]|2\.(?:[1-9]|1[0-2]))-[A-Z]{3}-SML[0-9]+$
```

**Alias breve:**

```
^(?:C|I0[1-8]|O0[1-9]|O1[0-6])-[A-U]-(?:0\.0|1\.[1-6]|2\.(?:[1-9]|1[0-2]))$
```

**Coerenza R/I:**

  * Se `R=0` → `I=0`
  * Se `R=1` → `I ∈ [1..6]`
  * Se `R=2` → `I ∈ [1..12]`

---

## Esempi canonici

* `HX-I03-A-0.0-FOR-SML2`
  **I03-A-0.0 — Foresta Nebbiosa (SML 2)**
  *“Abetaia fitta con altare di licheni; ululati in lontananza.”*

* `HX-O12-M-1.4-PAL-SML3`
  **O12-M-1.4 — Palude Salmastra (SML 3)**
  *“Passerella di tronchi marci; fuochi fatui al crepuscolo.”*

* `HX-I07-F-2.11-COL-SML1`
  **I07-F-2.11 — Colline Ventose (SML 1)**
  *“Menhir caduto e tracce fresche di capri selvatici.”*
