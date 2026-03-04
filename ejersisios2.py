estudiante = True
profesor = True
visitante = False

if estudiante == True or profesor == True:
    print("acceso permitido: vienvenido 🥳")
    print("puedes entar al edificio")

elif visitante == True:
    print("bienvendio visitante 👌")

else:
    print("acceso denegado 🙋‍♂️")

print("estado del usuario")
print(f"estudiant: {estudiante}")
print(f"estudiant: {profesor}")
print(f"estudiant: {visitante}")
