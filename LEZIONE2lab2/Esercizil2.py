import numpy as np

# 1. Creazione del vettore con i numeri primi tra 0 e 20
primi = np.array([2, 3, 5, 7, 11, 13, 17, 19])

# 2. Selezionare le voci maggiori di 10

maggiori_dieci = primi[primi > 10]

# 3. Selezionare tutti i numeri primi pari
# Il test logico controlla dove il resto della divisione per 2 è zero
primi_pari = primi[primi % 2 == 0]

# --- STAMPA RISULTATI ---
print(f"Vettore originale: {primi}")
print(f"Numeri > 10:       {maggiori_dieci}")
print(f"Numeri primi pari: {primi_pari}")

# Esempio di cosa accade "sotto il cofano" con il test logico:
print(f"\nMaschera logica per > 10: {primi > 10}")

#exo2

import numpy as np

# 1. Crea un array 2D (5 righe x 3 colonne) senza digitarlo
# Usiamo arange e reshape per generare una matrice da 1 a 15
a = np.arange(1, 16).reshape(5, 3)

# 2. Genera l'array 'b' con la 2ª e la 4ª riga
# Ricorda: l'indicizzazione in Python parte da 0, quindi usiamo [1, 3]
b = a[[1, 3], :]

# 3. Genera l'array 'c' con la 3ª riga (indice 2)
# Usiamo il slicing [2:3] per mantenere la struttura 2D necessaria al calcolo dopo
c = a[2:3, :]

# 4. Dividi ogni colonna di 'a' per l'array 'c'
# Grazie al broadcasting, NumPy divide ogni riga di 'a' per la riga 'c'
divisione = a / c

print("Array a (Originale 5x3):")
print(a)

print("\nArray b (2ª e 4ª riga):")
print(b)

print("\nArray c (Solo 3ª riga):")
print(c)

print("\nRisultato divisione (a / c):")
print(divisione)

#exo3

import numpy as np

# 1. Genera un array 10x3 con numeri casuali tra 0 e 1
np.random.seed(42)
a = np.random.rand(10, 3)

# 2. Calcola la distanza assoluta da 0.5
distanze = np.abs(a - 0.5)


indici_minimi = np.argmin(distanze, axis=1)

# 4. Fancy Indexing per estrarre i valori
# Creiamo un array di indici per le righe [0, 1, 2, ..., 9]
indici_righe = np.arange(10)

# Selezioniamo gli elementi usando (indici_righe, indici_colonne)
numeri_vicini = a[indici_righe, indici_minimi]

# --- OUTPUT ---
print("Matrice Casuale (10x3):")
print(a)
print("\nIndici dei valori più vicini a 0.5 per riga:")
print(indici_minimi)
print("\nValori selezionati:")
print(numeri_vicini)

#exo4
import numpy as np

# 1. Inserimento dei dati in un array NumPy
hr_data = np.array([
    68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 
    162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70
])

# 2. Frequenza cardiaca minima (riposo)
hr_min = hr_data.min()

# 3. Frequenza cardiaca massima 
hr_max = hr_data.max()

# 4. Creazione dell'array booleano
# True se > 120, False altrimenti
is_exercise = hr_data > 120

# 5. Calcolo della percentuale di osservazioni sopra 120
percentuale_esercizio = np.mean(is_exercise) * 100

# --- OUTPUT ---
print(f"Frequenza minima (Riposo): {hr_min} bpm")
print(f"Frequenza massima (Picco): {hr_max} bpm")
print(f"\nArray booleano 'is_exercise':\n{is_exercise}")
print(f"\nPercentuale di tempo in esercizio: {percentuale_esercizio:.2f}%")

#exo5

import numpy as np

# 1. Creazione del vettore iniziale
stipendi = np.array([50000, 105250, 55000, 89000])

# Costo totale iniziale
costo_iniziale = stipendi.sum()
print(f"Costo totale iniziale: ${costo_iniziale:,}")

# 2. Il problema del CEO e del dtype
# Se proviamo ad aggiornare lo stipendio del CEO:
# stipendi[1] = stipendi[1] * 1.15  <-- Questo causerebbe un troncamento!
# Motivo: l'array è stato creato come 'int', quindi non può contenere decimali.

# 3. Ricreazione del vettore con dtype corretto (float)
stipendi = np.array([50000, 105250, 55000, 89000], dtype=float)

# Aumento al CEO (15%)
stipendi[1] *= 1.15
print(f"Nuovo stipendio CEO: ${stipendi[1]:,.2f}")

