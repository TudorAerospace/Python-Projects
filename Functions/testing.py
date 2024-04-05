# Import the random module
import random

# Define the game variables
target_distance = random.randint(10, 100) # The distance of the target in meters
bullet_speed = 800 # The speed of the bullet in meters per second
wind_speed = random.randint(-10, 10) # The speed of the wind in meters per second
wind_direction = random.choice(["left", "right"]) # The direction of the wind
hit_chance = 0.8 # The base chance of hitting the target
score = 0 # The player's score

# Define the game loop
while True:
    # Display the game instructions
    print("Welcome to the hunting minigame!")
    print("You have a hunting rifle and you need to hit the target.")
    print("The target is {} meters away from you.".format(target_distance))
    print("The wind is blowing at {} meters per second to the {}.".format(wind_speed, wind_direction))
    print("You can choose to aim left, right, or center.")
    print("Enter 'exit' to quit the game.")

    # Get the user's choice
    choice = input("Where do you want to aim? ")

    # Check if the user wants to quit
    if choice == "exit":
        print("Thanks for playing!")
        break

    # Check if the user's choice is valid
    if choice not in ["left", "right", "center"]:
        print("Invalid input. Please enter left, right, or center.")
        continue

    # Calculate the bullet's deviation due to the wind
    wind_deviation = wind_speed * target_distance / bullet_speed
    if wind_direction == "left":
        wind_deviation = -wind_deviation

    # Calculate the bullet's deviation due to the user's choice
    aim_deviation = 0
    if choice == "left":
        aim_deviation = -0.5
    elif choice == "right":
        aim_deviation = 0.5

    # Calculate the total deviation
    total_deviation = wind_deviation + aim_deviation

    # Calculate the hit probability
    hit_probability = hit_chance - abs(total_deviation)

    # Generate a random number between 0 and 1
    random_number = random.random()

    # Check if the random number is less than or equal to the hit probability
    if random_number <= hit_probability:
        # The bullet hits the target
        print("You hit the target!")
        score += 1
    else:
        # The bullet misses the target
        print("You missed the target!")

    # Display the score
    print("Your score is {}.".format(score))

    # Ask the user if they want to play again
    again = input("Do you want to play again? (y/n) ")

    # Check if the user wants to play again
    if again == "y":
        # Reset the game variables
        target_distance = random.randint(10, 100)
        wind_speed = random.randint(-10, 10)
        wind_direction = random.choice(["left", "right"])
    elif again == "n":
        # Exit the game loop
        print("Thanks for playing!")
        break
    else:
        # Invalid input
        print("Invalid input. Please enter y or n.")
        continue
