import random

print("Welcome to Rock Paper Scissors!")

def main():
    a = 0
    c = 0
    p = 0
    game_over = False
    plays = int(input("Play to best of: "))
    while game_over == False:
        print(f"-----------------------------------\n The score is:\n Player: {p} \n Computer: {c}\n -----------------------------------")
        a=0
        b=0
        while a not in [1,2,3]:
            a = int(input("Play Rock(1), Paper(2), or Scissors(3)? "))
        b = random.randint(1,3)
        if a == b:
            if a==1:
                 print("Draw! You both drew rock!")
            elif a==2:
                print("Draw! You both drew paper!")
            elif a==3:
                print("Draw! You both drew scissors!")
        elif a == 1 and b == 2:
                 print("The computer drew paper! You lose.")
                 c = c + 1
        elif a == 1 and b == 3:
                print("The computer drew scissors. You win!")
                p = p + 1
        elif a == 2 and b == 1: 
                print("The computer drew rock. You win!")
                p = p + 1
        elif a == 2 and b == 3:
                print("The computer drew scissors! You lose.")
                c = c + 1
        elif a == 3 and b == 1:
                print("The computer drew rock! You lose.")
                c = c + 1
        elif a == 3 and b == 2: 
                print("The computer drew paper. You win!")
                p = p + 1
        if p == plays:
            print("You win the game!")
            game_over = True
        elif c == plays: 
            print("The computer wins the game!")
            game_over = True

main()