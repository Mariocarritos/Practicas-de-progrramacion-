# ============================================================
# DESAFÍO PRÁCTICO — PARTE 1
# CREAR UN NUEVO TIPO DE ENEMIGO: BossEnemy
# ============================================================

# CONTEXTO:
# Hasta ahora tenemos Player y Enemy funcionando.
# El sistema es extensible, pero necesitamos algo más complejo.
#
# En videojuegos reales, no todos los enemigos son iguales.
# Algunos tienen mecánicas especiales, fases o estados internos.
#
# En este desafío vas a crear un NUEVO tipo de enemigo:
# un BossEnemy.


# ============================================================
# OBJETIVO GENERAL
# ============================================================
# Crear una clase BossEnemy que herede de Enemy
# y agregue un nuevo comportamiento basado en su estado interno.


# ============================================================
# REGLAS IMPORTANTES
# ============================================================
# - NO modifiques la clase Player
# - NO modifiques la clase Enemy
# - Todo el código nuevo va aquí
# - Lee los comentarios con atención antes de escribir código
#
# Esto simula trabajar sobre un proyecto existente.


# ============================================================
# PARTE 1 — DEFINICIÓN DE LA CLASE
# ============================================================

class BossEnemy(Enemy):
    """
    BossEnemy es un tipo especial de enemigo.

    Características:
    - Es más resistente
    - Se vuelve más peligroso a medida que recibe daño

    Esta clase DEBE heredar de Enemy.
    """

    def __init__(self, name: str, max_hp: int, strength: int, xp_reward: int):
        # TODO:
        # 1. Llamar correctamente al constructor de Enemy usando super()
        # 2. Inicializar un nuevo atributo llamado rage_level
        #    - Debe comenzar en 0
        #
        # Pista:
        # El boss parte calmado, pero no dura mucho así…

        pass  # <- elimina este pass cuando implementes el código


    # ========================================================
    # PARTE 2 — ESTADO INTERNO (RAGE)
    # ========================================================

    def increase_rage(self) -> None:
        """
        Aumenta el nivel de ira del boss.

        Esta función debe:
        - Incrementar rage_level
        - NO devolver nada
        """

        # TODO:
        # Implementar el aumento de rage_level
        pass


    # ========================================================
    # PARTE 3 — RECIBIR DAÑO (COMPORTAMIENTO ESPECIAL)
    # ========================================================

    def take_damage(self, amount: int) -> None:
        """
        El BossEnemy reacciona al daño.

        Cada vez que recibe daño:
        - Pierde vida (igual que cualquier enemigo)
        - Aumenta su rage_level

        IMPORTANTE:
        - No reescribas toda la lógica desde cero
        - Reutiliza código existente usando super()
        """

        # TODO:
        # 1. Llamar al método take_damage de la clase padre
        # 2. Luego aumentar el rage_level
        #
        # Pregunta clave:
        # ¿Qué va primero? ¿Recibir daño o aumentar la ira?
        pass


    # ========================================================
    # PARTE 4 — ATAQUE ESPECIAL
    # ========================================================

    def attack(self, other: Player) -> int:
        """
        El BossEnemy ataca al jugador.

        Regla:
        - Mientras más alto el rage_level, más daño hace

        Este método debe:
        - Reutilizar el ataque base (super)
        - Agregar daño extra según rage_level
        - Mantener el código claro y legible
        """

        # TODO:
        # 1. Llamar al ataque base
        # 2. Calcular daño extra según rage_level
        # 3. Aplicar ese daño extra al jugador
        # 4. Retornar el daño total
        #
        # No hardcodees números sin sentido.
        # Si algo es una regla del juego, hazla clara.
        pass


# ============================================================
# DESAFÍO EXTRA (OPCIONAL)
# ============================================================
# Agrega un método __str__ para BossEnemy que muestre:
# - Nombre
# - Vida actual
# - Rage level
#
# Esto NO es obligatorio, pero mejora la experiencia del sistema.


# ============================================================
# REFLEXIÓN (NO CÓDIGO)
# ============================================================
# Antes de dar esto por terminado, piensa:
#
# - ¿Qué métodos heredaste sin tocar?
# - ¿Qué métodos sobrescribiste?
# - ¿Por qué BossEnemy necesita estado interno?
# - ¿Qué pasaría si rage_level crece sin límite?
#
# Estas preguntas importan más que el código.
