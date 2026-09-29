from random import randint
import time

from math import log10, floor

def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

def far_hint(guess,num):
    if num > int(guess):
        hint = round_to_1(num - int(guess))
        print(f"Your Guess is about {hint} to the actual number")
    else:
        if num < int(guess):
            hint = round_to_1(int(guess) - num)
            print(f"Your Guess is about {hint} to the actual number")

def even_hint(num):
    if int(num) % 2 == 0:
        print("even")
    else:
        print("odd")

def close_hint(guess,num):

    if int(guess) >= num:
        print("Lower")
    else:
        print("Higher")

def random_num(start_num,end_num):

    num = randint(start_num,end_num)

    return num

game_active = True

puzzle_1 = False
puzzle_2 = False
puzzle_3 = False

close_counter = 5
even_counter = 1
far_counter = 2

while game_active:
    print("So you decided to play after all")
    print("Lemme give you some quick insight to how this will work")
    print("I'm gonna think of a random number and all you have to do is guess, simple right?")
    cont_1 = input("Press 1 to start ")
    if cont_1 == "1":
        num_1 = random_num(1,10)
        guess_1 = input("Guess the number from 1 to 10: ")
        while int(guess_1) != num_1:
            print("wrong")
            guess_1 = input("Guess the number from 1 to 10: ")
        else:
            puzzle_1 = True
    if puzzle_1:
        print("Well done you got it but its gonna get harder now")
        print("Don't worry though you can get a certain type of hint")
        print("just type your guess and close and ill tell you if its higher or lower then the number")
        num_2 = random_num(1,100)
        guess_2 = input("Now guess a number 1 to 100: ")
        while int(guess_2) != num_2:
            print("Not it buddy")
            hint_1 = input("You want a hint?: ")
            if hint_1.lower() == "close":
                close_hint(guess_2,num_2)
            guess_2 = input("Guess a number 1 to 100: ")
        else:
            puzzle_2 = True
    if puzzle_2:
        print("Consider me surprised you actually made it")
        print("Well its not over though same thing but now you can also type even to know if it is that or not")
        num_3 = random_num(1,1000)
        guess_3 = input("A number from 1 to 1000")
        while int(guess_3) != num_3:
            print("nope")
            hint_2 = input("You want a hint?: ")
            if hint_2.lower() == "close":
                close_hint(guess_3,num_3)
            if hint_2.lower() == "even":
                even_hint(num_3,hint_2)
            guess_3 = input("A number from 1 to 1000: ")
        else:
            puzzle_3 = True
    if puzzle_3:
        print("Seems I underestimated you")
        print("This is the last and hardest one")
        print("You also get a new hint by saying far and it'll tell you how far your guess is from the actual num")
        print("One last thing to make stuff harder you can only use hints specific amount of times")
        num_4 = random_num(1,10000)
        guess_4 = input("Guess a number from 1 to 10,000: ")
        while int(guess_4) != num_4:
            print("nope")
            hint_3 = input("You want a hint?: ")
            if hint_3.lower() == "close":
                if close_counter == 0:
                    print("You don't have any left")
                else:
                    close_hint(guess_4,num_4)
                    close_counter -= 1
                    print(f"You have {close_counter} close hints left")
            elif hint_3.lower() == "even":
                if even_counter == 0:
                    print("You don't have any left")
                else:
                    even_hint(num_4)
                    even_counter -= 1
                    print(f"You have {even_counter} even hints left")
            elif hint_3.lower() == "far":
                if far_counter == 0:
                    print("You don't have any left")
                else:
                    far_hint(guess_4,num_4)
                    far_counter -= 1
                    print(f"You have {far_counter} far hints left")
            guess_4 = input("Guess a number from 1 to 10,000: ")
        else:
            print("Congrats you made it")
            print("Were you expecting something?")
            print("Ofcourse there isnt anything go get a job you bum")

            
    break