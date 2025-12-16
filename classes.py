"""
 INTRODUCCIÓN A CLASES EN PYTHON
Alumno: Aaron

Guía básica para aprender Programación Orientada a Objetos (POO)
pensando desde ya en videojuegos, simulaciones y motores como Unity.

Lee los comentarios con calma.
Ejecuta el archivo.
Modifica cosas.
Rompe cosas.
Aprende.
"""

# ============================================================
# 1. ¿QUÉ ES UNA CLASE?
# ============================================================
# En ingeniería de software, una clase es una ABSTRACCIÓN.
# No es el objeto en sí, sino la definición de cómo debe ser y comportarse.

# Una clase describe:
# - Qué datos tiene una entidad (estado)
# - Qué acciones puede realizar (comportamiento)

# En el contexto de videojuegos, una clase representa un TIPO de entidad:
# Player, Enemy, Weapon, Projectile, etc.
# Cada instancia de la clase será un objeto concreto dentro del juego.

# En sistemas bien diseñados NO se trabaja con variables sueltas.
# Se modela el dominio usando objetos, porque:
# - Agrupan datos relacionados
# - Encapsulan lógica
# - Reducen errores
# - Escalan mejor a sistemas grandes (motores, simulaciones, IA)

# Un objeto tiene:
# - Atributos → representan su estado en un momento dado
# - Métodos → definen cómo puede cambiar ese estado


class Player:
    """
    La clase Player representa a un jugador dentro de un juego.

    Buenas prácticas que ya estamos aplicando:
    - Nombre claro (PascalCase)
    - Docstring explicando el propósito
    - Atributos bien definidos
    """

    def __init__(self, name: str, max_hp: int, strength: int):
        """
        El constructor (__init__) se ejecuta cuando creamos un Player.

        Aquí definimos el ESTADO inicial del objeto.
        """

        # Validaciones simples (código profesional empieza acá)
        if max_hp <= 0:
            raise ValueError("La vida máxima debe ser mayor que 0")

        if strength <= 0:
            raise ValueError("La fuerza debe ser mayor que 0")

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength

        # Composición: un jugador TIENE un inventario
        self.inventory = []

    # ========================================================
    # 2. MÉTODOS DE COMPORTAMIENTO
    # ========================================================

    def is_alive(self) -> bool:
        """Devuelve True si el jugador sigue con vida."""
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """
        Reduce la vida del jugador.

        Observa:
        - No devuelve nada (None)
        - Protegemos el estado interno
        """

        if amount < 0:
            raise ValueError("El daño no puede ser negativo")

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int) -> None:
        """
        Cura al jugador sin superar la vida máxima.
        """

        if amount < 0:
            raise ValueError("La curación no puede ser negativa")

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, other: "Player") -> int:
        """
        Ataca a otro jugador.

        Devuelve el daño realizado.
        """

        # Validación de tipo (importante en sistemas grandes)
        if not isinstance(other, Player):
            raise TypeError("Solo se puede atacar a otro Player")

        if not self.is_alive():
            print(f"{self.name} no puede atacar porque está derrotado.")
            return 0

        damage = self.strength
        other.take_damage(damage)
        return damage

    # ========================================================
    # 3. MÉTODOS MÁGICOS
    # ========================================================

    def __str__(self) -> str:
        """
        Representación amigable del objeto.
        Se usa cuando hacemos print(objeto)
        """
        return f"Player(name={self.name}, hp={self.hp}/{self.max_hp})"

    def __repr__(self) -> str:
        """
        Representación técnica (para debugging).
        """
        return (
            f"Player(name={self.name!r}, "
            f"hp={self.hp}, max_hp={self.max_hp}, strength={self.strength})"
        )


# ============================================================
# 4. HERENCIA
# ============================================================
# La herencia permite crear una clase a partir de otra,
# reutilizando código y extendiendo comportamiento.

# IMPORTANTE:
# Un enemigo NO es un Player.
# Esa es una mala abstracción muy común y genera diseños frágiles.

# En videojuegos, tanto el jugador como los enemigos
# suelen compartir un concepto más general, por ejemplo:
# - Character
# - Entity
# - Actor

# La herencia debe cumplir la regla "ES UN":
# - Un Player ES un Character
# - Un Enemy ES un Character
# - Un Character NO ES necesariamente un Player

# Usar herencia correctamente permite:
# - Evitar duplicar código
# - Modelar el dominio del juego de forma clara
# - Facilitar la extensión del sistema sin romperlo


