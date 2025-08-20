# -*- coding: utf-8 -*-

import os
import re


def raccogli_file_md(directory):
    """
    Restituisce la lista ordinata di file .md in una directory:
    - Prima i file direttamente nella root
    - Poi quelli nelle sottocartelle, in ordine alfabetico
    """
    root_files = []
    nested_files = []

    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for filename in sorted(files):
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                if os.path.abspath(root) == os.path.abspath(directory):
                    root_files.append(full_path)
                else:
                    nested_files.append(full_path)

    return root_files + nested_files


def unisci_file_md(file_list, output_path, base_dir):
    """
    Unisce una lista di file Markdown in un unico file.
    Inserisce intestazioni tra i file, tranne che prima del primo.
    Ogni intestazione include il path relativo del file come commento HTML.
    """
    PATTERN_3LINES = r'(?mi)^---\s*\r?\npassword:\s*.*\r?\n---\s*\r?\n?'
    with open(output_path, 'w', encoding='utf-8') as fout:
        for index, file_path in enumerate(file_list):
            if index > 0:
                rel_path = os.path.relpath(file_path, start=base_dir).replace('\\', '/')
                fout.write("---\n")
                fout.write(f"<!-- {rel_path} -->\n\n")
            with open(file_path, 'r', encoding='utf-8') as fin:
                contenuto = fin.read().rstrip()
                contenuto = re.sub(PATTERN_3LINES, '', contenuto)

                fout.write(contenuto + "\n\n")

    print(f"[OK] File unificato scritto in: {output_path}")


def processa_unione_md(source_dir, output_dir, output_name=None):
    """
    Elabora tutti i file .md in source_dir e li unisce in un file Markdown in output_dir.
    Se output_name è None, usa il nome della cartella sorgente come nome file.
    """
    os.makedirs(output_dir, exist_ok=True)

    nome_file = output_name or f"{os.path.basename(os.path.normpath(source_dir))}.md"
    output_path = os.path.join(output_dir, nome_file)

    file_md = raccogli_file_md(source_dir)
    if not file_md:
        print(f"[INFO] Nessun file .md trovato in: {source_dir}")
        return

    unisci_file_md(file_md, output_path, source_dir)


if __name__ == "__main__":
    OUTPUT_FOLDER = "../exports"

    processa_unione_md("../docs/md/base", OUTPUT_FOLDER)
    processa_unione_md("../docs/md/dm", OUTPUT_FOLDER)
    processa_unione_md("../docs/md/extra", OUTPUT_FOLDER)
    processa_unione_md("../docs/md/lore-tool", OUTPUT_FOLDER)
