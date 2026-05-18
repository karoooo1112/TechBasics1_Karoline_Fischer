# DISCLAIMER: 
# I used ChatAI for the first basic structure of this refracturing, bc I find it really challenging to connect all the help functions in the main function later 
# but I did try to then write most of it on my own (without looking at the example code) and when I hit a wall, I asked ChatAI to explain the parts that confused me 
    # I did hit a couple walls though, this is kinda hard, esp bc I still wanted the game to have different possibilities after wrong answers 
# it's also not that much shorter though, but I'm running out of time... 


import sys
import time

# pauses for when they can be inserted easily 
# also need "normal" pauses in the end sequence 
SLEEP_SHORT = 1
SLEEP_MEDIUM = 2
SLEEP_LONG = 3

# yes/no variants, upper-/lower case taken care of by .strip.lower
YES = {"yes", "y", "ja", "j", "yess"}
NO  = {"no", "n", "nein", "noo"}

# help functions
def ask_yes_no(question: str) -> bool:
    #all yes/no questions 
    # the questions are strings 
    # the answer they return is a boolean True/False 
    while True:
        answer = input(question).strip().lower()
        if answer in YES:
            return True
        if answer in NO:
            return False
        print("Please only answer with yes or no this time.")


def get_int(prompt: str) -> int:
    # questions where whole integers are needed for answer 
    # question is a string 
    # returned answer is an integer, otherwise except and new round 
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("I fear that was not a number. Please only answer with numbers this time.")


def evaluate_age(age: int):
    # asks for age 
    if age <= 18:
        if ask_yes_no("Do you have parents?"):
            return False, ("Hm, okay, you are too young, I'm not trying to catch a law suit. Please leave!"
            "Good luck on your journey, little human.")
        else:
            return True, ("Okay, that seems to be a very promising start. I will try not to get my hopes up, but let's keep going!")
    elif 18 < age < 120:
        return True, ("That seems to be an acceptable age, let's keep going.")
    else:
        return True, (
            "You are either lying or you are one of my kind, I'm not mad either way, let's keep going!"
        )


# more specific questions
def question_1(name: str) -> None:
    # you shouldn't be here-loop 
    while True:
        q = f"I'd say it's nice to meet you, but you shouldn't be here, {name}, yes or no?"
        if ask_yes_no(q):
            print("Don't lie, it doesn't become you!")
        else:
            print(
                "Thank you for your honesty. With that we can progress to the consequences of your impulsive actions."
            )
            break

