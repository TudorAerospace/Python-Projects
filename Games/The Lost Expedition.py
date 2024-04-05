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
        if self.health == 0:
            print(f"{Fore.RED + "You died!" + Fore.RESET}")
            return self.health == 0


class Canteen:
    def __init__(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")
        self.volume = 0

    def fill(self):
        print("Filling...")
        self.volume = 1000

    def drink(self):
        print("Drinking...")
        if self.volume >= 250:
            self.volume = self.volume - 250
            print(f"You have{self.volume}ml left.")
        elif self.volume == 0:
            print("Your canteen is empty.")


class Gun:
    def __init__(self, damage, type_):
        self.damage = damage
        self.type = type_


left_path = False
right_path = False
forward_path = False
game_over = False
canteen = Canteen(500, 'water')
player = Player(25, 75, 100, [])
M1A = Gun(25, 'M1A')
followers = []
action = 0

print("Welcome to The Lost Expedition!")
print("------------------------")
print("      Main Menu")
print("------------------------")
mm = (input("1. Start\n2. Credits\n"))
mm = mm.lower()
while mm not in ["start", "credits"]:
    mm = (input())
    mm = mm.lower()
if mm == "credits":
    print("Made by Tudor. Thanks for playing!")
elif mm == "start":
    print(
        "You wake up to the sound of birds and insects.\nYou open your eyes and see the green canopy of the "
        "rainforest above you.\nYou are lying on a makeshift bed of leaves and branches, covered by a tarp.\nYou "
        "feel sore and thirsty, but otherwise okay.\n \nYou look around and see the remains of the plane, "
        "half-buried in the mud and vegetation.\nYou see Bazyli, Lisa, and Raul, who are also awake and busy with "
        "their tasks.\nBazyli is checking his map and compass, Lisa is sorting out the supplies, and Raul is "
        "sharpening his machete\n\nYou get up and stretch your muscles, and wonder what the day will bring.\nYou "
        "have been in the jungle for three days but have not seen any signs of civilization or rescue.\nYou have "
        "only seen more dangers and mysteries.")
left_camp = False
while not game_over:
    while not left_camp:
        while action not in ["talk to bazyli", "talk to lisa", "talk to raul",
                             "look around camp", "leave camp"]:
            action = input(
                "----------------------------------------------\nAre you going to:\n1. Talk to Bazyli\n2. Talk to "
                "Lisa\n3. Talk to Raul\n4. Look around camp\n5. Leave "
                "camp\n----------------------------------------------\n")
            action = action.lower()
        if action == "talk to bazyli":
            if 'Bazyli' not in followers:
                print(
                    f"Bazyli: We're close... I know we're close... We just need to get over that river...\n{Fore.GREEN + "<Bazyli is now following you!>" + Fore.RESET}")
                followers.append("Bazyli")
                action = 0
            elif 'Bazyli' in followers:
                print("Bazyli: Come on, we need to go!")
                action = 0
        elif action == "talk to lisa":
            if 'Lisa' not in followers:
                print("Lisa: Looks like you still have some wounds... Let me patch them up.")
                player.health = player.health + 25
                print(
                    f"Your health is now {Fore.RED + str(player.health) + Fore.RESET}.\n{Fore.GREEN + "<Lisa is now following you!>" + Fore.RESET}")
                followers.append("Lisa")
                action = 0
            elif 'Lisa' in followers:
                print("Lisa: Looks like you're alright.")
                action = 0
        elif action == "talk to raul":
            if 'Raul' not in followers:
                print(
                    f"Raul: If we leave, we'll need supplies. Take these bandages.\n{Fore.RED + "<Bandages added to inventory>" + Fore.RESET}\n{Fore.GREEN + "<Raul is now following you!>" + Fore.RESET}")
                player.inventory.append("bandages")
                followers.append("Raul")
                action = 0
            elif 'Raul' in followers:
                print("Raul: We need to find a way out of here.")
        elif action == "look around camp":
            print(
                "You look around your makeshift camp. Your Springfield M1A rifle is leaning against the fuselage of the plane.  Food is running low, but you have enough water stored.")
            while action not in ["y", "n"]:
                action = input("Fill canteen with water? (y/n)")
                action = action.lower()
                if action == "y":
                    canteen.fill()
                    print(f"Your canteen is now full with {Fore.BLUE + str(canteen.volume) + Fore.RESET}ml of water.")
                elif action == "n":
                    print("You probably have enough water.")
            action = 0
            while action not in ["y", "n"]:
                action = input("Pick up your gun?(y/n)")
                action = action.lower()
                if action == "y":
                    print("You pick up your rifle.")
                    print(f"{Fore.RED + "<M1A Rifle added to inventory>" + Fore.RESET}")
                    player.inventory.append("M1A")
                elif action == "n":
                    print("It's probably safe out there.")
        elif action == "leave camp":
            action = input("Are you sure you want to leave?(y/n)")
            action = action.lower()
            if action == "n":
                action = 0
            elif action == "y":
                left_camp = True
                action = 0
                if len(followers) == 1:
                    print(f"You and {followers[0]} leave camp.")
                elif len(followers) == 0:
                    print("You leave camp alone.")
                elif len(followers) == 2:
                    print(f"You, {followers[0]} and {followers[1]} leave camp.")
                elif len(followers) == 3:
                    print(f"You, {followers[0]}, {followers[1]} and {followers[2]} leave camp.")
    while action not in ["left", "right", "forward", "go left", "go right", "go forward"]:
        action = input("After some time, you arrive at a fork in the road. You can either go left, right or forward.\n")
        action = action.lower()
    if action == "go left" or action == "left":
        left_path = True
    elif action == "go right" or action == "right":
        right_path = True
    elif action == "go forward" or action == "forward":
        forward_path = True
    if left_path:
        action = 0
        print("You go left.")
        left_path = False
    elif right_path:
        action = 0
        print("------------------------------------------------------------------------")
        print("You begin walking on the right path. You feel a gentle\n"
              "breeze on your face and hear the sound of a stream nearby.\n"
              "You follow the sound and find a clear, sparkling water flowing\n"
              "through the meadow. You see colorful flowers and butterflies\n"
              "all around you. You feel a sense of calm and wonder.\n")
        print("As you walk along the stream, you notice something\n"
              "moving in the trees. You look up and see a magnificent\n"
              "bird with bright feathers and a long tail. You recognize\n"
              f"it as the {Fore.LIGHTMAGENTA_EX + "**quetzal**" + Fore.RESET}, a rare and endangered species that\n"
              "was thought to be extinct. You can't believe your eyes.\n"
              "You take out your camera and snap a few pictures. You feel lucky\n"
              "and grateful to witness such a beautiful creature.\n")
        print("You decide to sit down and enjoy the view for a while.\n"
              "You feel peaceful and relaxed. You think that maybe\n"
              "this expedition was worth it after all.\n\n"
              "You begin walking back to the fork in the road.")
        print("------------------------------------------------------------------------")
        right_path = False
    elif forward_path:
        action = 0
        print("------------------------------------------------------------------------")
        print("You keep going forward. As you walk, you start hearing a rumbling river.\n"
              "You approach the bank of the river. You could keep going forward, but\n"
              "the river is infested with caimans. To the right, you see an old bridge\n"
              "You could go left, and follow the course of the river. It might lead to civilization.\n")
        print("------------------------------------------------------------------------")
        print(f"Health: {Fore.RED + str(player.health) + Fore.RESET}\n"
              f"Hydration: {Fore.BLUE + str(player.hydration) + Fore.RESET}")
        while action not in ["left", "right", "forward", "go left", "go right", "go forward"]:
            action = input()
            action = action.lower()
        if action in ["forward", "go forward"]:
            print("You decide to swim to the other side of the river.\n"
                  f"{Fore.RED + "<You get attacked by a caiman!>" + Fore.RESET}")
            if "M1A" in player.inventory:
                player.health -= 25
                print("The caiman bites you, but you shoot it with your gun!\n"
                      f"You lose {Fore.RED + "25" + Fore.RESET} health, but you successfully \n"
                      "make it to the other side of the river.")
            else:
                print("The caiman bites your arm, and won't let go!\nYou reach for your gun, but it's not there...")
                player.health = 0
                print(f"{Fore.RED + "<You died!>" + Fore.RESET}")
                game_over = True




