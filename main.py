#Paso 1: preparar el proyecto
cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\nPendientes:", cola_pendientes, "\n ")
    print("Historial:", pila_historial, "\n")


#Observa: cada solicitud será un diccionario con id, cliente, asunto y estado.

#Paso 2: registrar solicitudes en una cola
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


registrar_solicitud("Ana", "No conecta a Wi-Fi")
registrar_solicitud("Luis", "Impresora sin papel")
registrar_solicitud("Sofía", "Equipo lento")
mostrar_estado()

#Verificación: deben existir tres solicitudes en orden de registro, con identificadores 1, 2 y 3.
#Prueba también un cliente vacío: la cola no debe cambiar.

#Paso 3: atender la cola y registrar acciones en la pila
def atender_siguiente():
    if not cola_pendientes:
        return None

    solicitud = cola_pendientes.pop(0)
    solicitud["estado"] = "atendida"
    pila_historial.append(solicitud)
    return solicitud


print("Atendida:", atender_siguiente())
mostrar_estado()

#Verificación: Ana debe salir de la cola y aparecer en el historial 
# como atendida. Al atender nuevamente, debe salir Luis. Cuando la cola 
#está vacía, la función debe devolver None sin fallar.

#Paso 4: deshacer la última atención

def deshacer_ultima_atencion():
    if not pila_historial:
        return None

    solicitud = pila_historial.pop()
    solicitud["estado"] = "pendiente"
    cola_pendientes.insert(0, solicitud)
    return solicitud


print("Restaurada:", deshacer_ultima_atencion())
mostrar_estado()
#Verificación: si se atendió a Ana y después a Luis, el primer deshacer 
# devuelve a Luis al inicio; otro deshacer devuelve a Ana antes que Luis. 
# ¿Por qué?
#porque al atender a ana, ella pasa a atendidos y luis queda pendiente
#cuando se atiende a luis, pasa de pendiente a atendido. El primer deshacer devuelve al estado anterior
#Luis pasa de atendido a pendiente y ana queda igual. Al hacer el segundo deshacer, se vuelve al estado anterior 
#al que estamos ahorita, por lo que Ana vuelve a estar en pendientes, y estará antes que luis porque 
#así estaba anteriormente, no solamente devuelve a determinado grupo el deshacer, sino que 
#mantiene el mismo orden también

#Paso 5: crear un menu interactivo
def ejecutar_menu():
    while True:
        print("\n1. Registrar solicitud")
        print("2. Atender siguiente")
        print("3. Deshacer última atención")
        print("4. Mostrar estado")
        print("5. Salir")
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
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejecutar_menu()