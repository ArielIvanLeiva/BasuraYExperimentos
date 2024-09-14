# Aclaraciones:
En modelos.py defino las clases que son entidades e intervienen en la partida. Tuve en mente solo
aclarar los métodos necesarios para las features de este sprint.

# Sobre la BDD
Idealemente solo tenemos que guardar los atributos de cada instancia y asociarle como ID, la PRIMARY KEY que se usa en la BDD. No hay muchos problemas con respecto a eso, y mucho menos si usamo Object-Relational Mapper, en ese caso se hace casi con magia.

# Sobre la comunicación con el Front:
Es una decisión a concretar con el resto del equipo, pero mi propuesta es:
Bajo la especificación de las clases, los objetos de tipo Partida, CartaFigura, CartaMovimiento, son elementos que puramente usan WebSockets para comunicarse fuera del BackeEnd.

Por otro lado la clase Jugadores en particular está pensada para, *en general*, tener  acciones
que están claramente asociadas a un endpoint de la API, pero que dentro del BackEnd deben tener acciones no controladas por el usuario, por ejemplo administrarse los mazos, generarse las cartas que le faltan, controlar sus bloqueos, etc.

Por último la clase Tablero debe estar por un lado reflejando acciones que se toman en el Front y se comuncian hacia el back por la API, pero además deben estar reflejando el estado del tablero hacia el Front constantemente.
