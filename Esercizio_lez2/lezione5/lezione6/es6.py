def calcola_quadrato():
    while True:
        valore = input("Inserisci un numero intero: ")
        try:
            numero = int(valore)
            quadrato = numero ** 2
            print(f"Il quadrato di {numero} è {quadrato}")
            break
        except ValueError:
            print(f"Errore: '{valore}' non è un numero intero valido. Riprova.")

calcola_quadrato()