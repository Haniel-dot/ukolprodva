opak="ano"

while opak=="ano":

    #hanca_ukola
    j1=input("zadejte prvni jidlo co jste jedl")
    j2=input("zadejte druhe")
    j3=input("zadejte treti")
    j1k=int(input("kalorie prvniho"))
    j2k=int(input("kalorie druheho"))
    j3k=int(input("kalorie tretiho"))

    celkova_kalorie=j1k+j2k+j3k
    
    print(celkova_kalorie)

    #Míša úkol B
    sport1= input ("zadejte první sport")
    sport2 = input ("zadejte druhý sport")

    cas_sport1 = int(input("zadejte kolik minut jste dělal první sport"))
    cas_sport2 = int(input ("zadejte kolik minut jste dělal druhý sport"))

    výsledek= (cas_sport1 + cas_sport2)
    celkový_výdej= výsledek/5 
    print ("spálil jste" , str(celkový_výdej), "kalorií")

    cel=celkova_kalorie-celkový_výdej

    print(f"Snědla jste {celkova_kalorie:.1f} a spálila jste {celkový_výdej:.1f}.")

    if cel>0:
        print(f"přebytek: {cel} kalorii")
    else:
        print(f"nedostatek: {cel} kalorii")

    input("chcete opakovat")


