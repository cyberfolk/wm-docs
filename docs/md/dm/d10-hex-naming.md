---
password: VAI VIA
---

# Nomenclatura Esagoni

## Formato degli identificatori

**Codice**

```
[Q].[R].[I]
```

**Codice Completo**

```
[MA].[Codice].[BIO].SML[X]
```

**Codice Completo Leggibile**

```
[MA].[Codice] — [Bioma leggibile] (SML[X])
```

---

## Campi e valori ammessi

* **\[MA] MacroArea**
  `C` (Centro), `I01…I08` = interne, `E01…E16` = esterne.

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

---

## Esempi canonici

* `C.A.0.0.FOR.SML2` =   **C-A.0.0 — Foresta Nebbiosa (SML 2)**

* `I03.M.1.4.PAL.SML3` =   **I03-M.1.4 — Palude Salmastra (SML 3)**

* `E09.F.2.11.COL.SML1` =   **E09-F.2.11 — Colline Ventose (SML 1)**
