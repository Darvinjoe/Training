print("""        INFORMATION
         Fahrenheit	°F = 1.8°C + 32°
         Celsius	°C =5/9(°F-32°)
         Kelvin      K = °C + 273°""")
input_type=input("enter the input type(example:\"cel\",\"kel\",\"fah\"):")

if input_type in ["kel","cel","fah"]:
    if input_type=="kel":
        k=int(input("enter the value:"))
        c=k-273
        f=1.8*c+32
        print(f"Celsius   :{c}")
        print(f"Fahrenheit:{f}")
    if input_type=="cel":
        c=int(input("enter the value:"))
        f=1.8*c+32
        k=c+273
        print(f"kelvin    :{k}")
        print(f"Fahrenheit:{f}")
    if input_type=="fah":
        f=int(input("enter the value:"))
        c=(5/9)*(f-32)
        k=c+273
        print(f"Celsius:{c}")
        print(f"kelvin :{k}")

else:
    print("invalid input")
