import os
from PIL import Image
from PIL.ExifTags import TAGS

cartella = "cartella"

files = os.listdir(cartella)

i = 1
for file in files :
    percorso = os.path.join(cartella, file)

    # Saltiamo le sottocartelle
    if not os.path.isfile(percorso) :
        continue

    '''
        Saltiamo i file che non sono immagini:
            riduco il nome del file in minuscolo
            controllo se finisce con una sottostringa uguale ai tipi di file
                jpg, png, jpeg
            se non rispetta questo requisito interropo l'iterazione corrente 
            e vado al file successivo
    ''' 
    if not file.lower().endswith(('.jpg', '.png', '.jpeg')) :
        continue

    print(f"Trovata foto: {file}")

    try :
        # Apro l'immagine usando PIL (può generare errore se il file non è un'immagine)
        foto = Image.open(percorso)
        # Estraggo i metadati exif dall'immagine
        exif = foto._getexif()

        # Se non sono presenti metadati, esco dall'iterazione con continue
        if not exif:
            print(f"{file} non contiene metadati")
            continue

        # Estraggo i metadati usando le costanti TAGS che PIL ci fornisce
        metadati = {}
        for tag_id, valore in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            metadati[tag] = valore
        
        # Stampo data dello scatto e macchina utilizzata
        print(f"{file} è stata scattata il {metadati['DateTime']} usando {metadati['Model']}")
    except Exception as e:
        print(f"Errore nel file {file}: {e}")