#Dagens uppgift:
#- Skriv ett program som kollar på ett tal och avgör om det är ett primtal eller ej. ÄR det ett primtal, skriv ut det på skärmen. 
#- Omvandla delar av programmet till en funktion

x = 9

for x in range(2,21):
    prime = True
    for i in range(2,x):
        if x % i == 0:
            prime = False
            break
     
    if prime:
        print(x)
