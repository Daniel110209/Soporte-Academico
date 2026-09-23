LONGITUD_MINIMA_CODIGO = 6


def mostrar_menu():
    # Menu principal
    # Esta funcion no recibe parametros ni devuelve ningun valor
    print(" SOPORTE ACADEMICO ")
    print("1. Registrar nueva solicitud")
    print("2. Salir")
   


def validar_texto_obligatorio(texto, longitud_minima):
    # Requerimiento 6: funcion CON retorno que valida un texto obligatorio
    # Se usa para validar nombre, descripcion y codigo con distinta longitud minima
    texto = texto.strip()
    if len(texto) >= longitud_minima:
        return True
    else:
        return False


def validar_codigo_estudiante(codigo):
    # Requerimiento 2: valida codigo de estudiante (no vacio, longitud minima)
    # Un codigo valido debe tener minimo 6 caracteres, ej: EST2026
    return validar_texto_obligatorio(codigo, LONGITUD_MINIMA_CODIGO)


def validar_tipo_consulta(tipo):
    # Requerimiento 3: valida que el tipo de consulta este en la lista permitida
    # Tipos permitidos: matricula, pagos, constancia, plataforma, otro
    tipo = tipo.strip().lower()
    if tipo == "matricula" or tipo == "pagos" or tipo == "constancia" or tipo == "plataforma" or tipo == "otro":
        return True
    else:
        return False


def calcular_prioridad(tipo_consulta):
    # Requerimiento 5: funcion con retorno
    # Plataforma y pagos son urgentes (Alta), otro es Baja, el resto es Media
    tipo = tipo_consulta.strip().lower()
    prioridad = "Media"  # variable local (Requerimiento 9)
    if tipo == "plataforma" or tipo == "pagos":
        prioridad = "Alta"
    elif tipo == "otro":
        prioridad = "Baja"
    return prioridad


def mostrar_resumen(codigo, nombre, tipo_consulta, descripcion, prioridad):
    # Requerimiento 7: funcion sin retorno que muestra el resumen de la solicitud
    # Recibe los datos ya validados y solo los imprime en pantalla
    print("--- Resumen de solicitud ---")
    print("Codigo: " + codigo)
    print("Nombre: " + nombre)
    print("Tipo de consulta: " + tipo_consulta)
    print("Descripcion: " + descripcion)
    print("Prioridad asignada: " + prioridad)


def main():
    # Requerimiento 10: listas del programa principal para guardar hasta 3 solicitudes
    lista_codigos = []
    lista_nombres = []
    lista_tipos = []
    lista_prioridades = []

    mostrar_menu()

    # Requerimiento 11: 5 pruebas con datos fijos, antes de pedir datos por teclado
    print("")
    print("PRUEBA 1 (datos validos):")
    codigo = "N00534090"
    nombre = "Ana Torres"
    tipo_consulta = "matricula"
    descripcion = "Consulta por horario"
    if validar_codigo_estudiante(codigo) and validar_tipo_consulta(tipo_consulta):
        prioridad = calcular_prioridad(tipo_consulta)
        mostrar_resumen(codigo, nombre, tipo_consulta, descripcion, prioridad)
    else:
        print("Datos invalidos")

    print("")
    print("PRUEBA 2 (codigo vacio):")
    codigo_prueba = ""
    if validar_codigo_estudiante(codigo_prueba):
        print("Codigo valido")
    else:
        print("Codigo invalido, no se puede registrar")

    print("")
    print("PRUEBA 3 (tipo de consulta incorrecto):")
    tipo_prueba = "biblioteca"
    if validar_tipo_consulta(tipo_prueba):
        print("Tipo valido")
    else:
        print("Tipo de consulta no reconocido")

    print("")
    print("PRUEBA 4 (prioridad alta):")
    print(calcular_prioridad("plataforma"))

    print("")
    print("PRUEBA 5 (prioridad baja):")
    print(calcular_prioridad("otro"))

    # enviando los datos por parametros y usando variables locales dentro de cada funcion
    # Requerimiento 8: codigo, nombre, tipo_consulta y descripcion se pasan a las funciones de validacion, no se usan variables globales
    print("")
    contador = 0
    while contador < 3:
        print("Registrando solicitud numero " + str(contador + 1))
        codigo = input("Codigo de estudiante: ")
        nombre = input("Nombre: ")
        tipo_consulta = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ")
        descripcion = input("Descripcion breve: ")

        codigo_valido = validar_codigo_estudiante(codigo)
        tipo_valido = validar_tipo_consulta(tipo_consulta)
        nombre_valido = validar_texto_obligatorio(nombre, 3)
        descripcion_valida = validar_texto_obligatorio(descripcion, 5)

        if codigo_valido and tipo_valido and nombre_valido and descripcion_valida:
            prioridad = calcular_prioridad(tipo_consulta)
            lista_codigos.append(codigo)
            lista_nombres.append(nombre)
            lista_tipos.append(tipo_consulta)
            lista_prioridades.append(prioridad)
            mostrar_resumen(codigo, nombre, tipo_consulta, descripcion, prioridad)
            contador = contador + 1
        else:
            print("No se pudo registrar la solicitud:")
            if not codigo_valido:
                print("- El codigo esta vacio o es muy corto")
            if not tipo_valido:
                print("- El tipo de consulta no es valido")
            if not nombre_valido:
                print("- El nombre es muy corto")
            if not descripcion_valida:
                print("- La descripcion es muy corta")

    print("")
    print("Se registraron " + str(contador) + " solicitudes en esta ejecucion")


main()