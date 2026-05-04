def conta_vocali(testo):
    vocali = "aeiouAEIOU"
    contatore = 0
    
    for carattere in testo:
        if carattere in vocali:
            contatore += 1
            
    return contatore