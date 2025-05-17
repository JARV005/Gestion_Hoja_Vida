#Diccionario para almacenar datos
cvs = {"Documento" : {"Datos Personales": {"Nombre" : "", "Telefono" : "", "Direccion" : "", "Correo Electronico" : "", "Fecha de nacimiento" : (), "Edad" : ""}, 
       "Estudios" : [["institucion", "titulo", "años"]], 
       "Experiencia" : [["empresa", "cargo", "funciones", "duracion"]], 
       "Referencias" : [["nombrer", "relacion", "telefono"]], 
       "Certificaciones" : [["certificado"]],
       "Habilidades" : {"comunicacion"}}}

import datetime

def num_int(message):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            print("Debe ingresar solo números.")

def add_cv():
    print("DATOS PERSONALES")
    id = num_int("Número de documento: ")
    if id in cvs:
        print("El documento de identidad ya está relacionado a una hoja de vida existente.")
    else:
        cvs[id] = {"Datos Personales" : {}, "Estudios" : [], "Experiencia" : [], "Referencias" : [], "Certificaciones" : [], "Habilidades" : set(),}
        #Datos personales
        name = input("Nombre completo: ")
        contact = num_int("Número de contacto: ")
        addres = input("Dirección: ")
        email = input("Correo electrónico: ")
        print("Fecha de nacimiento")
        yeardate = num_int("Año: ")
        month = num_int("Mes: ")
        day = num_int("Día: ")
        birthdate = datetime.date(yeardate,month,day)
        actu = datetime.date.today().year
        age = actu - yeardate
        datospersonales = {"Nombre" : name, "Telefono" : contact, "Dirección" : addres, "Correo Electronico" : email, "Fecha de nacimiento" : birthdate, "Edad" : age}
        cvs[id]["Datos Personales"] = datospersonales        


    #Formacion academica
    print("FORMACION ACADEMICA")
    while True:
        institute = input("Nombre de la institución: ")
        title = input("Título adquirido: ")
        year = input("Periodo de estudios (ej. 2020-2024): ")
        estudios =[institute,title,year]
        cvs[id]["Estudios"].append(estudios)

        more = input("Desea agregar otro estudio? (s/n)").lower()
        if more != "s":
            break


    # Experiencia laboral
    print("EXPERIENCIA LABORAL")
    while True:
        company = input("Nombre de la empresa: ")
        position = input("Cargo en la empresa: ")
        functions = input("Funciones que desempeñaba: ")
        period2 = num_int("Año de inicio: ")
        period1 = num_int("Año de finalización: ")
        period = f"{period2} - {period1}"
        experiencia = [company, position, functions, period]
        cvs[id]["Experiencia"].append(experiencia)

        more = input("Desea ingresar otra experiencia laboral? (s/n): ").lower()
        if more != "s":
            break


    #Referencias personales
    print("REFERENCIAS PERSONALES")
    while True:
        ref = input("Referencia personal: ")
        relationship = input("Relacion: ")
        phone = num_int("Numero de telefono: ")
        referencias = [ref, relationship, phone]
        cvs[id]["Referencias"].append(referencias)

        more = input("Desea agregar otra referencia? (s/n): ").lower()
        if more != "s":
            break
        

    #Hablidades y certificaciones
    print("CERTIFICADOS")
    while True:
        institute_c = input("Institucion")
        name_certificate = input("Nombre del certificado: ")
        year_certificate = num_int("Año de realización: ")
        certificates = [institute_c,name_certificate,year_certificate]
        cvs[id]["Certificaciones"].append(certificates)

        more = input("Desea agregar otro certificado? (s/n): ").lower()
        if more != "s":
            break
    

    print("HABILIDADES")
    while True:
        habilities = input("Habilidad: ")
        cvs[id]["Habilidades"].add(habilities)

        more = input("Desea agregar otra habilidad? (s/n): ").lower()
        if more != "s":
            break
        
def filter_cv():
    print("Ingrese la opción por la que desea filtrar la información\n1. Experiencia\n2. Formación\n3. Habilidades")
    opt = num_int("")
    match opt:
        case 1:
            flag = False
            search_exp = num_int("Ingrese los años de experiencia por los que desea filtrar: ")
            for id_cv, datos in cvs.items():
                for experience in datos['Experiencia']:
                    years = experience[3].split("-")
                    exp = int(years[1]) - int(years[0])
                    if exp == search_exp:
                        print(cvs[id_cv]) ## Aca va la hoja organizada
                        flag = True
            if not flag:
                print("Ninguna de las hojas de vida cumple con el filtro")

        case 2:
            flag = False
            search_ed = str(input("Ingrese el título que desea buscar: "))
            for id_cv, datos in cvs.items():
                for study in datos["Estudios"]:
                    if search_ed in study:
                        print(cvs[id_cv]) ## Aca va la hoja organizada
                        flag = True
            if not flag:
                print("Ninguna de las hojas de vida cumple con el filtro")
        case 3:
            flag = False
            search_sk = str(input("Ingrese la habilidad que desea buscar: "))
            for id_cv, datos in cvs.items():
                for skill in datos["Habilidades"]:
                    if search_sk in skill:
                        print(cvs[id_cv]) ## Aca va la hoja organizada
                        flag = True
            if not flag:
                print("Ninguna de las hojas de vida cumple con el filtro")









































































































































































"""Datos personales (nombre, documento, contacto, dirección, correo, fecha
de nacimiento)
• Formación académica (institución, título, años)
• Experiencia profesional (empresa, cargo, funciones, duración)
• Referencias personales y/o laborales (nombre, relación, teléfono)
• Habilidades o certificaciones adicionales

Diccionarios (para representar cada hoja de vida)
• listas (para almacenar múltiples experiencias, estudios, etc.)
• sets (para validar datos únicos como correos, habilidades globales)
• tuplas (para datos que no cambian, como documento + fecha nacimiento"""
