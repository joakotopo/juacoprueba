
def rut_valido(rut):
    if len(rut) not in (8,9):
        return
    if rut[-1].lower() == "k":
        return rut[:-1].isdigit()
    return rut.isdigit()

def ingresar_alumno(estudiantes):
    nombre = input("ingrese el nombre del alumno: ")
    rut = input("ingrese el numero de rut del alumno (sin . ni -): ")
    while not rut_valido(rut):
        print("rut ingresado no valido")
        print("")
        rut = ("ingrese el rut del alumno (sin . ni -): ")
    
    print("")
    print("ingrese las 4 notas del alumno")
    nota1 = int(input("ingrese la primera nota: "))
    nota2 = int(input("ingrese la segunda nota: "))
    nota3 = int(input("ingrese la tercera nota: "))
    nota4 = int(input("ingrese la cuarta nota: "))
    
    suma = nota1 + nota2 + nota3 + nota4 
    promedio = suma /4
    if promedio >= 40:
        final = "Aprobado"
    elif promedio < 40:
        final = "Reprobado"
    alumnos =[nombre,rut,nota1,nota2,nota3,nota4,promedio,final]
    estudiantes.append(alumnos)
    
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("aun no hay estudiantes registrados")

    if estudiantes:  
    
      for alumnos in estudiantes:
       print("lista alumnos")
       print("")
       print(f"nombre: {estudiantes[0]}, rut: {estudiantes[1]}, nota1: {estudiantes[2]}, nota2: {estudiantes[3]}, nota3: {estudiantes[4]}, nota4: {estudiantes[5]}, promedio: {estudiantes[6]}, resultado: {estudiantes[7]}")


def buscar_estudiante(estudiantes):
    if not estudiantes:
        print("aun no hay estudiantes: ")
    
    if estudiantes:
        buscado = input("ingrese el rut del estudiante que busca: ")
        encontrado = False
        for alumnos in estudiantes:
            if alumnos[1].lower() == buscado:
                print("")
                print("alumno encontrado")
                print("")
                print(f"nombre: {alumnos[0]}, rut: {alumnos[1]}, nota1: {alumnos[2]}, nota2: {alumnos[3]}, nota3: {alumnos[4]}, nota4: {alumnos[5]}, promedio: {alumnos[6]}, resultado: {alumnos[7]}")
                encontrado = True
            if not encontrado:
                print("el alumno no se a encontrado")
            



import csv
def exportar_cvs(estudiantes):
    with open("nuevo_archivo.csv","w", newline="") as archivo_csv:
        for alumnos in estudiantes:
         escritor_csv = csv.writer(archivo_csv)
         escritor_csv.writerow(["nombre","rut","nota1","nota2","nota3","nota4","promedio","resultado"])
         escritor_csv.writerow(f"{alumnos[0]} {alumnos[1]} {alumnos[2]} {alumnos[3]} {alumnos[4]} {alumnos[5]} {alumnos[6]} {alumnos[7]}")













lista = []




while True:
    print("")
    print("menu colegio")
    print("")
    print("1: ingresar alumno")
    print("2: mostrar todos los estudiantes")
    print("3: buscar estudiante")
    print("4: exportar a cvs")
    print("5: salir")
    opc = int(input("ingrese una opcion: "))

    if opc == 1:
        ingresar_alumno(lista)
    
    elif opc == 2:
        mostrar_estudiantes(lista)
    
    elif opc == 3:
        buscar_estudiante(lista)
    
    elif opc == 4:
        exportar_cvs(lista)
    
    elif opc == 5:
        print("hasta la proximaaaa")
        break
    else: 
        print("opcion invalida")
     