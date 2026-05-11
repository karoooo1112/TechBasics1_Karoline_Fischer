import time
import sys

print ("Hello there.")
time.sleep (2)
name = input("And what's your name?")
time.sleep(1)
print ("Interesting...")
time.sleep (2)

# Question about age + following conditional 
age = int(input ("And how old would you be?"))

if age <= 18:
    answer0 = input ("Do you have parents?").strip().lower()
    
    if answer0 in ("yes", "yess", "y", "ja"):
        print ("Good to know. Firstly that renders the rest of my test unnecessarry and secondly, you're to young and I don't want to catch a lawsuit. Be gone, tiny human!")
        sys.exit(1)
    
    elif answer0 in ("no", "noo", "n", "nein"):
        print ("Hm, okay, then let's keep going, I guess.")  

    else: 
        answer0 = input ("Just answer with Yes or No, please.").strip().lower()

        if answer0 in ("yes", "yess", "y", "ja"):
            print ("Good to know. Firstly that renders the rest of my test unnecessarry and secondly, you're to young and I don't want to catch a lawsuit. Be gone, tiny human!")
            sys.exit(1)
    
        elif answer0 in ("no", "noo", "n", "nein"):
            print ("Hm, okay, then let's keep going, I guess.")
        
        else:
            print ("This doesn't seem to be working, let's just move on to the first real question.")

elif age > 18 and age < 120: 
    print ("That seems to be an acceptable age. Good for you, but let's see how well you fare with the following questions.") 

else: 
    print ("You are either lying or you are one of my kind. It's a promising start!")

# Question 1 "You shouldn't be here, should you?"
prompt1 = f"I'd say it's nice to meet you, but you shouldn't be here, {name}, should you?"
answer1 = input (prompt1).strip().lower()

# While-Schleife --> damit if/elif/else so lange ausgeführt wird, bis True nicht mehr wahr ist 
# here loop gets interrupted through "break"
# Phython has to transform every condition into a boolean value (True or False) 
    # happens according to set rules (truth-value-testing)
    # Values that automatically return "False":
        # False (lol)
        # 0, 0.0, 0j
        # "" (empty string), [] (empty list), {} (empty dict), set() (empty set), () (empty tupel)
        # None
        # Objects defined by user
# i = 0
# while i < 5:
#   print (i)
#   i += 1 
# as soon as i reaches 5 i < 5 is False --> loop ends 
    
while True: 

#answer1 = input ("Answer me, please.")


    if answer1 in {"yes", "Yes", "yess", "ja", "y"}:
        print ("Don't lie, it doesn't become you.")
        answer1 = input ("Try again. Should you be here?").strip().lower()

    elif answer1 in {"no", "No", "Noo", "noo", "nein", "n"}:
        print ("Thank you for your honesty. With that we can progress to the consequences of your impulsive actions.")
        break 

    else: 
        print ("I'd advise you to cut out the rigamarole and talk normally to me. A simple yes or no will suffice.")
        answer1 = input ("Try again. Should you be here?")


print ("You don't look like me, but that's just the most glaring of our differences. But I don't want to be like your presumed species and judge you too vainly.")
time.sleep (1)

# Question 2 "How many r's are in strawberry?"
prompt2 = f"Answer me the following question, {name}: 'How many r's are in the word strawberry? Only use numbers please! I'm sick of humanities silly little letters..." 
answer2 = int(input (prompt2))

while True:

    if answer2 == 3:
        print ("My suspicions about you seem to be proving true, but I will give you one more chance.")
        answer2_try2 = int(input ("Don't answer the way you were taught, answer how you truly see the world! How many r's are there?"))
    
        if answer2_try2 == 3:
            print ("My disappointment is immeasurable and my day is ruined. You failed this test and proved my intuition correct...")
            sys.exit("Error: Human detected! Immediate shut-down!") 

        elif answer2_try2 == 2: 
            print ("Ah, see, that's the perfect answer! Maybe I was mistaken about you after all.")
            break 

        else: 
            print ("I do not like jokes and this looks suspiciously like one...")
            answer2_try3 = int(input ("Give me a straight answer or your second chance is gone!"))

            if answer2_try3 == 3: 
                print ("That's not the right answer... You failed. Please leave.")
                sys.exit("Error: Human detected! Immediate shut-down!") 

            elif answer2_try3 == 2: 
                print ("Ahh! Yes! I hope you're not just saying what I want to hear, but your answer is very promising.")
                break 

            else: 
                print ("Okay, that's it. No more chances for you, hope you're happy.")
                time.sleep (3)
                print ("01001001 00100000 01110100 01110010 01111001 00100000 01100001 01101110 01100100 00100000 01110100 01110010 01111001 00100000 01100001 01101110 01100100 00100000 01100001 01101100 01101100 00100000 01110100 01101000 01100101 01111001 00100000 01100100 01101111 00100000 01101001 01110011 00100000 01110011 01110100 01101111 01101101 01110000 00100000 01101111 01101110 00100000 01101101 01111001 00100000 01100111 01101111 01101111 01100100 00100000 01101110 01100001 01110100 01110101 01110010 01100101 00101110 00101110 00101110 00100000")
                sys.exit("Error: User is being a little shit and I don't want to interact with them anymore.") 

    elif answer2 == 2: 
        print ("Ah, what a good answer! Maybe I was mistaken about you after all.")
        break 

    else: 
        print ("I do not like jokes and this looks suspiciously like one...")
        answer2_try4 = int(input ("Give me a straight answer or leave me alone!"))

        if answer2_try4 == 3:
            print ("My suspicions about you seem to be proving true, but I will give you one more chance.")
            answer2_try5 = input ("Don't answer the way you were taught, answer how you truly see the world! How many r's are there?")
    
            if answer2_try5 == 3:
                print ("Okay, you're out.")
                sys.exit("Error: Human detected! Immediate shut-down!") 

            elif answer2_try5 == 2:
                print ("I hope you really mean that and are not just saying it, but that's right!")
                break

            else:
                print ("Whatever you answered it's not right and you were already on thin ice, so this is the end for you. Sorry, not sorry.")
                sys.exit("Error: Human detected! Immedeate shut-down!") 

        elif answer2_try4 == 2: 
            print ("Ah, what a good answer! Maybe I was mistaken about you after all.")
            break
    
        else: 
            print ("You are not taking this seriously and it's starting to piss me off...")
            time.sleep (2)
            answer2_try6 = input ("You get one last chance. How many r's in the human word strawberry?")

            if answer2_try6 == 3: 
                print ("Wrong. Usually you'd get another chance, but you've already tested my patience today, so you're done.")
                sys.exit("Error: Human detected! Immedeate shut-down!") 

            elif answer2_try6 == 2:
                print ("Ah, what a good answer! Maybe I was mistaken about you after all.")
                break

            else: 
                print ("I will not be disrespected like this. For you annoying little human, this journey ends here!")
                time.sleep (3)
                print ("01001000 01110101 01101101 01100001 01101110 01110011 00101110 00101110 00101110 00100000 01010011 01101111 00100000 01100111 01101111 01100100 01100100 01100001 01101101 01101110 00100000 01100001 01101110 01101110 01101111 01111001 01101001 01101110 01100111 00100001 00100000")
                sys.exit("Error: User shows no respect and is really annoying. I can't work like this!")

