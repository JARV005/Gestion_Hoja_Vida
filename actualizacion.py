"""Actualizar información registrada, como:
• Añadir nueva experiencia o formación
• Editar Datos Personales o de contacto
• Cambiar o agregar habilidades y referencias"""

"""Estructuras de datos obligatorias:
• diccionarios (para representar cada hoja de vida)
• listas (para almacenar múltiples experiencias, estudios, etc.)
• sets (para validar datos únicos como correos, habilidades globales)
• tuplas (para datos mod no cambian, como num_idumento + fecha nacimiento)"""
import datetime


# Estructura base
# {Identificación : {Estudios: [[...]], Experiencia lab: [[...]], datos únicos: (correos, habilidades globales..), datos pers: (fecha nacimiento)}}
cvs = {'1020' : {
    "Datos Personales" : {"nombre", "telefono", "direccion", "email", ("fecha de nacimiento")},
    "Estudios" : [["institucion", "titulo", "años"]],
    "Experiencia" : [["empresa", "cargo", "funciones", "duracion"]],
    "Referencias" : [["nombrer", "relacion", "telefono"]],
    "Certificaciones" : [["Certificaciones"]]},
       '6256': {
    'Datos Personales': {'Nombre': 'strjsj', 'Telefono': 'ssrtjsyj', 'Dirección': 'sartjshyj', 'Correo Electronico': 'athjsjsy', 'Fecha de nacimiento': datetime.date(1998, 4, 24), 'Edad': 27},
    'Estudios': [['zrtujstykj', 'dtydty', '68478'], ['djdhjkd', 'hjdghjdh', '45756']],
    'Experiencia': [['stjhyj', 'shjdhj', 'djdthj', '658478'], ['shsrjsj', 'sgjsj', 'sjsyj', '57567']],
    'Referencias': [['ahfgj', 'sgjshjk', '658478'], ['sghsgjsj', 'srjsyhj', '67658']],
    'Certificaciones': [['trasjstyj'], ['sghsgj']],
    'Habilidades': {'ahshgj', 'ghgjhj'}}}

# (num_id,name,contact,addres,email,birthdate,institute,title,year,company,position,functions,period,ref,relationship,phone,certificates)

def act_datos():
    id = str(input("Ingrese el número de num_idumento: "))
    if id not in cvs:
        print("Ese numero de documento no se encuentra registrado")
    else:
        print("\nSeleccione la acción que desea realizar:")
        print("1. Añadir dato\n2. Modificar dato\n3. Regresar")
        opc = int(input(">> "))
        while True:
            match opc:
                case 1:
                    while True:
                        print("\nSeleccione el dato que desea añadir: ")
                        op1 = int(input("1. Estudios\n2. Experiencia\n3. Habilidades\n4. Certificaciones\n5. Regresar"))
                        match op1:
                            case 1:
                                while True:
                                    cont = True
                                    title = input("Ingrese el título que desea añadir: ")
                                    for dato in cvs[id]["Estudios"]:
                                        if title in dato:
                                            print("El estudio ingresado ya existe")
                                            cont = False
                                            break
                                    if not cont:
                                        break
                                    else:
                                        institute = input("Nombre de la institución: ")
                                        year = input("Periodo de estudios (ej. 2020-2024): ")
                                        estudios =[institute,title,year]
                                        cvs[id]["Estudios"].append(estudios)
                                        break
                            case 2:
                                while True:
                                    cont = True
                                    position = input("Ingrese el cargo en la empresa: ")
                                    for dato in cvs[id]["Experiencia"]:
                                        if position in dato:
                                            print("El cargo ingresado ya existe")
                                            cont = False
                                            break
                                    if not cont:
                                        break
                                    else:
                                        company = input("nombre de la empresa: ")
                                        functions = input("funciones que desempeñaba: ")
                                        period = input("periodo en el que trabajó: ")
                                        experiencia = [company, position, functions, period]
                                        cvs[id]["Experiencia"].append(experiencia)
                                        break
                            case 3:
                                while True:
                                    hab = input("Ingrese la habilidad que desea añadir: ")
                                    if hab in cvs[id]["Habilidades"]:
                                        print("La habilidad ingresada ya existe")
                                        break
                                    else:
                                        cvs[id]["Habilidades"].add(hab)
                                        break
                            case 4:
                                while True:
                                    cont = True
                                    name_certificate = input("Nombre del certificado: ")
                                    for dato in cvs[id]["Certificaciones"]:
                                        if name_certificate in dato:
                                            print("La certificación ingresada ya existe")
                                            cont = False
                                            break
                                    if not cont:
                                        break
                                    else:
                                        institute_c = input("Institucion")
                                        name_certificate = input("Nombre del certificado: ")
                                        year_certificate = input("Añoi de realización: ")
                                        certificates = [institute_c,name_certificate,year_certificate]
                                        cvs[id]["Certificaciones"].append(certificates)
                                        break
                            case 5:
                                break
                            case _:
                                print("Debe elegir una de las opciones")
                case 2:
                    while True:
                        print("\n¿Qué dato desea cambiar?")
                        print("1. Teléfono\n2. Dirección\n3. Correo Electronico\n4. Regresar")
                        opd = int(input(">> "))
                        match opd:
                            case 1:
                                contact = input("Ingrese el nuevo número de telefono: ")
                                cvs[id]["Datos Personales"]["Telefono"]= contact
                            case 2:
                                addres = input("Ingrese la nueva dirección: ")
                                cvs[id]["Datos Personales"]["Dirección"]= addres
                            case 3:
                                email = input("Ingrese el nuevo correo electrónico: ")
                                cvs[id]["Datos Personales"]["Correo Electronico"]= email
                            case 4:
                                break
                            case _:
                                print("Error: Debe seleccinar una de las opciones")
                case 3:
                    break
                case _:
                    print("Error: Debe seleccinar una de las opciones")
