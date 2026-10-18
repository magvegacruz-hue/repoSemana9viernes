#Implementa deshacer_varias(cantidad) reutilizando deshacer_ultima_atencion(). Valida que la 
#cantidad sea un entero positivo. Si hay menos acciones disponibles, restaura solo las existentes e 
# informa cuántas recuperó.
#Prueba: atiende A, B y C; deshaz dos. Deben quedar pendientes B, C, 
#… y solo A debe permanecer atendida.
cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\nPendientes:", cola_pendientes, "\n ")
    print("Historial:", pila_historial, "\n")

def registrar_solicitud(cliente, asunto):
    global siguiente_id
    if not cliente.strip() or not asunto.strip():
        return None
    solicitud = {
        "id": siguiente_id,
        "cliente": cliente.strip(),
        "asunto": asunto.strip(),
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

###############
# nuevo def   #
###############
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

def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer ultima atención")
        print("4. Mostrar estado")
        print("5. Consultar siguiente pendiente")
        print("6. Buscar solicitud por id")
        print("7. Cancelar el siguiente pendiente")
        print("8. Cancelar mas de una pendiente")
        print("9. Salir")
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
            break
        else:
            print("Opción inválida")
                
if __name__ == "__main__":
    ejecutar_menu()