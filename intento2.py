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

class Boss(Enemy):
    def __init__(self, name: str, max_hp: int, strength: int, xp_reward: int, rage_level: int):
        super().__init__(name,max_hp,strength,xp_reward)
        self.rage_level = rage_level
    
    def increase_rage(self) -> None:
        self.rage_level += 3
    
    def take_damage(self, amount: int) -> None:
        super().take_damage(amount)
        self.increase_rage()

    def attack(self, other: Player) -> int:
        base_damage = super().attack(other)
        bonus_damage = self.rage_level
        total_damage = base_damage + bonus_damage

        other.take_damage(bonus_damage)
        return total_damage
        
    def __str__(self) -> str:
        return f"(Boss={self.name}, hp={self.hp}/{self.max_hp}, Rage level={self.rage_level})"


def create_boss(level: int) -> Boss:

    base_hp = 30 + level * 5
    base_strength = 5 + level
    xp = level * 10

    return Boss(
        name=f"Boss_Lv{level}",
        max_hp=base_hp,
        strength=base_strength,
        xp_reward=xp,
        rage_level = 0
    )

def battle(player: Player, boss: Boss) -> None:
    print("¡Comienza la batalla!")
    print(player)
    print(boss)
    print("-" * 30)

    turn = 1

    while player.is_alive() and boss.is_alive():
        print(f"Turno {turn}")

        damage = player.attack(boss)
        print(f"{player.name} ataca y hace {damage} de daño.")
        print(boss)

        if not boss.is_alive():
            print("¡Enemigo derrotado!")
            break

        damage = boss.attack(player)
        print(f"{boss.name} ataca y hace {damage} de daño.")
        print(player)

        if not player.is_alive():
            print(f"¡{player.name} derrotado!")
            break

        print("-" * 30)
        turn += 1

    print("Fin del combate.")

if __name__ == "__main__":
    aaron = Player(name="Aaron", max_hp=100, strength=10)
    boss = create_boss(level= random.randint(3, 6))
    battle(aaron, boss)

