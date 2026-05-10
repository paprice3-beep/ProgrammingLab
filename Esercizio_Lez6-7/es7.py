def menu_operazioni():
    while True:
        print("\n--- MENU ---")
        print("1. Calcolare la somma di due numeri")
        print("2. Calcolare la differenza tra due numeri")
        print("3. Uscire")
        
        scelta = input("Scegli un'opzione (1, 2 o 3): ")

        if scelta == "3":
            print("Arrivederci!")
            break
        
        if scelta in ["1", "2"]:
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
                
                if scelta == "1":
                    risultato = num1 + num2
                    print(f"Risultato della somma: {risultato}")
                else:
                    risultato = num1 - num2
                    print(f"Risultato della differenza: {risultato}")
            except ValueError:
                print("Errore: Inserisci dei valori numerici validi.")
        else:
            print("Errore: Opzione non valida. Inserisci 1, 2 o 3.")

