#app para pasar una temperatura indicada en Celsius a Fahrenheit o viceversa 

temperatura = float(input("Ingrese la temperatura: "))
escala = input("Es Fahrenheit(F) o Celsius(C)?:").upper()

if escala == "F" or escala == "C":
    if escala == "C":
        temperaturaF = (temperatura * (9/5)) + 32
        print("la temperatura en Fahrenheit es:", temperaturaF)
    else:
        temperaturaC = (temperatura - 32) * (5/9)
        print("la temperatura en Celsius es:", temperaturaC)
else:
    print("escala no valida")