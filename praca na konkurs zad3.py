from turtle import*
def koslawiec():
  seth(0)
  fillcolor("red")
  begin_fill()
  for i in range(4):
    fd(14);rt(90);fd(7);lt(90);fd(7);lt(90);fd(7);rt(90);fd(14);rt(90)
  end_fill()
def poziomy():
  seth(0)
  fillcolor("green")
  begin_fill()
  fd(21);lt(90);fd(7);lt(90);fd(21);lt(90);fd(7)
  end_fill()
def pionowy():
  seth(90)
  fillcolor("yellow")
  begin_fill()
  fd(21);lt(90);fd(7);lt(90);fd(21);lt(90);fd(7)
  end_fill()
#main
#poziomy()
#pionowy()
def piramida(ile):
  ilepion=ile
  pu();bk(21*ile);rt(90);fd(15*ile);lt(90);pd()
  for b in range (ilepion):
    for a in range (ile):
     print (a,b)
     koslawiec()
     pu();fd(35);rt(90);fd(21);lt(90);bk(7);pd()
     if a!=0:
       pu();lt(90);fd(14);lt(90);fd(7);rt(90);pd()
       pionowy()
       pu();fd(7);rt(90);fd(14);lt(90);pd()
     if a!=ile-1:
      poziomy()
      pu();lt(90);fd(14);lt(90);fd(21);pd()
    pu();lt(90);fd(9*7);rt(90);bk(6*7*(ile-1)-14);pd()
    ile=ile-1
# main
#liczba = int(input("Wysokosc piramidy: "))
#piramida(liczba)
#input("Takie Czekanie...")
  
  
