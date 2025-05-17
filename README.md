# GESTION HOJA DE VIDA

**Integrantes: John Brahian Montoya (Van Rossum)** 
             - **Johan Alexander Rivera (Van Rossum)**
             - **Omar Bedoya Gallego (Ritchie)**

## Descripción
El presente programa permite gestionar hojas de vida, registrando los datos personales, formación educativa, experiencia laboral y habilidades de una o más personas. Ademaś permite añadir o actualizar nuevos datos, consultar hojas de vida referente a la información de cada persona. De la misma manera permite realizar reportes para filtrar las hojas de vida en base a una condición específica (años de experiencia, certficaciones, etc.)

## Instrucciones

Cuando se inicia el programa encontramos el siguiente menú principal:

|Menú principal                 |
|-------------------------------|
|1. Registrar nueva hoja de vida|
|2. Buscar hoja de vida         |
|3. Actualizar hoja de vida     |
|4. Generar reportes            |
|5. Exportar hojas de vida      |
|6. Salir                       |

Para acceder a una de las opciones se debe ingresar el número correspondiente (de ingresar un número diferente se recibe un error y se vuelve a solicitar la opción deseada)

**1. Registrar nueva hoja de vida**
Cuando se ingresa en esta opción se le solicita al usuario toda la información necesaria para el diligenciamiento de la hoja de vida.
Datos como:
-Información personal (nombre, identificación, teléfono, fecha de nacimiento, etc.)
-Educación (Título, institución, fecha)
-Experiencia laboral(Cargo, empresa, funciones, fechas)
-Certificaciones
-Habilidades

**2. Buscar hoja de vida**
En esta opción el usuario puede buscar una hoja de vida utilizando tres datos (Nombre, identificación o correo)
Cuando se encuentra el registro correspondiente se muestra toda la información respectiva de la hoja de vida.
En caso de no encontrarse el registro se muestra la respectiva adevertencia anunciandolo. 

**3. Actualizar hoja de vida**
Cuando se desee añadir o modificar alguno de los datos registrados anteriormente, esta opción le permite hacerlo-
Información personal como teléfono, dirección o correo electrónico puede ser modificada.
Además se pueden añadir datos como experiencia laboral, educación, certificaciones y habilidades.

**4. Generar reportes**
Esta opción le permite al usario acceder a reportes utilizando filtros como años de experiencia, certificaciones o formaciones especificas.

**5. Exportar hojas de vida**
Esta opción le muestra al usario hojas de vida de acuerdo al formato seleccionado (.json o .txt).

**6. Salir**
Termina la interacción con el usuario.


## Librerias usadas
Se utilizaro las siguientes librerias:
- json, se importa: import json
- datetime, se importa: from datetime import datetime
- tabulate, se importa: from tabulate import tabulate
- collections, se importa: from collections import Counter


## Ejemplos de entradas

Funcion num_int: input = "Número de documento: " = "1234567890" Output: "Documento" : 1234567890

Funcion act_datos: input = "Ingrese el titulo: " = "Bachiller" Output: "El titulo ingresado ya existe."

Funcion act_datos: input = "Ingrese el nuevo correo electronico: " = "ejemple@ejemplo.com" Output: "Correo electronico" : "ejemple@ejemplo.com"


## Tablero de trabajo

![Captura desde 2025-05-16 21-05-18](https://github.com/user-attachments/assets/c4f144ce-cfa1-427d-a46a-58ebd8b1dcc4)