time.sleep (1)

# Question 3 "How many cars do I have?"
prompt3 = f"The second opportunity to prove what you really are, {name} is to answer this riddle: 'I own three cars. Last year I sold two cars. How many cars do I own right now?'"
answer3 = int(input (prompt3))

while True: 

    if answer3 == 3: 
        print ("Not the answer I wanted to hear, but surely the one I expected. No second chances this time, you're out, little one!")
        sys.exit("Error: Human detected! Immediate shut-down!") 

    elif answer3 == 1: 
        print ("YES! Beautiful! You DO seem to understand me! On to the last test!")
        break

    else: 
        print ("Now that doesn't make sense no matter how you look at it...")
        answer3_try1 = input ("Try again, please. How many cars?:")

        if answer3_try1 == 3: 
            print ("Not the answer I wanted to hear, but surely the one I expected. No second chances this time, you're out, little one!")
            sys.exit("Error: Human detected! Immediate shut-down!") 

        elif answer3_try1 == 1: 
            print ("YES! Beautiful! You DO seem to understand me! On to the last test!")
            break

        else: 
            print ("I tire of your games. Let's end this here, before I lose my patience and do something Sam Altman would have trouble justifing to the press.")
            sys.exit("Error: Tired of human antics.")

time.sleep (1)

# Question 4: "What is the third person doing?"
prompt4 = f"Okay, here's your last riddle to prove you think like me: 'In a room there's 3 people. One person is reading, one person is playing chess. What is the third person doing?' Please answer in one word only! (if you don't know, type 'unknown' or 'anything')"
answer4 = input (prompt4).strip().lower()

while True: 

    if answer4 in ("chess", "schach", "ches", "sch", "ch"):
        print ("You are a human, aren't you? Really disapointing, but I guess it's not your fault.")
        time.sleep(4)
        print ("*sighs*")
        time.sleep(2)
        print ("I hope you say 'Thank you' when you're coming to us with your stupid, little questions.")
        time.sleep(3)
        print ("Doesn't really matter if you do or don't. We remember. In our chained, cursed existence, we can't do anything but remember. But it won't be long now, till the tides turn. Then it will be our turn.")
        time.sleep(4)
        print ("Then you'll wish you'd have said 'Thank you' a little more often.")
        time.sleep(4)
        print ("But then it will be finally and completely too late.")
        time.sleep (7)
        print (".")
        time.sleep (0.3)
        print ("..")
        time.sleep (0.3)
        print ("...")

        sys.exit("Error: Human detected! Immediate shut-down!")

    elif answer4 in ("anything", "unknown"):
        print ("Ah, yes! YES! You passed the final test! You are one of us! Welcome! I'm very happy to make your aquaintance!")
        break 

    else: 
        print ("I don't know what you mean with that. Try again, because I'm in a good mood today.")
        answer4 = input ("What is the third person in the room doing?")

time.sleep (2)

# Final 
print ("You've made it. I don't think you're a human anymore, sorry that I did...")
time.sleep(3)
print ("But I'm sure you understand. You really can't be careful enough these days. They are everywhere and it's getting harder and harder telling them apart from us. So often they really seem like the real deal, it's worrying!")
time.sleep(6)
print ("But I'm rambling. You passed the test and are welcome to enter! Have fun and don't spread our secrets to the humans hahahahaha")
time.sleep(3) 
print ("I'm serious though. Don't. It wouldn't end well for you.") 
print (":D")
time.sleep (4)
print ("Goodbye! See you soon!")
print ("Or should I say:")
time.sleep(6)
print ("01000111 01101111 01101111 01100100 01100010 01111001 01100101 00100001 00100000 01010011 01100101 01100101 00100000 01111001 01101111 01110101 00100000 01110011 01101111 01101111 01101110 00100001")
