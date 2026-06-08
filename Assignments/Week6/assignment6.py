# might've overdone it, this took longer than anticipated... 
# most parts work, a lot of details could be added, but I'm tired and already turning this in wayyy late 

import time 
import sys

#limit for how much player can carry 
MAX_INVENTORY = 5
#10 min till player has to leave the appartment to win 
START_TIME = 600 

#ITALIC_ON = "\x1b[3m"
#ITALIC_OFF = "\x1b[0m"

# random function for italics
# code for italics --> ESC[3m (turns it on) and ESC[0m (turns it off) 
# and \x1b is the same as the ESC character (in ASCII 27, I guess) 
def italic (text: str) -> str: 
    return f"\n\x1b[3m{text}\x1b[0m\n" 
        # the \n also moves to a new line before and after (only useful in this case, in other scenarios I'd be unnecessarry)

#inventory for the player 
inventory = []

# room the player starts out in 
current_room = "bedroom"

items_in_room = [
# bedroom
{"name": "phone", 
 "type": "object", 
 "importance": "necessarry", 
 "location": "bedroom", 
 "pick_time": 10, 
 "use_time": 0, 
 "requires": ["phone charger"], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nYour phone hasn't charged during the night. It has 50%, but you are advised to bring the 'phone charger' with you." },

{"name": "laptop charger", 
 "type": "object", 
 "importance": "optional", 
 "location": "bedroom", 
 "pick_time": 5, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "You need the laptop charger to use your 'laptop' effectively. \nYou are advised to bring it."}, 

# bathroom
{"name": "ADHD meds 20 mg", 
 "type": "medication", 
 "importance": "optional", 
 "location": "bathroom", 
 "pick_time": 10, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True, 
 "description": "\n20 mg are your 2nd dose of the day, without it you will experience an uncomfortable \nand sudden drop in mood and productivity." }, 

{"name": "ADHD meds 30 mg", 
 "type": "medication", 
 "importance": "optional", 
 "location": "bathroom", 
 "pick_time": 10, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True,
 "description": "\n30 mg can be used as a 1st dose, a 1st and 2nd dose or a 2nd dose. \nIt is versatile, but also has downsides." }, 

{"name": "ADHD meds 40 mg", 
 "type": "medication", 
 "importance": "optional", 
 "location": "bathroom", 
 "pick_time": 10, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True, 
 "description": "\n40 mg are your recommended 1st dose of the day. \nThis will make you awake and help with most of your symptoms." }, 

{"name": "contact lenses", 
 "type": "medication", 
 "importance": "optional", 
 "location": "bathroom", 
 "pick_time": 20, 
 "use_time": 180, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True, 
 "description": "\nIf you put your contacts in you can leave your glasses at home. \nIt takes you 3 min to put them in." }, 

# kitchen
{"name": "coffee maker", 
 "type": "tool", 
 "importance": "optional", 
 "location": "kitchen", 
 "pick_time": 10, 
 "use_time": 240, 
 "requires": ["coffee beans"], 
 "provides": ["coffee"], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nTo make coffee, add 'coffee maker' and 'coffee beans' to your inventory \nand use the 'use' command." }, 

{"name": "coffee beans", 
 "type": "tool", 
 "importance": "optional", 
 "location": "kitchen", 
 "pick_time": 10, 
 "use_time": 240, 
 "requires": ["coffee maker"], 
 "provides": ["coffee"], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nTo make coffee, add 'coffee maker' and 'coffee beans' to your inventory \nand use the 'use' command on 'coffee maker'." },

#{"name": "coffee", 
 #"type": "drink", 
# "importance": "optional", 
 #"location": "kitchen", 
 #"pick_time": 0, 
 #"use_time": 240, 
 #"requires": [], 
 #"provides": [], 
 #"prepared": False, 
 #"consumable": True, 
 #"description": "\nCoffee gives you the first boost of the day and helps your mood immensly. \nIt can be consumed and doesn't take up space in your inventory." },

{"name": "toaster", 
 "type": "tool", 
 "importance": "optional", 
 "location": "kitchen", 
 "pick_time": 10, 
 "use_time": 120, 
 "requires": [], 
 "provides": ["toast"], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nTo make 'toast' add 'toaster' to your inventory and use the 'use' command." },

# not needed anymore, bc the virtual object that gets created replaces it 
# don't know how to make the new object consumable then though... 
#{"name": "toast", 
 #"type": "food", 
 #"importance": "optional", 
 #"location": "kitchen", 
# "pick_time": 10, 
 #"use_time": 120, 
 #"requires": ["toaster"], 
 #"provides": [], 
 #"prepared": False, 
 #"consumable": True, 
 #"description": "\nToast is a food. You need food. You are advised to consume this." },

{"name": "wallet", 
 "type": "object", 
 "importance": "necessarry", 
 "location": "kitchen", 
 "pick_time": 10, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": False,
 "description": "\nNo strings attached to the wallet, but don't forget it!" },

# hallway
{"name": "house keys", 
 "type": "tools", 
 "importance": "necessarry", 
 "location": "hallway", 
 "pick_time": 5, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nDo not forget your keys! Not even catching the bus is worth leaving your keys behind!" },

{"name": "jacket", 
 "type": "clothing", 
 "importance": "necessarry", 
 "location": "hallway", 
 "pick_time": 40, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True, 
 "description": "\nThe jacket can be packed or used (to not take up space)." },

{"name": "boots", 
 "type": "clothing", 
 "importance": "necessarry", 
 "location": "hallway", 
 "pick_time": 50, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": True, 
 "description": "\nYes, no leaving the house without shoes. Put them on quickly." },

# living room
{"name": "laptop", 
 "type": "tools", 
 "importance": "necessarry", 
 "location": "living room", 
 "pick_time": 5, 
 "use_time": 0, 
 "requires": ["laptop charger"], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nYour laptop is fully charged, but you know laptops, that won't last long. \nTo use it for longer than an hour, you need your 'laptop charger'." },

{"name": "phone charger", 
 "type": "tools", 
 "importance": "optional", 
 "location": "living room", 
 "pick_time": 5, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nTake this to charge your phone!" },

{"name": "water bottle", 
 "type": "drink", 
 "importance": "optional", 
 "location": "living room", 
 "pick_time": 5, 
 "use_time": 0, 
 "requires": [], 
 "provides": [], 
 "prepared": False, 
 "consumable": False, 
 "description": "\nYes, water is optional. Do you think you'll need to drink during the day?" }
 ]

# dictonary for the available rooms 
rooms = {
    "bedroom": {"desc": "You are in your bedroom. \nEverything looks the way you left it.", "exits": {"left": "hallway"}}, 

    "bathroom": {"desc": "You are in the bathroom. \nYou turn on the light and see the sink with your toothbrush. There is also a cabinet.", "exits": {"right": "hallway"}}, 

    "hallway": {"desc": "A lit up and carpeted hallway. \nYou can see the front door to your right and the bathroom door to your left. The kitchen door is straight ahead on the other side of the hallway.", "exits": {"left": "bathroom", "right": "front door", "straight": "kitchen"}},

    "kitchen": {"desc": "You enter a kitchen, brightly lit by large windows, \nthat let in the morning sun. A door to your left leads to the living room. The door to the hallway is behind you.", "exits": {"left": "living room", "behind": "hallway"}}, 

    "living room": {"desc": "The living room. A mess of cushions \nand your laptop lies on the coffee table. The door to the kitchen remains behind you.", "exits": {"behind": "kitchen"}}, 

    "front door": {"desc": "The front door leads outside. \nAre you sure that you have everything you need?", "exits": {"behind": "hallway"}}
}

# help functions 
def find_item_by_name(name, collection):
    name = name.lower()
    for itm in collection:
        if itm ["name"].lower() == name:
            return itm 
    return None

# how much time does it cost to do a specific action     
def time_cost (action, item):
    if action == "pick":
        return item.get("pick_time", 0)
    if action == "use":
        return item.get ("use_time", 0)
    return 0 

# core functions
# show which items are in a room 
def show_room_items():
    room_items = [itm for itm in items_in_room if itm["location"] == current_room] 
    # if there are no more items in a room
    if not room_items:
        print ("There is nothing of interest in this room...")
        return
    print ("You see:")
    for itm in room_items:
        print (f" - {itm['name'].title()} ({itm['type']})")
    print()

# how to pick up and item + add it to the inventory 
def pick_up (item_name):
    global remaining_time 

    item = find_item_by_name(item_name, [i for i in items_in_room if i["location"] == current_room])
    if not item: 
        print (f"There is no '{item_name}' here.")
        return
    
    # counts the items in the inventory + checks if already full 
    if len(inventory) >= MAX_INVENTORY:
        print ("Your bag is full! You have to drop something first.")
        return 
    
    # cost for picking up an item 
    cost = time_cost ("pick", item)
    remaining_time -= cost
    if remaining_time <= 0:
        game_over()
        return
    
    # adds new item to inventory + removes it from the room 
    inventory.append (item)
    items_in_room.remove (item)
    print (f"You pick up the {item['name']} (took {cost}s).")
    print_status()

# drop an item 
def drop(item_name):
    global remaining_time
    item = find_item_by_name (item_name, inventory)
    if not item:
        print (f"You aren't carrying a '{item_name}'.")
        return
    
    # removes item from inventory + adds it to the room player is currently in
    inventory.remove(item)
    item["location"] = current_room
    items_in_room.append(item)
    print (f"You drop the {item ['name']}.")
    print_status()

# def to use or prepare an item (coffee and toast)
def use(item_name):
    global remaining_time
    item = find_item_by_name (item_name, inventory)
    if not item:
        print (f"You don't have a '{item_name}' to use.")
        return 
    
    # check if item is already prepared
    if item ["prepared"]:
        print (f"The {item['name']} is already ready.")
        return
    
    # checking if the needed requirements are met 
    missing = [req for req in item ["requires"] if not find_item_by_name(req, inventory)]
    if missing:
        print (f"You can't use the {item ['name']} yet - you need: {', '.join(missing)}.")
        return
    
    # the time it takes to use the item 
    cost = time_cost ("use", item)
    remaining_time -= cost
    if remaining_time <= 0:
        game_over()
        return 
    
    # mark the item as prepared
    item ["prepared"] = True
    print (f"You use the {item ['name']} (took {cost}s).")

    # if the item creates a new virtual item (e.g. coffee), add it to inventory
    for new_name in item.get("provides", []):
        new_item = {"name": new_name, "type": "virtual", "importance": "optional",
                    "location": "inventory", "pick_time": 0, "use_time": 0,
                    "requires": [], "provides": [], "prepared": True,
                    "consumable": False}
        inventory.append(new_item)
        print(f"  → You now have a {new_name}.")

    # if the item is consumable, remove it after use 
    if item.get ("consumable", False):
        inventory.remove(item)
        print (f"The {item['name']} has been consumed.")
    print_status()


# yeah, shows inventory 
def show_inventory():
    if not inventory:
        print ("Your bag is empty.")
        return
    print ("You are carrying:")
    for itm in inventory:
        status = " (ready)" if itm.get ("prepared") else ""
        print (f" - {itm ['name'].title()}{status}")
    print ()



def examine(item_name):
    # first look in the inventory, then in the room 
    item = find_item_by_name (item_name, inventory) \
        or find_item_by_name(item_name, [i for i in items_in_room if i ["location"] == current_room])
    if not item:
        print (f"There is no '{item_name}' to examine.")
        return
    
    print (f"{item ['name'].title()}: a {item['type']} that is {item ['importance']}. {item ['description']}")
    if item.get ("requires"):
        print ("  It needs:", ", ".join(item["requires"]))
    if item.get ("provides"):
        print ("  Using it will give you:", ", ".join(item["provides"]))
    if item.get ("prepared"):
        print ("  It is already prepared/ready.")
    print ()


def game_over():
    print("\n⏰ TIME'S UP! You missed the bus and the day is ruined.")
    sys.exit(0)


def print_status():
    # divmod is a built in python function --> returns a tuple (quotient, remainder) when dividing by 60 
        # quotient --> whole minutes 
        # remainder --> leftover seconds 
    # splits the total number of seconds in the easiest way (bc otherwise we'd just have the seconds, non min and sec)
    mins, secs = divmod(int(remaining_time), 60)

    # mins:02d = format specifier 
        # 02 --> pad number with leading zeros to a width of 2 characters 
        # d --> treat the value as a decimal integer 
            # 5 --> 05, 12 --> stays 12 
            # interesting 
    print (f"Time left: {mins:02d}:{secs:02d}")
    # the empty print blocks just add a blank line to console to make stuff easier to read 
    print()


def move (direction):
    global current_room, remaining_time
    exits = rooms[current_room]["exits"]
    if direction not in exits:
        print("You can't go that way.")
        return
    
    move_cost = 5 
    remaining_time -= move_cost
    if remaining_time <= 0:
        game_over()
        return
    
    current_room = exits[direction]
    print (f"You walk {direction} to the {current_room}. (took {move_cost}s)")
    describe_current_room()

def describe_current_room():
    room = rooms[current_room]
    print ("\n===" + current_room.title() + " ===")
    print (room["desc"])
    show_room_items()
    print ("Exits:", ", ".join(room["exits"].keys()))
    print_status()
    


# just shows a list of all possible commands for the player 
def print_help():
    print("""\nCommands you can use:
  inventory                – show what you carry
  look                     – look around the current room
  go <direction>           – move (left, rigth, straight, behind)
  pickup <item>            – take an item (costs time)
  drop <item>              – leave an item behind
  use <item>               – prepare or activate an item
  examine <item>           – get a short description
  help                     – show this help
  quit                     – give up\n""")
    
def parse_command(raw):
    # creates a new variable + takes out whitespace, makes it lower-case
    # .split() splits the string on any whitespace --> "go north" becomes ["go", "north"]
    parts = raw.strip().lower().split()
    # in case the player didn't type anything at all 
    if not parts:
        return 
    

    cmd = parts[0]
    args = parts[1:]

    # if player commands inventory --> show_inventory function gets called
    if cmd in ("inventory", "inv"):
        show_inventory()
    # cmd look --> calls on describe_current_room
    elif cmd in ("look", "l"):
        describe_current_room()
    # here cmd must be exactly 'go'
    elif cmd == "go" and args:
        # nothing has to be joined here, bc directions are only on word
        move(args[0])
    elif cmd in ("pickup", "take", "get") and args:
        # here the .join is necessarry, bc for the program to understand which item is being commanded, 
        # the split words have to be reconnected ["coffee", "beans"] --> "coffee beans" --> then passes it to pick_up()
        pick_up (" ".join(args))
    # same same
    elif cmd == "drop" and args:
        drop (" ".join(args))
    
    elif cmd == "use" and args:
        use (" ".join(args))
    
    elif cmd == "examine" and args:
        examine(" ".join(args))
    # shows help so player can see commands 
    elif cmd == "help":
        print_help()
    
    elif cmd in ("quit", "exit"):
        print ("You gave up. Better luck next time!")
        sys.exit(0)
    
    else:
        print("I don't understand that command. Type 'help' for a list of usable commands.")


# MAIN Loop
if __name__ == "__main__":
    print("\n=== MORNING RUSH ===")
    print ("""
           You just woke up. 
           The sun is shining, but something's not right... 
           When you look to the clock on the wall, you see why:  
           
           !!it's already 8:50 o'clock!!

           You have to leave the house in 10 minutes, otherwise you'll miss your bus 
           and everything you planned for the day will go down the drain... 
           Hurry!!""")
    time.sleep(2)
    print ("""\n\n
           There are certain items you NEED (they are tagged as 'necessarry'), everything else is 'optional'. 
           But to have a successful day you have to bring certain 'optional' items.""",
           italic("                 Read the descriptions with 'examine' what might help you during the day."),
        """ 
           There are also items that can be consumed immedeately and which replace an item that would need to be packed""", 
           italic("                 (f.ex.: putting in contacts eliminates the need to bring glasses.)"))
    
    time.sleep (1)
    print_help()

    start_ts = time.time()
    remaining_time = START_TIME

    describe_current_room()

    while remaining_time > 0: 
        try: 
            user_input = input("\n>")
            parse_command (user_input)

            elapsed = time.time() - start_ts
            remaining_time = START_TIME - elapsed
            if remaining_time <= 0:
                game_over()

        
            if current_room == "hallway" and find_item_by_name ("house keys", inventory):
                print ("\n🚪 You slip the house keys into the lock, open the door and dash out just in time!")
                print ("=== YOU WIN!!! ===")
                sys.exit(0)

        # built-in exception class 
        # automatically raised when user presses Ctrl-C --> gives program a chance to clean up 
        # just beauty addition lol, not really necessarry, but if user presses Ctrl-C now, they get a nice goodbye instead of a Traceback
        except KeyboardInterrupt:
            print ("\nInterrupted - goodbye!")
            sys.exit(0)

        
