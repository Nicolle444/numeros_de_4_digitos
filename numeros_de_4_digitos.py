# verificar si un numero es positivo y de 4 digitos

print("-----------------------------------")
print("------4 digitos y positivo---------")
print("-----------------------------------")

# input

a = int(input("Digite el numero: "))


# procesing and output

if a > 0 and a >= 1000 and a <= 9999:
    print("El numero tiene cuatro digitos y es positivo")

else:
    print("El numero no cumple con las condiciones")

