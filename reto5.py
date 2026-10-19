#Construye obtener_estadisticas() para devolver la cantidad de pendientes, 
#atenciones actualmente en el historial y total de solicitudes únicas. Además, 
# evita registrar una nueva solicitud con el mismo cliente y asunto cuando ya 
# existe una pendiente equivalente, ignorando mayúsculas y espacios en los extremos.

#Prueba: registrar dos veces «Ana / Wi-Fi» y « ana / wi-fi » solo debe añadir un pendiente.
#Ahora seria marcelo no tiene agua en vez de ana wifi
cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\nPendientes:")
    for solicitud in cola_pendientes:
        print(solicitud)
    print("\nHistorial:")
    for solicitud in pila_historial:
        print(solicitud)
    print()

def registrar_solicitud(cliente, asunto):
    global siguiente_id

    cliente_limpio = cliente.strip()
    asunto_limpio = asunto.strip()

    if not cliente_limpio or not asunto_limpio:
        return None

    for solicitud in cola_pendientes:
        if solicitud["cliente"].lower() == cliente_limpio.lower():
            if solicitud["asunto"].lower() == asunto_limpio.lower():
                return None

    solicitud = {
        "id": siguiente_id,
        "cliente": cliente_limpio,
        "asunto": asunto_limpio,
        "estado": "pendiente"
    }

    cola_pendientes.append(solicitud)
    siguiente_id += 1
    return solicitud

registrar_solicitud("Marcelo", "No tiene agua")
registrar_solicitud("Miguel", "Se le inundo la casa")
registrar_solicitud("David", "Le robaron en el bus")
mostrar_estado()

def atender_siguiente():
    if not cola_pendientes:
        return None
    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud

print("Atendida:", atender_siguiente())
mostrar_estado()

def deshacer_ultima_atencion():
    if not pila_historial:
        return None
    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud

print("Restaurada:", deshacer_ultima_atencion())
mostrar_estado()

def consultar_siguiente():
    if not cola_pendientes:
        return None
    return cola_pendientes[0]

def buscar_solicitud(id_solicitado):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitado:
            return solicitud, "pendientes"
    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitado:
            return solicitud, "historial"
    return None

def cancelar_pendiente(id_solicitado):
    indice = 0
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitado:
            solicitud_cancelada = cola_pendientes.pop(indice)
            return solicitud_cancelada
        indice += 1
    return None

def deshacer_varias(cantidad):
    if cantidad <= 0:
        return 0
    recuperadas = 0
    while recuperadas < cantidad:
        resultado = deshacer_ultima_atencion()
        if resultado is None:
            break
        recuperadas += 1
    return recuperadas

def obtener_estadisticas():
    pendientes = len(cola_pendientes)
    atendidas = len(pila_historial)

    total_unicas = pendientes + atendidas

    return pendientes, atendidas, total_unicas

def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Consultar siguiente pendiente")
        print("6. Buscar solicitud por ID")
        print("7. Cancelar solicitud pendiente")
        print("8. Deshacer varias atenciones")
        print("9. Mostrar estadísticas")
        print("10. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos invalidos")
        elif opcion == "2":
            print("Atendida:", atender_siguiente())
        elif opcion == "3":
            print("Restaurada:", deshacer_ultima_atencion())
        elif opcion == "4":
            mostrar_estado()
        elif opcion == "5":
            print("El siguiente pendiente es:", consultar_siguiente())
        elif opcion == "6":
            texto_id = input("Id de la solicitud: ").strip()

            if texto_id.isdigit():
                id_solicitud = int(texto_id)
                resultado = buscar_solicitud(id_solicitud)

                if resultado is None:
                    print("No se encontró la solicitud.")
                else:
                    solicitud, ubicacion = resultado
                    print("Solicitud encontrada:", solicitud)
                    print("Ubicación:", ubicacion)
            else:
                print("Debes digitar un número valido.")
        elif opcion == "7":
            texto_id = input("ID de la solicitud a cancelar: ").strip()

            if texto_id.isdigit():
                id_solicitud = int(texto_id)
                resultado = cancelar_pendiente(id_solicitud)

                if resultado is None:
                    print("No se puede cancelar: la solicitud no está pendiente.")
                else:
                    print("Solicitud cancelada:", resultado)
            else:
                print("Debes digitar un número válido.")
        elif opcion == "8":
            texto_cantidad = input("¿Cuántas atenciones deseas deshacer? ")
            if texto_cantidad.isdigit():
                cantidad = int(texto_cantidad)

                if cantidad > 0:
                    recuperadas = deshacer_varias(cantidad)
                    print("Se recuperaron", recuperadas, "solicitud(es).")
                else:
                    print("Debes digitar un número mayor que cero.")
            else:
                print("Debes digitar un número entero positivo.")
        elif opcion == "9":
            pendientes, atendidas, total_unicas = obtener_estadisticas()
            print("Pendientes:", pendientes)
            print("Atenciones en historial:", atendidas)
            print("Total de solicitudes únicas:", total_unicas)
        elif opcion == "10":
            break
        else:
            print("Opción inválida")
                
if __name__ == "__main__":
    ejecutar_menu()