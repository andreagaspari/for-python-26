'''
    Organizza le foto in sotto cartelle Anno/Mese
'''
import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

def get_data_scatto(percorso_file) :
    '''
        Recupera la data dello scatto dai metadati dell'immagine

        Parametri:
            (str) percorso_file Il file completo di path relativo

        Ritorna:
            (str) La data in cui è stata scattata la foto
    '''
    try :
        # Apro l'immagine usando PIL (può generare errore se il file non è un'immagine)
        foto = Image.open(percorso_file)
        # Estraggo i metadati exif dall'immagine
        exif = foto._getexif()

        # Se non sono presenti metadati, esco dalla funzione ritornando None
        if not exif:
            return None

        # Estraggo i la data se presente usando le costanti TAGS che PIL ci fornisce
        for tag_id, valore in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTime" :
                return valore
            
    except Exception as e:
        return None
    
    return None

cartella_foto = "cartella"

for file in os.listdir(cartella_foto) :
    percorso_file = os.path.join(cartella_foto, file)

    # Salto i NON file
    if not os.path.isfile(percorso_file) :
        continue

    # Salto i file NON immagine
    if not file.lower().endswith((".jpg", ".jpeg", ".png")) :
        continue

    data_scatto = get_data_scatto(percorso_file)

    # Salto se data_scatto è NONE
    if data_scatto is None:
        continue

    # EXIF ha uno standard di formato data AAAA:MM:DD HH:MM:SS
    anno = data_scatto[0:4] # Sottostringa da indice 0 (incluso) a indice 4 (escluso)
    mese = data_scatto[5:7] # Sottostringa da indice 5 (incluso) a indice 7 (escluso)
    
    # Creo il percorso per le sottocartelle ANNO/MESE
    cartella_destinazione = os.path.join(cartella_foto, anno, mese)

    # Creo, se non esistono, le sottocartelle ANNO/MESE
    os.makedirs(cartella_destinazione, exist_ok=True)

    # Creo il nuovo percorso relativo della foto
    nuovo_percorso_file = os.path.join(cartella_destinazione, file)

    # Muovo la foto nella sotto cartella
    shutil.move(percorso_file, nuovo_percorso_file)

