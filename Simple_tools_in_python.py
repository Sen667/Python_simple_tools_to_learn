#fonction valeur = 1
def calculer_age(nir):    
  #Condition | le NIR doit contenir uniquement des Chiffre et il doit y en avoir strictement 13

    # Extraire les composantes du NIR
 s = int(nir // 10**12)  # Sexe
 aa = int((nir // 10**10) % 100)  # Année
 m = int((nir // 10**8) % 100)  # Mois
 d = int((nir // 10**6) % 100)  # Département
 c = int((nir // 10**3) % 1000)  # Commune
 r = int(nir % 1000)  # Registre
 if aa <= 22:
        annee_naissance = 2000 + aa
 else:
        annee_naissance = 1900 + aa
        age = 2022 - annee_naissance
 return age                 


#fonction valeur = 4
def definir_une_annee_valide(annee1,mois1,jours1):
    if mois1 <1 or mois1 > 12 :
        return False    
    jours_valide = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if annee1 % 4 == 0 and (annee1 % 100 != 0 or annee1 % 400 == 0):
        jours_valide[1] = 29    
    if jours1 < 1 or jours1 > jours_valide[mois1 - 1]:
        return False
    return True

#Recommencer si l'option n'est pas valide
valeur = int(input("\n Choisissez une option :"
                    "\n1 - Calculer l'âge à partir d'un NIR" #Valeur == 1
                    "\n2 - Vérifier si c'est un multiple de 7" #Valeur == 2
                    "\n3 - Convertisseur miles en km/h"  #Valeur == 3
                    "\n4 - Vérifie si une date est valide (En maintenance)"#Valeur == 4
                    "\n5 - Donne l'inverse d'un nombre "
                    "\n0 - Eteindre le programme "))

while valeur  > 5 or valeur < 1:
    valeur=int(input("Option invalide, réessayer svp"
                      "\n Choisissez une option :"
                      "\n1 - Calculer l'âge à partir d'un NIR" #Valeur == 1
                      "\n2 - Vérifier si c'est un multiple de 7" #Valeur == 2
                      "\n3 - Convertisseur miles en km/h"  #Valeur == 3
                      "\n4 - Vérifie si une date est valide (En maintenance)"#Valeur == 4
                      "\n5 - Donne l'inverse d'un nombre "
                      "\n0 - Eteindre le programme ")) #Valeur == 5


#Calculer un INR
if valeur == 1:

    nir = int(input("Saisir votre NIR (13 chiffres) :"))
    age_personne = calculer_age(nir)
    print("L'âge de la personne est de", age_personne, "ans"),
    retour_menu= str(input("Retourner au menu ? (reply yes or no plz) "))

    if retour_menu == "yes" or "Yes" or "1" or "True":
       valeur = int(input("\n Choisissez une option :"
                    "\n1 - Calculer l'âge à partir d'un NIR" #Valeur == 1
                    "\n2 - Vérifier si c'est un multiple de 7" #Valeur == 2
                    "\n3 - Convertisseur miles en km/h"  #Valeur == 3
                    "\n4 - Vérifie si une date est valide (En maintenance)"#Valeur == 4
                    "\n5 - Donne l'inverse d'un nombre "))
       
    else: print("Fin du programme \n Aurevoir ")
    

#Verifier si c'est un multiple de 7
elif valeur == 2:
    multiple = int(input("Donner un entier:")) 
    if multiple % 7 == 0:
         print(multiple,"est un multiple de 7") 
    else:
         print(multiple,"n'est pas un multiple de 7")

#Convertire une distance en miles en Km/h
elif valeur == 3:
    S1 = int(input("Convertisseur \n [1] Convertire la distance miles -> km/h \n [2] Convertire la distance km/h -> miles"))
    if S1 == 1:
     distance_en_miles = float(input("Distance en miles:"))
     distance_en_km = distance_en_miles * 1.609
     print("Distance en kilomètres:", distance_en_km)
    if S1 == 2:
     distance_en_km2 = int(input("Distance en km/h:"))
     distance_en_km1 = distance_en_km2 / 1.609
     print("Distance en miles:", distance_en_km1)
    else:
        print("fonctionnalité pas encore disponile désole")

#Vérifier si une date est valide
elif valeur == 4: #Non Fonctionnel a revoir !
    jours1 = int(input("Jours ?"))
    mois1 =int(input("Mois ? "))
    annee1 = int(input("Annee ? "))
    if definir_une_annee_valide(jours1, mois1, annee1):
      print("Date valide !")
    else:
        print("Date non valide !")

#Donne l'inverse d'un nombre 
elif valeur == 5:
    def inverse(nombre):
     while nombre == 0:
        nombre = float(input("Erreur, veuillez saisir un réel non nul : "))
     return 1 / nombre
    
    nombre = float(input("Donnez un réel non nul : "))
    resultat = inverse(nombre)
    print("L'inverse de",nombre ,"est",resultat) 

elif valeur == 0:
        print ("Fin du programme")
else:
    print("Option invalide")
