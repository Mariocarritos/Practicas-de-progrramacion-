import random 

class Player:    
    def __init__(self, name: str, max_hp: int, strength: int):
        if max_hp <= 0:
            raise ValueError("La vida máxima debe ser mayor que 0")

        if strength <= 0:
            raise ValueError("La fuerza debe ser mayor que 0")

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.lv = 0
        self.nivel = 1
        self.inventory = []

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("El daño no puede ser negativo")

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("La curación no puede ser negativa")

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, other: "Player") -> int:
        if not isinstance(other, Player):
            raise TypeError("Solo se puede atacar a otro Player")

        if not self.is_alive():
            print(f"{self.name} no puede atacar porque está derrotado.")
            return 0

        damage = self.strength
        other.take_damage(damage)
        return damage

    def __str__(self) -> str:
        return f"Player(name={self.name}, hp={self.hp}/{self.max_hp})"

    def __repr__(self) -> str:
        return (
            f"Player(name={self.name!r}, "
            f"hp={self.hp}, max_hp={self.max_hp}, strength={self.strength})"
        )


class Enemy(Player):
    def __init__(self, name: str, max_hp: int, strength: int, xp_reward: int):
        # Llamamos al constructor de la clase padre
        super().__init__(name, max_hp, strength)
        self.xp_reward = xp_reward

    def taunt(self) -> None:
        print(f"{self.name} se burla de ti 😈")

    def attack(self, other: Player) -> int:
        base_damage = super().attack(other)
        bonus_damage = 2
        total_damage = base_damage + bonus_damage

        other.take_damage(bonus_damage)
        return total_damage


def create_basic_enemy(level: int) -> Enemy:

    base_hp = 20 + level * 5
    base_strength = 3 + level
    xp = level * 10

    return Enemy(
        name=f"Enemy_Lv{level}",
        max_hp=base_hp,
        strength=base_strength,
        xp_reward=xp,
    )


def battle(player: Player, enemy: Enemy) -> None:
    print("¡Comienza la batalla!")
    enemy.taunt()
    print(player)
    print(enemy)
    print("-" * 30)

    turn = 1

    while True:
        while player.is_alive() and enemy.is_alive():
            print(f"Turno {turn}")

            damage = player.attack(enemy)
            print(f"{player.name} ataca y hace {damage} de daño.")
            print(enemy)

            if not enemy.is_alive():
                print("¡Enemigo derrotado!")
                print(f"{player.name} gana {enemy.xp_reward} XP.")
                player.lv += enemy.xp_reward
                if player.lv >= player.nivel*100:
                    player.nivel += 1
                    player.max_hp += player.nivel* 20
                    player.strength += player.nivel*5
                    print(f"{player.name} has subido de nivel!")
                    print(f"Ahora tienes {player.max_hp} de vida y haces {player.strength} de daño")

                break

            damage = enemy.attack(player)
            print(f"{enemy.name} ataca y hace {damage} de daño.")
            print(player)

            if not player.is_alive():
                print(f"¡{player.name} derrotado!")
                break

            print("-" * 30)
            turn += 1

        print("Fin del combate.")
        print("Quieres jugar otra ronda y seguir subiedo de nivel?")
        print("-Si   /   -No")
        preg = input("")
        if preg == "No":
            print("Fin del juego")
            break
        else:
            print("Buena eleccion")
            turn = 1
            player.hp = player.max_hp
            enemy.hp = enemy.max_hp

if __name__ == "__main__":
    aaron = Player(name="Aaron", max_hp=100, strength=10)
    enemy = create_basic_enemy(level=random.randint(1, aaron.nivel*10))
    battle(aaron, enemy)

    # Prueba cosas:
    # - Cambia valores
    # - Agrega prints
    # - Rompe algo y mira el error