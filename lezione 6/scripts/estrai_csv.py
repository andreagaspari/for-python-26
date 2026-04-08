import os
import pandas as pd

cartella = "cartella"

for file in os.listdir(cartella) :
    # Creo il percorso relativo del file
    percorso_file = os.path.join(cartella, file)

    # Salto i NON file
    if not os.path.isfile(percorso_file) :
        continue

    # Salto i file NON CSV
    if not file.lower().endswith(".csv") :
        continue

    # Leggo i dati usando Pandas
    dati_file = pd.read_csv(percorso_file)

    # Stampo la tabella intera 
    print(dati_file)

    # Stampo Nome e numero di telefono
    for indice, riga in dati_file.iterrows():
        print(f"{riga['nome']}: {riga['telefono']}")