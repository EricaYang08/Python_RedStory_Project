import sys
from random import *
from draw import *

# exploration for glass for chapter 2
def exploration(file, sentence, bag, object):
    with open(file, encoding='utf-8') as f:
        print(f.read())
    print("---")
    # let the user choose whether they want to explore the forest
    choice1 = input("Yes or No?")
    if choice1.lower() == "no":
        return bag
    find = [True, False]
    result = choice(find)
    # if first exploration fails
    if not result:
        # ask user if they want to try again
        second_choice = input("Nothing happen. Do you want to try again? Answer Yes or No: ")
        # user do not want to try again. move on
        if second_choice.lower() == "no":
            print("No thing happen. The red leave.")
        # user decide to try again
        elif second_choice.lower() == "yes":
            result = choice(find)
            # second time fails
            if not result:
                print("Sorry. The red finds nothing.")
            # second time wins
            elif result:
                print(sentence)
                bag[object] += 1
        else:
            sys.exit()
    # first time wins
    elif result:
        print(sentence)
        bag[object] += 1
    return bag

# Chapter 1 and Chapter 2
def begin(bag):
    print("\nThe Story of The little Red Riding Hood begin...")
    with open("chap_1.txt", encoding='utf-8') as f:
        print(f.read())
    time = input("Enter A for Early Morning and Enter B for Afternoon: ")
    if time.lower() not in ["a", "b"]:
        sys.exit()

    with open("chap_2_1.txt", encoding='utf-8') as f:
        print(f.read())

    # exploration for glass
    sentence = "Beneath a violet, Red found a small, polished magnifying glass, perfect for examining things up close"
    bag = exploration("chap_2_Explore1.txt", sentence, bag, "glass")

    # exploration for knife
    sentence = "Hidden in a nook of the tree, Red found a small, sharp knife, useful for cutting through obstacles."
    bag = exploration("chap_2_Explore2.txt", sentence, bag, "knife")

    # if the user enter A for chapter 1 option
    if time.lower() == "a":
        with open("chap_2_2_mor.txt", encoding='utf-8') as f:
            print(f.read())
        choice_3 = input("Answer A for shortcut and B for Old Road: ")
    elif time.lower() == "b":
        with open("chap_2_2_aft.txt", encoding='utf-8') as f:
            print(f.read())
        choice_3 = "A"
    
    return choice_3

# Chapter 3 function
def Char3(choice_3, bag):
    # old road choice
    if choice_3.lower() == "b":
        with open("chap_3_oldroad.txt", encoding='utf-8') as f:
            print(f.read())
        f.close()
        Char4(bag)
    # shortcut choice
    elif choice_3.lower() == "a":
        with open("chap_3_shortcut.txt", encoding='utf-8') as f:
            print(f.read())
        response = input("Type A for reveals and B for Conceals: ")
        if response.lower() == "a":
            with open("chap_3_shortcut_reveals.txt", encoding='utf-8') as f:
                print(f.read())
            f.close()
            lose()
            done()
            print("You lose!")
        elif response.lower() == "b":
            with open("chap_3_shortcut_conceals.txt", encoding='utf-8') as f:
                print(f.read())
            Char4(bag)
        else:
            sys.exit()

# Story of Chapter 4
def Char4(bag):
    with open("chap_4.txt", encoding='utf-8') as f:
        print(f.read())
    clue = None
    choice = input("Type A for use and B for not use: ")
    if choice.lower() == "a":
        if bag['glass'] > 0:
            print("You use the magnifying glass")
            with open("chap_4_withglass.txt", encoding='utf-8') as f:
                print(f.read())
            clue = True
        else:
            with open("chap_4_noglass.txt", encoding='utf-8') as f:
                print(f.read())
            print("You do not have one!!!!!")
            clue = False
    elif choice.lower() == "b":
        clue = False
        with open("chap_4_noglass.txt", encoding='utf-8') as f:
            print(f.read())
    else:
        sys.exit()

    Char5(bag, clue)


def Char5(bag,clue):
    if(clue == False):
        f = open("chap_5_noclues.txt")
        print(f.read())
        f.close()
        lose()
        print("You lose!")
        done()
    else:
        f = open("chap_5_withclues.txt")
        print(f.read())
        f.close()
        choice = input("Type A for Outwit and B for Boldly: ")
        if(choice.lower() == "a"):
            if(bag['knife'] > 0):
                f = open("chap_5_withclues_outwit_knife.txt")
                print(f.read())
                f.close()
                win()
                print("You win!")
                done()
            else:
                f = open("chap_5_withclues_outwit_noknife.txt")
                print(f.read())
                f.close()
                draw_shield()
                print("You escape, but you cannot save grandma.")
                done()
        elif(choice.lower() == "b"):
            if(bag['knife'] > 0):
                f = open("chap_5_withclues_confront_knife.txt")
                print(f.read())
                f.close()
                win()
                print("You win! ")
                done()
            else:
                f = open("chap_5_withclues_confront_noknife.txt")
                print(f.read())
                f.close()
                lose()
                print("You lose! ")
                done()

            
    
# Start of the main function
bag = {"glass": 0, "knife": 0}
step = input("Are you ready for your adventure? Yes/No (if you want to exit the game after, type anything that is not the answer to exit): ")
if step.lower() == "yes":
    value = begin(bag)
else:
    sys.exit()

Char3(value, bag)
print("The story ends here.")
