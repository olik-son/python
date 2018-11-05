from turtle import*
def atleci(ile):
  pu();bk(45*ile);rt(90);fd(3);lt(90);pd()
  for i in range(ile):
    fillcolor("yellow")
    fd(40); bk(15)
    begin_fill()
    lt(90);fd(10);lt(90);fd(10);lt(90);fd(10)
    end_fill()
    fillcolor("green")
    rt(90);fd(5);lt(90)
    begin_fill()
    fd(20);lt(90);fd(20);lt(90);fd(20);lt(90);fd(20)
    end_fill()
    lt(90);fd(40);rt(90);fd(10)
    pu();bk(30);pd();bk(10);fd(10);rt(90);fd(20)
    fd(20);rt(90);fd(10);pu();bk(40);pd()
    if i % 2 == 0:
        #sztanga na dole
        print("dol")
        rt(90);fd(20);pu();fd(5);pd();rt(90);fd(20);bk(80);fd(20);lt(90);pu();fd(5);pd();pu();bk(10);pd();bk(20);fd(20);pu();fd(5);pd();lt(90);fd(10);lt(90);fd(5);bk(10);fd(5);fd(5);bk(5);rt(90)
        #huhyhy
        fd(5);lt(90);fd(10);bk(20);fd(10);rt(90)
        fd(5);lt(90);fd(15);bk(30)
        fd(15);lt(90)
        fd(80);lt(90);fd(15);bk(30);fd(15);rt(90);bk(5);rt(90);fd(10);bk(10);fd(10);bk(20);fd(10);rt(90);fd(5);lt(90);fd(5);bk(10)
        pu();fd(30);rt(90);fd(10);fd(90);pd()      
    else:
        #sztanga na gore
        print("gora")
        lt(90);fd(20);lt(90);fd(20);bk(80);fd(20);lt(90);fd(20);bk(20);rt(90);bk(10)
        lt(90);fd(5);bk(10);fd(5);lt(90)
        fd(5);lt(90);fd(10);bk(20);fd(10);rt(90)
        fd(5);lt(90);fd(15);bk(30)
        fd(15);lt(90)
        fd(80);lt(90);fd(15);bk(30);fd(15);rt(90);bk(5);rt(90);fd(10);bk(10);fd(10);bk(20);fd(10);rt(90);fd(5);lt(90);fd(5);bk(10)
        fd(5);rt(90);fd(10);rt(90);fd(20);lt(90);pu();fd(90);pd()
# main
#liczba = int(input("Ile Ma byc Atletow: "))
#atleci(liczba)

