from app.punto_2 import LinkedList

def test_check_head():
    """
    este metodo verifica que la head de la lista de equipos sea el correcto.
    datos es la informacion con la que se creara la multilista
    usted debe cargar los datos
    """
    lista_Multilista = LinkedList(datos)
    assert lista_Multilista.head.nombre == "Caimanes de Barranquilla"

def test_most_runs():
    """
    este metodo verifica si se encontro el jugador con mas carreras y el equipo
    al que pertenece.
    datos es la informacion con la que se creara la multilista
    """
    lista_Multilista = LinkedList(datos)
    # your code here
    # example jugador = lista_Multilista.find_most_runs()
    # puede cambiar el resultado si el numero de carreras es entero en su algoritmo
    assert jugador == ["Porfirio L\u00f3pez", "99"]

def test_delete_team():
    """
    este metodo verifica si el algoritmo elimina un equipo, tambien se deben 
    eliminar los jugadores asociados a ese equipo.
    datos es la informacion con la que se creara la multilista
    """
    lista_Multilista = LinkedList(datos)
    # your code here
    # example lista_Multilista.delete_team("Getsemani Leones de La Trinidad")
    assert lista_Multilista.values == ["Caimanes de Barranquilla", "Gigantes de Barranquilla", "Tigres de Cartagena", "Vaqueros de Monteria"]