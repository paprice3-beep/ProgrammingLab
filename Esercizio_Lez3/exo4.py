def hanno_elemento_communi(lista1,lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return not set1.isdisjoint(set2)