#Implementa buscar_solicitud(id_solicitud) que busque primero entre pendientes
#y luego en el historial. Devuelve el registro encontrado y dónde está, o None.
#Condición: no modifiques el orden de la cola ni el de la pila

#Como entrada espero la digitacion de la accion que quiera hacer y como salida, que muestre el cliente
#cuyo registro coincida con el solicitado y que muestre la ubicacion

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

##########################
# Nuevo Def              #
##########################

def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"] == id_solicitud:
            return solicitud, "pendientes"

    for solicitud in pila_historial:
        if solicitud["id"] == id_solicitud:
            return solicitud, "historial"

    return None
    
def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer ultima atención")
        print("4. Mostrar estado")
        print("5. Consultar siguiente pendiente")
        print("6. Buscar solicitud por id")
        print("7. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cliente = input("Cliente: ")
            asunto = input("Asunto: ")
            resultado = registrar_solicitud(cliente, asunto)
            print("Registrada:", resultado if resultado else "Datos inválidos")
        elif opcion == "2":
            print("Atendida:", atender_siguiente())
        elif opcion == "3":
            print("Restaurada:", deshacer_ultima_atencion())
        elif opcion == "4":
            mostrar_estado()
        elif opcion == "5":
            print("El siguiente pendiente es:", consultar_siguiente())
        elif opcion == "6":
            texto_id = input("ID de la solicitud: ").strip()

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
                print("Debes digitar un número válido.")
        elif opcion == "7":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    ejecutar_menu()