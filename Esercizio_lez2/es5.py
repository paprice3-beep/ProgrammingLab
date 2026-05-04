numero = int(input("inserisci un numero primo"))
if numero < 2 :
   prim0 = False
for i in range(2, numero):
    if (numero % i == 0):
       primo = False; break
       
       print(f"numero non è primo")
    else:
       print(f"numero  è primo")


    