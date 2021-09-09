def calc_1(x,a,b):
    if x=="add":
        print(a+b)
    elif x=="sub":
        print(a-b)
    elif x=="mul":
        print(a*b)
    elif x=="div":
        print(a/b)
    elif x=="mod":
        print(a%b)
    elif x=="exp":
        print(a**b)
    elif x=="flo":
        print(a//b)
def calc_2(x,a,b):
    if x == 'rst':
        print(a>>b)
    elif x=="lst":
        print(a<<b)
def calc_3(x,a):
    if x=="sqr":
        print(a**2)
    elif x=="cub":
        print(a**3)

print("for addition enter 'add'\n for subtraction enter 'sub'\n for multiplication enter 'mul'\n for division 'div'\n for modulus 'mod'\n for Exponentiation 'exp'\n for Floor division 'flo'\n for right shift 'rst'\n for left shift 'lst'\n for square 'sqr'\n for cube 'cub'")
y=input("enter the operation:")
if y in ["add","sub","mul","div","mod","exp","flo"]:
    c=float(input("enter the first no:"))
    d=float(input("enter the second number:"))
    calc_1(y,c,d)
if y in ["rst","lst"]:
    c= int(input("enter the no:"))
    d = int(input("enter how many bits you want to shift:"))
    calc_2(y,c,d)
if y in ["sqr", "cub"]:
    c = float(input("enter the no:"))
    calc_3(y,c)
if y not in["add","sub","mul","div","mod","exp","flo","rst","lst","sqr", "cub"] :
    print("invalid input")
