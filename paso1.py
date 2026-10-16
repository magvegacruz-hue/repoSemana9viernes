cola_pendientes = []
pila_historial = []
siguiente_id = 1

def mostrar_estado():
    print("\nPendientes:", cola_pendientes)
    print("Historial:", pila_historial)

#Observa: cada solicitud será un diccionario con id, cliente, asunto y estado.