def è_palindromo(testo):
    testo_pulito = testo.replace(" " , "  ").lower
    return testo_pulito == testo_pulito[ : : -1]
