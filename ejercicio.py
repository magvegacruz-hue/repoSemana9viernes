#Paso 1: preparar el proyecto
cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\nPendientes:", cola_pendientes)
    print("Historial:", pila_historial)


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
