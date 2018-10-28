from turtle import*
def koslawiec():
  seth(0)
  fillcolor("orange")
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
ile=3
for a in range (ile):
   print (a)
   koslawiec()
   pu();fd(35);rt(90);fd(21);lt(90);bk(7);pd()
   if a!=0:
     pu();fd(21);lt(90);fd(7);pd()
     pionowy()
   if a!=ile-1:
    poziomy()
    pu();lt(90);fd(14);lt(90);fd(21);pd()
   

  
  
