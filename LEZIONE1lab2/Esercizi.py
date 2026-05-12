 #exo1
#1
numeri = [1, 2, 3, 4, 5]
quadrati = []

for n in numeri:
    quadrati.append(n**2)

#comprehension di lista 
quadrati = [n**2 for n in numeri]

#2
numeri = range(10)
pari = []

for n in numeri:
    if n % 2 == 0:
        pari.append(n)

#Comprensione di lista:

pari = [n for n in numeri if n % 2 == 0]

#3
utenti = [" rey ", "tor", " patricia "]
tab = []

for nome in utenti:
    tab.append(nome.strip().capitalize())

#Comprensione di lista:

puliti = [nome.strip().capitalize() for nome in utenti]

#exo2
# 1. Creazione manuale del vettore (numeri primi tra 0 e 10)
# I numeri primi sono: 2, 3, 5, 7
vettore_primi = np.array([2, 3, 5, 7])

# 2. Conteggio degli elementi
conteggio_len = len(vettore_primi)
conteggio_size = vettore_primi.size

print(f"Vettore: {vettore_primi}")
print(f"Lunghezza con len(): {conteggio_len}")
print(f"Grandezza con .size: {conteggio_size}")

# 3. Ragionamento sul dtype
# Risposta ipotetica: Poiché abbiamo inserito solo numeri interi piccoli, 
# il dtype sarà probabilmente int64 (o int32 a seconda del sistema).
print(f"Tipo di dato (dtype): {vettore_primi.dtype}")

# 4. List Comprehension per trovare i numeri primi tra 0 e 10
# Un numero 'n' è primo se è > 1 e non ha divisori oltre a 1 e se stesso
primi_lc = np.array([
    n for n in range(11) 
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
])

print(f"Vettore generato con list comprehension: {primi_lc}")

#exo3
#array

# Creiamo un array 'a' 1D senza digitarlo (es. da 1 a 5)
a = np.arange(1, 6) 

# Creiamo 'b' estraendo una "sottostringa" (slicing)
# Nota: negli array numerici si intende una sotto-porzione del vettore
b = a[1:4]  # Prende gli elementi dall'indice 1 al 3: [2, 3, 4]

# Creiamo 'c' come reverse di 'a'
c = a[::-1] # Risultato: [5, 4, 3, 2, 1]

# Divisione tra array 'a' e 'c'
# NumPy esegue la divisione elemento per elemento (element-wise)
divisione_array = a / c

print("--- NUMPY ARRAY ---")
print(f"Array a: {a}")
print(f"Sottostringa b: {b}")
print(f"Reverse c: {c}")
print(f"Divisione (a / c): {divisione_array}\n")

# --- 2. OPERAZIONI CON LISTE  ---
# Creiamo una lista 'a_list'
a_list = list(range(1, 6))

# Sottostringa  della lista
b_list = a_list[1:4]

# Reverse della lista
c_list = a_list[::-1]

# Divisione tra liste 'a_list' e 'c_list'
divisione_lista = [x / y for x, y in zip(a_list, c_list)]

print("--- LISTE STANDARD ---")
print(f"Lista a: {a_list}")
print(f"Sottostringa b: {b_list}")
print(f"Reverse c: {c_list}")
print(f"Divisione (tramite comprehension): {divisione_lista}")