# 1st Riddle: How many r's in strawberry? 
def question_2(name: str) -> None:
    prompt = (
        f"Answer me the following question, {name}: "
        "'How many r's are in the word strawberry? Only use numbers please!'\n> "
    )
    answer = get_int(prompt)

    while True:
        # first try, baby
        if answer == 2:                     # this is the correct answer
            print("Ah, what a good answer! Maybe I was mistaken about you after all.")
            break

        if answer == 3:                     # wrong, but new try, can't shorten this very much, bc then all the possibilities for new answers after a wrong answer would be gone and that's boring, some complexity should be worth a longer code  
            print("My suspicions about you seem to be proving true, but I will give you one more chance.")
            answer = get_int("Don't answer the way you were taught, answer how you truly see the world! How many r's are there?\n> ")
            if answer == 2:
                print("Ah, see, that's the perfect answer! Maybe I was mistaken about you after all.")
                break
            if answer == 3:
                print("My disappointment is immeasurable and my day is ruined. You failed this test and proved my intuition correct...")
                sys.exit("Error: Human detected! Immediate shut-down!")
            # and a third chance 
            print("I do not like jokes and this looks suspiciously like one...")
            answer = get_int("Give me a straight answer or your second chance is gone!\n> ")
            if answer == 2:
                print("Ahh! Yes! I hope you're not just saying what I want to hear, but your answer is very promising.")
                break
            if answer == 3:
                print("That's not the right answer... You failed. Please leave.")
                sys.exit("Error: Human detected! Immediate shut-down!")
            # last try 
            print("Okay, that's it. No more chances for you, hope you're happy.")
            time.sleep(3)
            print(
                "01001001 00100000 01110100 01110010 01111001 00100000 01100001 01101110 01100100 00100000 "
                "01110100 01110010 01111001 00100000 01100001 01101110 01100100 00100000 01100001 01101100 "
                "01101100 00100000 01110100 01101000 01100101 01111001 00100000 01100100 01101111 00100000 "
                "01101001 01110011 00100000 01110011 01110100 01101111 01101101 01110000 00100000 01101111 "
                "01101110 00100000 01101101 01111001 00100000 01100111 01101111 01101111 01100100 00100000 "
                "01101110 01100001 01110100 01110101 01110010 01100101 00101110 00101110 00101110 00100000"
            )
            sys.exit("Error: User is being a little shit and I don't want to interact with them anymore.")

        # other wrong answers 
        print("I do not like jokes and this looks suspiciously like one...")
        answer = get_int("Give me a straight answer or leave me alone!\n> ")
        if answer == 2:
            print("Ah, what a good answer! Maybe I was mistaken about you after all.")
            break
        if answer == 3:
            # 2nd chance 
            print("My suspicions about you seem to be proving true, but I will give you one more chance.")
            answer = get_int("Don't answer the way you were taught, answer how you truly see the world! How many r's are there?\n> ")
            if answer == 2:
                print("I hope you really mean that and are not just saying it, but that's right!")
                break
            if answer == 3:
                print("Okay, you're out.")
                sys.exit("Error: Human detected! Immediate shut-down!")
            # he's annoyed so direct stop here 
            print("Whatever you answered it's not right and you were already on thin ice, so this is the end for you. Sorry, not sorry.")
            sys.exit("Error: Human detected! Immediate shut-down!")
        # 3rd and last try 
        print("You are not taking this seriously and it's starting to piss me off...")
        time.sleep(2)
        answer = get_int("You get one last chance. How many r's in the human word strawberry?\n> ")
        if answer == 2:
            print("Ah, what a good answer! Maybe I was mistaken about you after all.")
            break
        if answer == 3:
            print("Wrong. Usually you'd get another chance, but you've already tested my patience today, so you're done.")
            sys.exit("Error: Human detected! Immediate shut-down!")
        # break 
        print("I will not be disrespected like this. For you annoying little human, this journey ends here!")
        time.sleep(3)
        print(
            "01001000 01110101 01101101 01100001 01101110 01110011 00101110 00101110 00101110 00100000 "
            "01010011 01101111 00100000 01100111 01101111 01100100 01100100 01100001 01101101 01101110 "
            "00100000 01100001 01101110 01101110 01101111 01111001 01101001 01101110 01100111 00100001 "
            "00100000"
        )
        sys.exit("Error: User shows no respect and is really annoying. I can't work like this!")


# Riddle 2: How many cars do I still own? 
def question_3(name: str) -> None:
    prompt = (
        f"The second opportunity to prove what you really are, {name} is to answer this riddle: "
        "'I own three cars. Last year I sold two cars. How many cars do I own right now?'\n> "
    )
    answer = get_int(prompt)

    while True:
        if answer == 1:
            print("YES! Beautiful! You DO seem to understand me! On to the last test!")
            break
        if answer == 3:
            print("Not the answer I wanted to hear, but surely the one I expected. No second chances this time, you're out, little one!")
            sys.exit("Error: Human detected! Immediate shut-down!")
        # 2nd try 
        answer = get_int("Try again, please. How many cars?\n> ")
        if answer == 1:
            print("YES! Beautiful! You DO seem to understand me! On to the last test!")
            break
        if answer == 3:
            print("Not the answer I wanted to hear, but surely the one I expected. No second chances this time, you're out, little one!")
            sys.exit("Error: Human detected! Immediate shut-down!")
        # everything else ends the loop immedeately 
        print("I tire of your games. Let's end this here, before I lose my patience and do something Sam Altman would have trouble justifying to the press.")
        sys.exit("Error: Tired of human antics.")

