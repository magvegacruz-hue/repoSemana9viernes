#Implementa consultar_siguiente(), que devuelva el primer 
# pendiente sin modificar la cola.Si está vacía, devuelve None.
#Prueba: llama dos veces a la función. El mismo ID debe 
#aparecer y la longitud de la cola no debe variar.

#Como entrada puedo esperar que digite la opcion que indique que quiere consultar 
# el siguiente pendiente sin necesidad de mandarlo a atendido. Y como salida hay 2 casos, 
# en el primero devuelve la informacion del primer pendiente sin alterar la cola si hay 
# elementos en la cola, pero si no hay, devuelve None

#Como es el mismo ejercicio, solamente copiare y pegare todo lo que lleve hecho hasta el momento
#por terminos de practicidad pero sin los comentarios.

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

###############################################
#  Nuevo def                                  #
###############################################

def consultar_siguiente(siguiente):
    if not cola_pendientes:
        return None
    return cola_pendientes[0]
    
def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Consultar siguiente pendiente")
        print("6. Salir")
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
            print("El siguiente pendiente es: ", consultar_siguiente())
        elif opcion == "6":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejecutar_menu()