# 4. Aumento all'impiegata con stipendio più basso (20%)
# Usiamo l'indicizzazione booleana per trovare il minimo in modo dinamico
stipendi[stipendi == stipendi.min()] *= 1.20

# 5. Aumento agli altri dipendenti (10%)
# Selezioniamo chi non ha ancora ricevuto l'aumento (stipendi originali rimasti)
# In questo caso agiamo sugli indici 2 e 3 (55.000 e 89.000)
mask_altri = (stipendi == 55000) | (stipendi == 89000)
stipendi[mask_altri] *= 1.10

# 6. Calcoli finali
costo_finale = stipendi.sum()
differenza_totale = costo_finale - costo_iniziale

print(f"\nVettore stipendi finale: {stipendi}")
print(f"Costo totale finale: ${costo_finale:,.2f}")
print(f"Aumento totale dei costi aziendali: ${differenza_totale:,.2f}")

#exo6

import numpy as np

# 1. Caricamento dei dati
# Assumiamo che il file contenga un array 1D di valori di CO2
try:
    co2_data = np.load('emissioni_co2.npy')
except FileNotFoundError:
    # Generiamo dati di esempio se il file non è presente per testare il codice
    co2_data = np.random.uniform(5, 30, 100) 

# 2. Definizione della soglia
soglia = 18

# 3. Maschera booleana per valori sopra la soglia
maschera_sopra = co2_data > soglia

# 4. Calcolo del numero di valori e della media
valori_sopra = co2_data[maschera_sopra]
quantita = len(valori_sopra)
media_sopra = valori_sopra.mean() if quantita > 0 else 0

# 5. Calcolo della frazione totale di emissione
somma_sopra = valori_sopra.sum()
somma_totale = co2_data.sum()
frazione_emissioni = somma_sopra / somma_totale

# --- OUTPUT ---
print(f"Analisi Emissioni CO2 (Soglia: {soglia} tonnellate)")
print("-" * 45)
print(f"Numero di rilevazioni sopra soglia: {quantita}")
print(f"Valore medio sopra soglia:          {media_sopra:.2f} tonnellate")
print(f"Frazione totale sopra la soglia:    {frazione_emissioni:.2%} del totale")

#exo7

import numpy as np

survey_matrix = np.array([
    [25, 40000, 10], 
    [32, 52000, 12], 
    [40, 63000, 14], 
    [29, 47000, 11], 
    [35, 58000, 13]
])

# 1. Seleziona gli intervistati con almeno 12 anni di istruzione
# Usiamo la colonna indice 2 per il test logico
intervistati_istruiti = survey_matrix[survey_matrix[:, 2] >= 12]

# 2. In un'unica riga: seleziona i REDDITI degli intervistati con almeno 12 anni di istruzione
redditi_istruiti = survey_matrix[survey_matrix[:, 2] >= 12, 1]

# 3. In un'unica riga: calcola il REDDITO MEDIO degli intervistati con almeno 12 anni di istruzione
reddito_medio = survey_matrix[survey_matrix[:, 2] >= 12, 1].mean()

# --- OUTPUT ---
print("Intervistati con istruzione >= 12 anni:")
print(intervistati_istruiti)
print(f"\nSolo i redditi: {redditi_istruiti}")
print(f"Reddito medio:  ${reddito_medio:,.2f}")

#exo8

import numpy as np

