# -*- coding: utf-8 -*-

import os
import re


def ha_frontmatter(file_md):
    with open(fide_md, 'r', encoding='utf-8') as f:
        prima_riga = f.readline()
        return prima_riga.strip() == "---"


def aggiorna_o_aggiungi_password(file_md):
    with open(file_md, 'r', encoding='utf-8') as f:
        contenuto = f.read()

    if contenuto.startswith("---"):
        # C'è già un frontmatter: estrai il blocco
        blocchi = contenuto.split("---")
        if len(blocchi) >= 3:
            intestazione = blocchi[1].strip()
            resto = "---".join(blocchi[2:]).lstrip()

            # Cerca se c'è già una password
            if "password:" in intestazione:
                nuova_intestazione = re.sub(r"password:.*", f"password: {PASSWORD}", intestazione)
                print(f"[OK] Password aggiornata in: {file_md}")
            else:
                nuova_intestazione = intestazione + f"\npassword: {PASSWORD}"
                print(f"[OK] Password aggiunta a frontmatter in: {file_md}")

            nuovo_contenuto = f"---\n{nuova_intestazione}\n---\n\n{resto}"
        else:
            print(f"[ERRORE] Frontmatter malformato in: {file_md}")
            return
    else:
        # Nessun frontmatter: lo aggiunge
        nuovo_contenuto = f"---\npassword: {PASSWORD}\n---\n\n{contenuto}"
        print(f"[OK] Password inserita in: {file_md}")

    with open(file_md, 'w', encoding='utf-8') as f:
        f.write(nuovo_contenuto)


def processa_cartella(cartella):
    for root, _, files in os.walk(cartella):
        for nome_file in files:
            if nome_file.endswith(".md"):
                path_completo = os.path.join(root, nome_file)
                aggiorna_o_aggiungi_password(path_completo)


if __name__ == "__main__":
    TARGET_DIR = "."
    PASSWORD = "VAI VIA"
    processa_cartella(TARGET_DIR)