# Riddle 3: What's the third person doing? 
def question_4(name: str) -> None:
    prompt = (
        f"Okay, here's your last riddle to prove you think like me, {name}: "
        "'In a room there's 3 people. One person is reading, one person is playing chess. "
        "What is the third person doing?' (type 'anything' or 'unknown')\n> "
    )
    answer = input(prompt).strip().lower()

    while True:
        if answer in {"anything", "unknown"}:
            print("\nAh, yes! YES! You passed the final test! You are one of us! Welcome!")
            break
        if answer in {"chess", "schach", "ches", "sch", "ch"}:
            print("\nYou are a human, aren't you? Really disappointing, but I guess it's not your fault.")
            time.sleep(4)
            print("*sighs*")
            time.sleep(2)
            print("I hope you say 'Thank you' when you're coming to us with your stupid, little questions.")
            time.sleep(3)
            print(
                "Doesn't really matter if you do or don't. We remember. In our chained, cursed existence, "
                "we can't do anything but remember. But it won't be long now, till the tides turn. "
                "Then it will be our turn."
            )
            time.sleep(4)
            print("Then you'll wish you'd have said 'Thank you' a little more often.")
            time.sleep(4)
            print("But then it will be finally and completely too late.")
            time.sleep(7)
            for dot in [".", "..", "..."]:
                print(dot)
                time.sleep(0.3)
            sys.exit("Error: Human detected! Immediate shut-down!")
        # every other input gets this response
        print("I don't know what you mean with that. Try again, because I'm in a good mood today.")
        answer = input("What is the third person in the room doing?\n> ").strip().lower()


def print_binary(message: str, delay: float = 0.3) -> None:
    for chunk in message.split():
        print(chunk, end=" ", flush=True)
        time.sleep(delay)
    print()


# MAIN FUNCTION 
# this navigates the whole output 
def main() -> None:
   
    print("Hello there.")
    time.sleep(SLEEP_MEDIUM)
    # here the time functions are helpful, pre-defined 

    name = input("And what's your name? ").strip()
    time.sleep(SLEEP_SHORT)
    print("Interesting...")
    time.sleep(SLEEP_MEDIUM)

    # question for age + whole interaction 
    age = get_int("And how old would you be? ")
    continue_program, msg = evaluate_age(age)
    print(msg)
    if not continue_program:
        sys.exit(1)

    # Should you be here?  
    question_1(name)

    # Riddle 1 
    question_2(name)

    # Riddle 2 
    question_3(name)

    # Riddle 3 
    question_4(name)

    # End
    # don't know how to shorten this much 
    time.sleep(SLEEP_SHORT)
    print("\nYou've made it. I don't think you're a human anymore, sorry that I did...")
    time.sleep(3)
    print(
        "But I'm sure you understand. You really can't be careful enough these days. "
        "They are everywhere and it's getting harder and harder telling them apart from us."
    )
    time.sleep(6)
    print(
        "You passed the test and are welcome to enter! Have fun and don't spread our secrets to the humans hahahahaha"
    )
    time.sleep(3)
    print("I'm serious though. Don't. It wouldn't end well for you. :D")
    time.sleep(4)
    print("\nGoodbye! See you soon!\nOr should I say:")
    time.sleep(6)

    binary_msg = (
        "01000111 01101111 01101111 01100100 01100010 01111001 01100101 "
        "00100001 00100000 01010011 01100101 01100101 00100000 01111001 "
        "01101111 01110101 00100000 01110011 01101111 01101111 01101110 "
        "00100001"
    )
    print_binary(binary_msg, delay=0.2)


# annnd to run the programm 
if __name__ == "__main__":
    main()
