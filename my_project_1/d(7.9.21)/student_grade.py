print(''' YOUR GRADING SYSTEM
           0  TO 39 ----GRADE "A"
           40 TO 59 ----GRADE "B"
           60 TO 79 ----GRADE "C"
           80 TO 100----GRADE "D"''')
x=int(input("enter your marks:"))
if 0<x<40:
    print(f"your mark is {x} and your grade is \"A\" ")
if 40<=x<60:
    print(f"your mark is {x} and your grade is \"B\" ")
if 60<=x<80:
    print(f"your mark is {x} and your grade is \"C\" ")
if 80<=x<=100:
    print(f"your mark is {x} and your grade is \"D\" ")