# Caricamento del vettore ages
ages = np.array([92, 108, 75, 63, 62, 66, 90, 98, 97, 92, 60, 107, 90, 71, 97, 86, 55, 55,
                 98, 57, 96, 104, 96, 94, 72, 98, 111, 98, 89, 69, 77, 92, 85, 101, 93, 100,
                 90, 101, 96, 98, 999, 87, 106, 86, 108, 55, 67, 65, 68, 59, 67, 72, 57, 79,
                 95, 67, 86, 70, 91, 111, 67, 75, 59, 88, 90, 99, 94, 65, 111, 103, 100, 70,
                 63, 65, 100, 110, 999, 70, 57, 75, 56, 104, 111, 90, 74, 100, 90, 86, 88, 99,
                 58, 103, 88, 103, 64, 96, 105, 89, 83, 65, 100, 62, 73, 105, 83, 105, 58, 96,
                 77, 74, 95, 109, 91, 101, 91, 999, 63, 111, 97, 108, 75, 77, 73, 58, 94, 83,
                 90, 61, 110, 107, 105, 85, 64, 66, 71, 107, 105, 72, 78, 66, 100, 102, 72, 999,
                 74, 68, 73, 72, 90, 93, 99, 55, 92, 83, 58, 71, 89, 75, 98, 87, 999, 78,
                 97, 71, 106, 83, 58, 81, 100, 72, 93, 70, 65, 60, 95, 107, 94, 77, 87, 90,
                 82, 56, 99, 107, 86, 56, 73, 96, 64, 69, 64, 92, 57, 104, 110, 69, 66, 68,
                 84, 89, 72, 80, 55, 75, 87, 57, 106, 69, 66, 62, 102, 76, 111, 999, 96, 83,
                 84, 61, 102, 63, 107, 63, 76, 58, 83, 58, 61, 71, 77, 90, 74, 100, 103, 74,
                 92, 102, 63, 87, 93, 61, 63, 86, 74, 98, 64, 999, 78, 95, 84, 81, 107, 85,
                 79, 82, 89, 65, 107, 57, 74, 77, 97, 92, 58, 96, 105, 60, 55, 74, 57, 80,
                 62, 85, 87, 62, 999, 71, 74, 70, 97, 59, 82, 96, 105, 70, 89, 105, 60, 70,
                 87, 999, 64, 108, 107, 104, 85, 95, 108, 74, 64, 97, 89, 88, 79, 67, 81, 92,
                 63, 80, 76, 94, 104, 67, 73, 61, 99, 96, 68, 90, 86, 79, 85, 111, 75, 98,
                 81, 111, 108, 103, 85, 72, 108, 102, 999, 64, 107, 112, 66, 93, 89, 78, 66, 92,
                 63, 101, 92, 64, 72, 56, 71, 64, 87, 78, 107, 85, 109, 95, 69, 111, 64, 72,
                 55, 66, 99, 57, 78, 55, 58, 90, 88, 71, 90, 103, 92, 98, 67, 97, 77, 68,
                 77, 59, 78, 69, 77, 81, 61, 99, 999, 85, 78, 104, 97, 95, 74, 70, 69, 83,
                 68, 68, 77, 60, 85, 82, 93, 66, 71, 62, 64, 107, 999, 65, 78, 59, 83, 67,
                 108,  58,  95, 106,  83,  79,  67,  59,  96,  90,  55,  55,  96, 109,  82,  55, 101,  58,
                 97, 77, 60, 81, 999, 81, 75, 100, 66, 65, 105, 94, 101, 56, 999, 59, 105, 59,
                 93, 56, 104, 74, 81, 62, 76, 65, 107, 60, 107, 98, 77, 86, 83, 104, 74, 69,
                 97, 80, 91, 56, 108, 87, 65, 91, 93, 60, 91, 110, 107, 88, 96, 70, 60, 99,
                 66, 91, 107, 65, 81, 109, 84, 106, 80, 92, 78, 84, 91, 59])

# 1. Rimuovere i dati errati (999) usando l'indicizzazione booleana
clean_ages = ages[ages != 999]

# 2. Trovare l'età massima tra i dati puliti
oldest_citizen = clean_ages.max()

# 3. Conteggio degli errori per curiosità
num_errors = np.sum(ages == 999)

print(f"Numero di errori rimossi: {num_errors}")
print(f"Numero di cittadini validi analizzati: {len(clean_ages)}")
print(f"L'età del cittadino più anziano è: {oldest_citizen} anni")

#exo9

import numpy as np

lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 'VERDURA', 'IMPERO', 'RICEVIMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA', 'AGONIA', 'RECUPERO',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 'ANNUNCIO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA',
    'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE'
]

# 1. Estrazione casuale di 5 parole con reinserimento (replace=True)
parole_estratte = np.random.choice(lista_parole, size=5, replace=True)

# 2. Definizione del template della storia 
storia_template = (
    "In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico {0} che proteggeva. "
    "Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto "
    "abbondante e le offrì il {1} come dono, i suoi occhi si spalancarono e lei esclamò una sola parola, \"{2}\". "
    "Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un {3}. "
    "Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla "
    "donna saggia per donarglielo. Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna "
    "saggia guardò i suoi compaesani e disse: \"Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza {4}!\" "
    "Ci fu grande gioia e celebrazione."
)

# 3. Riempimento e stampa della storia
storia_finale = storia_template.format(*parole_estratte)

print("--- PAROLE ESTRATTE ---")
print(parole_estratte)
print("\n--- LA TUA STORIA ---")
print(storia_finale)