class Enemy(Player):
    """
    Enemy hereda de Player.

    NOTA IMPORTANTE DE DISEÑO:
    --------------------------
    En un diseño ideal, un Enemy NO debería heredar directamente de Player.
    Ambos deberían heredar de una clase más general (por ejemplo: Character).

    Entonces… ¿por qué lo hacemos así acá?

    Porque estamos en una etapa de aprendizaje:
    - Queremos entender cómo funciona la herencia
    - Cómo reutilizar código existente
    - Cómo extender y sobrescribir comportamiento

    Este es un EJEMPLO CONTROLADO.
    Más adelante veremos cómo refactorizar esto
    a un diseño más correcto y escalable.
    """

    def __init__(self, name: str, max_hp: int, strength: int, xp_reward: int):
        # Llamamos al constructor de la clase padre
        super().__init__(name, max_hp, strength)
        self.xp_reward = xp_reward

    def taunt(self) -> None:
        """Provoca al jugador."""
        print(f"{self.name} se burla de ti 😈")

    def attack(self, other: Player) -> int:
        """
        Sobrescribimos el método attack.
        El enemigo es un poco más agresivo.
        """

        base_damage = super().attack(other)
        bonus_damage = 2
        total_damage = base_damage + bonus_damage

        other.take_damage(bonus_damage)
        return total_damage


# ============================================================
# 5. PATRÓN SIMPLE: FACTORY
# ============================================================
# Una Factory es un patrón de diseño cuyo objetivo es CENTRALIZAR
# la creación de objetos.

# En lugar de crear objetos directamente con el constructor
# en muchas partes del código, usamos una función o clase
# encargada de crearlos.

# ¿Por qué esto es importante?
# - Reduce duplicación de código
# - Facilita cambios futuros (nuevos tipos de enemigos, balance, etc.)
# - Evita errores al crear objetos mal inicializados
# - Desacopla la lógica del juego de los detalles de construcción

# En videojuegos, las factories son muy comunes:
# - Spawners de enemigos
# - Creación de armas
# - Generación de ítems
# - Carga de entidades desde archivos o datos externos

# Este es un ejemplo SIMPLE de Factory.
# No es el patrón completo ni el más avanzado,
# pero es suficiente para entender la idea clave.


def create_basic_enemy(level: int) -> Enemy:
    """
    Factory function para crear enemigos según nivel.
    """

    base_hp = 20 + level * 5
    base_strength = 3 + level
    xp = level * 10

    return Enemy(
        name=f"Enemy_Lv{level}",
        max_hp=base_hp,
        strength=base_strength,
        xp_reward=xp,
    )


# ============================================================
# 6. SIMULACIÓN SIMPLE (MINI GAME LOOP)
# ============================================================
# Este código representa una SIMULACIÓN por turnos.
# Conceptualmente, es una versión extremadamente simplificada
# de lo que en un motor de videojuegos se conoce como "game loop".

# Un game loop es responsable de:
# - Actualizar el estado del juego
# - Procesar interacciones entre entidades
# - Avanzar el tiempo o los turnos
# - Determinar cuándo una simulación termina

# En este ejemplo:
# - Player y Enemy son ENTIDADES
# - battle es el SISTEMA que coordina la interacción
# - El while representa el ciclo principal del juego

# Este enfoque separa responsabilidades:
# - Las entidades saben cómo atacar o recibir daño
# - El loop decide el orden y las reglas del combate


def battle(player: Player, enemy: Enemy) -> None:
    """
    Simula un combate por turnos entre dos entidades.

    Responsabilidad de esta función:
    - Coordinar la interacción entre Player y Enemy
    - Controlar el flujo del combate
    - Determinar cuándo el combate termina

    Esta función NO decide cómo se ataca,
    solo cuándo y en qué orden ocurre.
    """

    print("¡Comienza la batalla!")
    print(player)
    print(enemy)
    print("-" * 30)

    turn = 1

    # Ciclo principal de la simulación
    while player.is_alive() and enemy.is_alive():
        print(f"Turno {turn}")

        # Turno del jugador
        damage = player.attack(enemy)
        print(f"{player.name} ataca y hace {damage} de daño.")
        print(enemy)

        if not enemy.is_alive():
            print("¡Enemigo derrotado!")
            break

        # Turno del enemigo
        damage = enemy.attack(player)
        print(f"{enemy.name} ataca y hace {damage} de daño.")
        print(player)

        print("-" * 30)
        turn += 1

    print("Fin del combate.")


# ============================================================
# 7. ZONA DE EJECUCIÓN
# ============================================================
# Este bloque solo se ejecuta si corres este archivo directamente.
# Es una práctica PROFESIONAL.


if __name__ == "__main__":
    # Creamos un jugador
    aaron = Player(name="Aaron", max_hp=100, strength=10)

    # Creamos un enemigo con factory
    enemy = create_basic_enemy(level=2)

    # Ejecutamos una simulación
    battle(aaron, enemy)

    # Prueba cosas:
    # - Cambia valores
    # - Agrega prints
    # - Rompe algo y mira el error