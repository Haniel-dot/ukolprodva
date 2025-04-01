#Míša úkol B
sport1= input ("zadejte první sport")
sport2 = input ("zadejte druhý sport")

cas_sport1 = int (input("zadejte kolik minut jste dělal první sport"))
cas_sport2 = int (input ("zadejte kolik minut jste dělal druhý sport"))

výsledek= (cas_sport1 + cas_sport2)
celkový_výdej= výsledek/5 
print ("spálil jste" , str(celkový_výdej), "kalorií")
