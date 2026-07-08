"""nom = input("quel est vutre nom?")
age = input("quel est votre age ?")

try:
    age_prochain = int(age) + 1
except:
    print("error: l'age doit etre un nombre entier")
else:
     print(f"bonjour {nom},vous avez {age} ans.")
     print(f"l'annee prochaine vous aurez {age_prochain} ans")"""


"""age=0
def demande_age():
  global age
  while age==0:
       age_str=input("quel est votre age ?")
       try:
           age=int(age_str)
       except:
           print("error: l'age doit etre un entier")
#print("fin de la boucle")
  
  


demande_age()
print(f"vous avez{age} ans")
print(f"l'annee prochaine vous aurez {age+1} ans")"""

"""def information_persone(nom ):
    #print(f"bonjour {nom}, vous avez {age} ans.")
     print(f"le nom comporte {len(nom)} caracteres")
print("debut du programme")

information_persone("mars")

print("fin du programme")"""

"""def afficher_table_multiplication(nombre):
    for i in range (1, 11):
        resultat = nombre * i
        print(f"{nombre} * {i} = {resultat}")

afficher_table_multiplication(4)"""

"""def project_questionnaire(question, r1, r2, r3, r4, choix_bonne_reponse):
   global score
   print("QUESTION")
   print(" " + question)
   print(" (a)", r1)
   print(" (b)", r2)
   print(" (c)", r3)
   print(" (d)", r4)
   print()
   reponse = input("votre reponse: ")
   if reponse == choix_bonne_reponse:
       print("bonne reponse")
       score += 1
   else:
       print("mauvaise reponse")
   print()
   print()


score=10   
project_questionnaire("quelle est la capitale de la france?", "paris", "nice", "londres", "berlin", "a")
print("score final:", score)"""

personne = ["marine", "fouda", "floris"]
#print(len(personne))
#print(personne[-1])

#for i in range(0, len(personne)):
    #print(personne[i])

"""nouvel_liste = "fredy"
print(personne)
personne.append(nouvel_liste)
print(personne)

del personne[-1]
print(personne)"""

def obtenir_infos():
    return "melani", 34, 1.67

nom, age, taille = obtenir_infos()
print(f"informations: nom: {nom}, age: {age}, taille: {taille}")