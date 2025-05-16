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

def add_list(num_id, site, mod):
    cvs[num_id][site].append(mod)

def add_set(num_id, site, mod):
    cvs[num_id][site].add(mod)


def act_datos():
    num_id = str(input("Ingrese el número de num_idumento: "))
    if num_id not in cvs:
        print("Ese numero de documento no se encuentra registrado")
    else:
        print("\nSeleccione la acción que desea realizar:")
        print("1. Añadir dato\n2. Modificar dato")
        opc = int(input(">> "))
        while True:
            if opc == 1:
                print("\nSeleccione el dato que desea añadir: ")
                op1 = int(input("1. Estudios\n2. Experiencia\n3. Habilidades\n4. Certificaciones\n5. Regresar"))
                match op1:
                    case 1:
                        while True:
                            ed = input("Ingrese el estudio que desea añadir: ")
                            for dato in cvs[num_id]["Estudios"]:
                                if ed in dato:
                                    print("El estudio ingresado ya existe")
                                    cont = False
                                    break
                            if not cont:
                                break
                            else:
                                fecha = input("Ingrese el año de inicio finalización en el siguiente formato (AAAA-AAAA): ")
                                nueva_ed = [ed, fecha]
                                cvs[num_id]["Estudios"].append(nueva_ed)
                                break
                    case 2:
                        while True:
                            exp = input("Ingrese el cargo que desea añadir: ")
                            for dato in cvs[num_id]["Experiencia"]:
                                if exp in dato:
                                    print("El cargo ingresado ya existe")
                                    cont = False
                                    break
                            if not cont:
                                break
                            else:
                                fecha = input("Ingrese la fecha de inicio y fin en el siguiente formato (AAA-MM): ")
                                nueva_exp = [exp, fecha]
                                cvs[num_id]["Experiencia"].append(nueva_exp)
                                break
                    case 3:
                        while True:
                            hab = input("Ingrese la habilidad que desea añadir: ")
                            if hab in cvs[num_id]["Habilidades"]:
                                print("La habilidad ingresada ya existe")
                                break
                            cvs[num_id]["Habilidades"].add(hab)
                            break
                    case 4:
                        while True:
                            cont = True
                            cert = input("Ingrese la nueva certificación: ")
                            for dato in cvs[num_id]["Certificaciones"]:
                                if cert in dato:
                                    print("La certificación ingresada ya existe")
                                    cont = False
                                    break
                            if not cont:
                                break
                            else:
                                cvs[num_id]["Certificaciones"].append(cert)
                                break
                    case 5:
                        break
                    case _:
                        print("Debe elegir una de las opciones")
            if opc == 2:
                print("\n¿Qué dato desea cambiar?")
                print("1. Teléfono\n2. Dirección\n3. Correo")
                opd = int(input(">> "))
                match opd:
                    case 1:
                        contact = input("Ingrese el nuevo número de telefono: ")
                        cvs[num_id]["Datos Personales"]["Telefono"]= contact
                    case 2:
                        contact = input("Ingrese la nueva dirección: ")
                        cvs[num_id]["Datos Personales"]["Dirección"]= contact
                    case 3:
                        contact = input("Ingrese el nuevo correo electrónico: ")
                        cvs[num_id]["Datos Personales"]["Correo"]= contact
                    case _:
                        print("MAL")
            


act_datos()