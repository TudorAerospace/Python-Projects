from colorama import Fore


class Player:
    def __init__(self, hydration, health, sanity, inventory):
        self.hydration = hydration
        self.health = health
        self.sanity = sanity
        self.inventory = inventory

    def check_stats(self):
        print(f"Hydration: {Fore.BLUE + str(self.hydration) + Fore.RESET}")
        print(f"Health: {Fore.RED + str(self.health) + Fore.RESET}")
    @property
    def is_dead(self):
        return self.health == 0


player = Player(25, 75, 100, [])

player.inventory.append("Hello")

print(player.inventory)

followers = ['Bazyli', 'Lisa', 'Raul']
print(len(followers))

player.check_stats()