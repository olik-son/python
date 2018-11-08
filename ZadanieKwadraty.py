from turtle import*
def dol(bok):
    fillcolor("tomato")
    begin_fill()
    for i in range(4):
        fd(bok);rt(90)
    end_fill()
    fd(bok)
def gora(bok):
    fillcolor("green")
    begin_fill()
    lt(90)
    for i in range(6):
        fd(bok);rt(90)
    fd(bok);lt(90)
    end_fill()
def kwadraty (liczby):
    liczbystr=str(liczby)
    iloscliczb=len(liczbystr)
    print("moj string: ", liczbystr)
    print("ilosc liczb: ", iloscliczb)
    bok=480/iloscliczb
    pu();bk(240);pd()
    for i in range(iloscliczb):
        cyfra=int(liczbystr[i])
        print ("Kolejna cyfra:",cyfra)
        if (cyfra % 3) == 0:
            print("podzielna przez 3 - gora")
            gora(bok)
        else:
            print("nie jest podzielna przez 3 - dol")
            dol(bok)
#main
#kwadraty(2458)
