from app.punto_1 import LinkedList

def test_change_head():
    """
    este metodo verifica si al intercambiar el valor que esta en la cabeza
    con el mismo la lista queda igual.
    Nota: se compara con la Double LinkedList representada como lista
    """
    lista_Doble = LinkedList([1,2,3,4,5])
    #your code here
    # example lista_Doble.exchange(k = 0,n = 0)
    assert lista_Doble.values == [1,2,3,4,5]

def test_change_head_tail():
    """
    este metodo verifica como queda la lista al intercambiar el valor que 
    esta en la cabeza con el de la cola.
    Nota: se compara con la Double LinkedList representada como lista
    """
    lista_Doble = LinkedList([1,2,3,4,5])
    # your code here
    # example lista_Doble.exchange(k = 0, n = tail)
    assert lista_Doble.values == [5,2,3,4,1]

def test_check_empty():
    """
    este metodo verifica el funcionamiento de su algoritmo si la lista es vacia.
    Nota: se compara con la Double LinkedList representada como lista
    """
    lista_Doble = LinkedList()
    # your code here
    # example lista_Doble.exchange(k = 0,n = 3)
    assert lista_Doble.values == [] # como otra opcion puede validar que suceda un error controlado