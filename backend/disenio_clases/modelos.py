class Partida:
    # Atributos
    self.name = String  # Nombre para la paritda
    self.id   = Int     # ID (Seguramente extraida de la primary Key de la BDD)
    self.jugadores = [Jugador1,Jugador2,Jugador3] # Lista de instancias de tipo de jugador.
    self.host = JugadorHost

    --Por si quieren cambiarlo-- self.orden_turnos = # Puede ser simplemente el orden en que aparecen los jugadores en el
                           # array de jugadores.

    # Metodos
    # - Para manejar jugadores --------------------------------------------------------------------
    agregar_jugador(jugadorA)   # Agrega el jugador A a la partida.
    obtener_siguiente_jugador() # Retorna el jugador que tiene el turno que sigue.

    sortear_turnos()            # Mezcla el array del atributo self.jugadores, los turnos
                                # son el orden en que aparecen en el arreglo para mantenerlo simple.

    # - Para el control de la partida -------------------------------------------------------------- 
    iniciar_partida() # Reparte cartas a los jugadores, sortea los turnos e inicia el primero.
    eliminar_jugador(JugadorA)
    terminar_turno_iniciar_siguiente()

    reparto_inicial_cartas_de_figura()     # Basado en la cantidad de jugadores en el Array
                                           # llama el método obtener_carta_figura() de cada jugador
                                           # con la cantidad adecuada de cartas como arg

    terminar_turno()                       # Interfaz para que el jugador que tiene el turno
                                           # pueda terminarlo.


class CartaFigura():
    # Atributos
    self.figura = Int # ID para saber cual es la figura en cuestión.
    self.revelada = Bool # Para comunicar al front que esta carta no se debe mostrar mientras sea False.

    # Metodos
    revelar()

class CartaMovimiento(): # El método constructor generaría la carta aleatoriamente
    # Atributos
    movimiento = int # Cual es el movimiento

class Jugador:
    # Atributos
    self.nickname = String
    self.ID = Int # Seguramente la PRIMARY KEY de la BDD
    
    self.mazo_cartas_movimiento = []
    self.mazo_cartas_figura = []

    # Metodos
    # - Para el manejo de cartas ------------------------------------------------------------------

    obtener_cartas_figura(n) # Agrega n cartas de figura al mazo del jugador.
    obtener_cartas_movimiento(n) # Agrega n cartas de movimiento al mazo del jugador.
    revelar_carta_figura(jugadorA) # Revela una de las cartas de figura que posee el jugador
                                   # se llamaría al fin de turno, en caso de no ser situacion
                                   # de bloqueo.
    # - Para tener accion en la partida -----------------------------------------------------------

    abandonar_partida()
    terminar_turno()


class Casilla(Enum) # Los enums en python son una bosta
    Rojo = 1
    Verde = 2
    Amarillo = 3
    Azul = 4

class Tablero:
    # Atributos
    self.casillas = [[Casilla]] # Matriz de casilla
    
    # Métodos
    swap_casillas(filax,columnax,filay,columnay)
    






