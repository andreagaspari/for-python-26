import os

cartella = "cartella"

files = os.listdir(cartella)

i = 1
for file in files :
    # Prendi il percorso relativo del file corrente
    vecchio_nome = os.path.join(cartella, file)
    # Crea il percorso relativo del file rinominandolo in 'file 1.txt' (1, 2, 3, ...)
    nuovo_nome = os.path.join(cartella, f"file {i}.txt")

    # Rinomina il file
    os.rename(vecchio_nome, nuovo_nome)
    i += 1