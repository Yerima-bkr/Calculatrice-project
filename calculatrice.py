def soustraction(a,b):
    return a -b;

def addition(a,b):
    return a + b;

def multiplication(a,b):
    return a * b;

def division(a,b):
    if b ==0 :
         return print("Erreur, impossible de diviser un nombre par 0 ");
    else : return a / b;

def modulo(a,b):
    if b == 0 :
         return print("Erreur, impossible de diviser un nombre par 0 ");
    else : return a % b;

print("Bonjour et bienvenue dans notre mini calculatrice !")
a=int(input("Entrer le premier nombre :"));
b=int(input("Entrer le deuxieme nombre :"));

print("Voici les opérations que nous pouvons effectuer :")
print("1- Soustraction")
print("2- Addition")
print("3- Multiplication")
print("4- Division")
print("5- Modulo")
operateur=int(input("Veuiller choisir l'opération que vous aimeriez effectuer :" ))
if operateur == 1:
 print("La soustraction de", a, "et de", b, "est :", soustraction(a,b));
elif operateur == 2:
    print("L'addition de",a, "et de", b, "est :", addition(a,b));
elif operateur == 3:
    print("La multiplication de ",a, "et de", b, "est :", multiplication(a,b));
elif operateur == 4 :
        print("La division de", a, "et de", b, "est :", division(a,b));
elif operateur == 5:
        print("Le modulo de", a, "et de", b, "est :", modulo(a,b));
else : print("Cette opération n'existe pas, veuillez réessayer !")