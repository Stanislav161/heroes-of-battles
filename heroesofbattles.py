class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def _show_health(self, hero):
        return max(0, hero.health)

    def start(self):
        print("\nНачинается битва героев!")
        print(f"{self.player.name} vs {self.computer.name}")
        print("========================")

        while True:
            # Ход игрока
            self.player.attack(self.computer)
            print(f"\n{self.player.name} атаковал {self.computer.name}.")
            print(f"У {self.computer.name} осталось {self._show_health(self.computer)} здоровья.")

            if not self.computer.is_alive():
                print(f"\n☠️ {self.computer.name} пал в бою!")
                print(f"🎉 Победил {self.player.name}!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"\n{self.computer.name} атаковал {self.player.name}.")
            print(f"У {self.player.name} осталось {self._show_health(self.player)} здоровья.")

            if not self.player.is_alive():
                print(f"\n☠️ {self.player.name} пал в бою!")
                print(f"🎉 Победил {self.computer.name}!")
                break


if __name__ == "__main__":
    game = Game()
    game.start()