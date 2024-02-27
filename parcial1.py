#inicio de parcial, realizar un proyecto en el cual salga un menú y pida ingresar carné, nombre y nota del estudiante.
#He definido una función en la cual se puede modificar a nota del estudiante con solo meter el carné.
#También definí otra función donde permite ver la nota del estudiante, este progrma también cuenta con ciclos y una lista de diccionario.
def agregar_estudiante(notas):
    # Esta función es definida para agregar una persona con su nota
    carné = int(input("Ingrese el carné: "))
    nombre = input("Ingrese el nombre: ")
    nota = float(input("Ingrese la nota: "))
    
    persona = {"carnet": carné, "nombre": nombre, "nota": nota}
    notas.append(persona)
    print("estudiante y carné agregados correctamrente.")

def modificar_nota(notas):
    # Esta función nos sirve para modificar las notas de un estudiante 
    carné = int(input("Ingrese el carné del estudiante cuya nota desea modificar: "))
    
    for persona in notas:
        if persona["carnet"] == carné:
            nueva_nota = float(input("Ingrese la nueva nota: "))
            persona["nota"] = nueva_nota
            print("Nota modificada correctamente.")
            return
    
    print("No se encontró ningun estudiante con el carné proporcionado.")

def consultar_nota(notas):
    # Esta es de utilidad cuando necesitamos saber cual es la nota de algun estudiante 
    carné = int(input("Ingrese el carné del estudiante cuya nota desea consultar: "))
    
    for persona in notas:
        if persona["carnet"] == carné:
            print(f"Nota de {persona['nombre']}: {persona['nota']}")
            return
    
    print("No se encontró ninguna persona con el carné proporcionado.")

def mostrar_menu():
    # Defini una función aqui para así poder mostrar el menú
    print("\nMenú:")
    print("a. Agregar persona con nota")
    print("b. Modificar nota de una persona")
    print("c. Consultar nota de una persona")
    print("q. Salir")

# Esta es una lista de diccionarios para almacenar las notas del curso de cada estudiante
notas_curso = []

# Ciclo principal del programa
while True:
    # Mostrar el menú
    mostrar_menu()
    
    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Tomar acciones según la opción seleccionada
    if opcion == 'a':
        agregar_estudiante(notas_curso)
    elif opcion == 'b':
        modificar_nota(notas_curso)
    elif opcion == 'c':
        consultar_nota(notas_curso)
    elif opcion == 'q':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción invalida. Por favor, selecciona una opción válida.")
