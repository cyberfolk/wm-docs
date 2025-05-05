# -*- coding: utf-8 -*-

import os

# === CONFIGURA QUI ===
cartella_target = "docs/dm"
password_da_inserire = "VAI VIA"


def ha_frontmatter(file_md):
    with open(file_md, 'r', encoding='utf-8') as f:
        prima_riga = f.readline()
        return prima_riga.strip() == "---"


def aggiungi_password(file_md):
    with open(file_md, 'r', encoding='utf-8') as f:
        contenuto = f.read()

    blocco_password = f"---\npassword: {password_da_inserire}\n---\n\n"
    nuovo_contenuto = blocco_password + contenuto

    with open(file_md, 'w', encoding='utf-8') as f:
        f.write(nuovo_contenuto)

    print(f"[OK] Password inserita in: {file_md}")


def processa_cartella(cartella):
    for root, _, files in os.walk(cartella):
        for nome_file in files:
            if nome_file.endswith(".md"):
                path_completo = os.path.join(root, nome_file)
                if not ha_frontmatter(path_completo):
                    aggiungi_password(path_completo)
                else:
                    print(f"[OK] Frontmatter già presente: {path_completo} (skippato)")


if __name__ == "__main__":
    processa_cartella(cartella_target)
