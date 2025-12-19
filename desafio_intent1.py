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
        super().__init__(name, max_hp, strength)
        self.xp_reward = xp_reward
        pass

    def taunt(self) -> None:
        print(f"{self.name} se burla de ti 😈")
        pass

    def attack(self, other: Player) -> int:
        base_damage = super().attack(other)
        bonus_damage = 2
        total_damage = base_damage + bonus_damage

        other.take_damage(bonus_damage)
        return total_damage
        pass

class BossEnemy(Enemy):

    def __init__(self, name: str, max_hp: int, strength: int, xp_reward: int, rage_level: int):
        super().__init__(name, max_hp, strength, xp_reward)
        self.rage_level = rage_level

    def increase_rage(self) -> None:
        self.rage_level += 3
       
    def take_damage(self, amount: int) -> None:
        super().take_damage(amount)
        self.increase_rage()


    def attack(self, other: Player) -> int:
        base_damage = super().attack(other)
        bonus_damage = 2
        total_damage = bonus_damage + base_damage * self.rage_level
        other.take_damage(bonus_damage)
        return total_damage
        pass
    
    def attack(self, other: Player) -> int:
        super().attack(other)
        total_damage += self.rage_level
        return total_damage



def create_Boss_enemy(level: int) -> BossEnemy:

    base_hp = 20 + level * 5
    base_strength = 3 + level
    xp = level * 10

    return BossEnemy(
        name=f"BossEnemy_Lv{level}",
        rage_level=0,
        max_hp=base_hp,
        strength=base_strength,
        xp_reward=xp,
    )

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
    pass


def battle_enemy(player: Player, enemy: Enemy) -> None:
    print("¡Comienza la batalla!")
    print(player)
    print(enemy)
    print("-" * 30)

    turn = 1

    while player.is_alive() and enemy.is_alive():
        print(f"Turno {turn}")

        damage = player.attack(enemy)
        print(f"{player.name} ataca y hace {damage} de daño.")
        print(enemy)

        if not enemy.is_alive():
            print("¡Enemigo derrotado!")
            break

        damage = enemy.attack(player)
        print(f"{enemy.name} ataca y hace {damage} de daño.")
        print(player)

        print("-" * 30)
        turn += 1

    print("Fin del combate.")
    pass


def battle_boss(player: Player, bossenemy: BossEnemy) -> None:
    print("¡Comienza la batalla!")
    print(player)
    print(bossenemy)
    print("-" * 30)

    turn = 1

    while player.is_alive() and bossenemy.is_alive():
        print(f"Turno {turn}")

        damage = player.attack(bossenemy)
        print(f"{player.name} ataca y hace {damage} de daño.")
        print(bossenemy)

        if not bossenemy.is_alive():
            print("¡Enemigo derrotado!")
            break

        damage = bossenemy.attack(player)
        print(f"{bossenemy.name} ataca y hace {damage} de daño.")
        print(player)

        print("-" * 30)
        turn += 1

    print("Fin del combate.")

"""
if __name__ == "__main__":
    aaron = Player(name="Aaron", max_hp=100, strength=10)
    enemy = create_basic_enemy(level=5)
    battle(aaron, enemy)

"""

if __name__ == "__main__":
    aaron = Player(name="Aaron", max_hp=100, strength=10)
    bossenemy = create_Boss_enemy(level= 5)
    battle_boss(aaron, bossenemy)