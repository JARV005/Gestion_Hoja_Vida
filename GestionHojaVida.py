#Diccionario para almacenar datos
cvs = {"Documento" : {"Datos Personales": {"Nombre" : "", "Telefono" : "", "Direccion" : "", "Correo Electronico" : "", "Fecha de nacimiento" : (), "Edad" : ""}, 
       "Estudios" : [["institucion", "titulo", "años"]], 
       "Experiencia" : [["empresa", "cargo", "funciones", "duracion"]], 
       "Referencias" : [["nombrer", "relacion", "telefono"]], 
       "Certificaciones" : [["certificado"]],
       "Habilidades" : {"comunicacion"}}}
import datetime

#{Identificación : {Educación: [[...]], Experiencia lab: [[...]], datos únicos: {correos, habilidades globales..}, datos pers: (fecha nacimiento)}}
#Función para registrar hojas de vida
def add_cv():
    print("DATOS PERSONALES")
    id = input("Número de documento: ")
    if id in cvs:
        print("El documento de identidad ya está relacionado a una hoja de vida existente.")
    else:
        cvs[id] = {"Datos Personales" : {}, "Estudios" : [], "Experiencia" : [], "Referencias" : [], "Certificaciones" : [], "Habilidades" : set(),}
        #Datos personales
        name = input("Nombre completo: ")
        contact = input("Número de contacto: ")
        addres = input("Dirección: ")
        email = input("Correo electrónico: ")
        print("Fecha de nacimiento")
        yeardate = int(input("Año: "))
        month = int(input("Mes: "))
        day = int(input("Día: "))
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
        company = input("nombre de la empresa: ")
        position = input("cargo en la empresa: ")
        functions = input("funciones que desempeñaba: ")
        period = input("periodo en el que trabajó: ")
        experiencia = [company, position, functions, period]
        cvs[id]["Experiencia"].append(experiencia)

        more = input("Desea ingresar otra experiencia laboral? (s/n): ").lower()
        if more != "s":
            break


    #Referencias personales
    print("REFERENCIAS PERSONALES")
    while True:
        ref = input("nombre de su referencia personal: ")
        relationship = input("relacion tiene: ")
        phone = input("numero de telefono de su referencia personal: ")
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
        year_certificate = input("Añoi de realización: ")
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
        
add_cv()



















































































































































































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