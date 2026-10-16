# Pila (LIFO)
# Consiste en ir apilando un elemento encima de otro
# Por lo que, para ir retirando elementos, debo retirar el ultimo 
# ejemplo
#creo la pila
pila = []
#agrego elementos a la pila
pila.append("A")
pila.append("B")
#elimino y muestro el elemento eliminado
print(pila.pop())  
#muestro la pila sin el elemento eliminado
print(pila)

# cola (FIFO)
# Consiste en hacer una fila de elementos uno tras otro y para retirar alguno
# hay que eliminar el primero 
cola = []
#agrego elementos a la pila
cola.append("A")
cola.append("B")
# sleeciono, elimino y muestro el primer elemento
print(cola.pop(0))
print(cola)

#pregunta inicial
# si llegan ana, luis y sofia, a quien atiende primero una cola?
# a ana
# si registras tres cambios consecutivos, cual deshaces primero?
# el ultimo 
