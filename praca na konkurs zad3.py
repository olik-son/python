from turtle import*
def koslawiec():
  fillcolor("orange")
  begin_fill()
  for i in range(4):
    fd(14);rt(90);fd(7);lt(90);fd(7);lt(90);fd(7);rt(90);fd(14);rt(90)
  end_fill()
def poziomy():
  fillcolor("green")
  begin_fill()
  fd(21);lt(90);fd(7);lt(90);fd(21);lt(90);fd(7)
  end_fill()
def pionowy():
  fillcolor("yellow")
  begin_fill()
  fd(21);lt(90);fd(7);lt(90);fd(21);lt(90);fd(7)
  end_fill()
#main
koslawiec()
poziomy()
koslawiec()
poziomy()
koslawiec()
pionowy()
    
