def kolejna(liczbapoczatkowa,kolejnaliczba):
 licznik = 1
 koniec = 0
 kolejna =0
 while koniec < 1 :
    wynik = liczbapoczatkowa + licznik
    wynikstr=str(wynik)
    if (wynikstr.find('3') != 0):
      kolejna = kolejna + 1
    if kolejnaliczba==1:
        kolejnaliczba=0
    if kolejna == kolejnaliczba+1:
        koniec = 2
    licznik += 1
    print("string: ", wynikstr)
    czytrzy = wynikstr.find('3')
    print ("czy trzy: ", czytrzy)
    print ("kolejna: ",kolejna)
 return wynik
#main
#a = int(input("Liczba poczatkowa: "))
#b = int(input("Liczba kolejna bez 3: "))
#mojwynik=kolejna(a,b)
#print("----------------------------------------------------")
#print("moj wynik: ",mojwynik)
#print("----------------------------------------------------")
