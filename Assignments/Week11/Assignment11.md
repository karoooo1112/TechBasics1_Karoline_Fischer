## Assignment 11

#### 1. Where did you find the code and why did you choose it? (Provide the link)

I found the code on github, here: https://github.com/CharlesPikachu/Games/tree/master/cpgames/core/games/pacman

One of the ideas for our final project is a maze pretty similar to pacman, so I looked specifically for a pacman game done in python. I chose this one, bc it was uploaded less than 5 years ago and the file structure was more appealing to me than in other versions I found, more organized. 


---

#### 2. What does the program do? What's the general structure of the program?

The program is a copy of the game Pacman. 

It is divided in 2 main classes: Config class und PacmanGame class. 
  The config class contains all of the game constants, the game settings, color definitions and resource paths + it also holds the file paths (and by using ```rootdir =     os.path.split(os.path.abspath(__file__))[0]``` it makes sure that all resource paths work regardless of where the game is launched from). 

  The PacmanGame class holds the core game functions, handles all events, defines how the character moves when the arrow keys are pressed, collision, the movement of the ghosts, the showing of the win or lose messages (and also what is defined as win or lose). 



---

#### 3. Function analysis: pick one function and analyze it in detail:

I will analyse the function run() because those are usually the functions I understand least. 

```def run(self):```
- name of the function 


        ```screen, resource_loader, cfg = self.screen, self.resource_loader, self.cfg```
- 3 variables are inherited from PygameBaseGame
- self.screen displays surface (was created in parent class with ```pygame.display.set_mode(config.SCREENSIZE)```)
- ```self.cfg``` = cinfig class containing all constants
- line is basically just a shortcut, so that you don't have to type self. every time


        ```pygame.display.set_icon(resource_loader.images['icon'])```
- ```resource.loader.images``` = dictonary of pygame surface objects
- ```[icon]``` --> accesses icon image (path defined in ```Config.IMAGE_PATHS_DICT```)
- sets the small icon in titel bar

  
        ```font_small = resource_loader.fonts['default_s']
        font_big = resource_loader.fonts['default_l']```
- fonts were loaded through ```Config.FONT_PATHS_DICT```
- small for rendering the score during the game
- big for win or lose text
- both of these are objects --> they don't draw themselves (are used later with ```.render()```)


        ```resource_loader.playbgm()```
- calls on resource.loader method to play background music
- bgm path was defined in ```Config.BGM_PATH```
- music starts playing immedeately and runs throughout the whole game

        
        ```for num_level in range(1, Levels.NUMLEVELS+1):```
- levels were imported from a different .py file
- ```Levels.NUMLEVELS``` = constant defined in the levels module --> tells how many levels exist
- +1 in range is needed, bc otherwise we wouldn't get the amount of actual levels but one less (range is exclusive of end value)

  
            ```level = getattr(Levels, f'Level{num_level}')()```
- most complex line
- ```f'Level {num_level}'``` --> creates Level + whatever level we're on
- ```getattr(Levels, f'Level{num_level}')``` --> dynamically gets an attribute from the Levels module by name
    - equivalent to writing ```Levels.Level1```, ```Levels.Level2``` etc.
    - with ```getattr()``` we can do it dynamically using loop variable
    - ```getattr()``` returns the class itself (not an instance)
- final ```()``` at the end --> calls that class
- resulting level object contains all the setup information for that level (wall positions, food positions, ghost paths, etc.)
- I don't even know... (ChatAI explained this to me)  


            ```is_clearance = self.startLevelGame(cfg, resource_loader, level, screen, font_small)```
- calls the function
- passes everything that is needed to run the game
    - cfg --> Config class for colors, FSP, etc.
    - resource.loader --> images
    - level --> level object with map and player data
    - screen --> pygame surface
    - font_small --> font for score

 
            ```if num_level == Levels.NUMLEVELS:
                self.showText(cfg, screen, font_big, is_clearance, True)
            else:
                self.showText(cfg, screen, font_big, is_clearance)```
 - checks if this was the last level
 - if yes --> calls showText() --> flag = True --> game restarts if player presses Enter
 - if no --> calls showText() --> Flag = False (default) --> go to next level if player presses Enter 

---

#### 4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

I learned that it might be helpful not to put the whole code into one big .py file, but split it up into its main functions like the creator of this code did (the levels, the core functions like here, the classes for characters and ghosts, etc.). I knew that we will have to do that, but seeing here how the different files were called up in the "main" code was good to see, I understand it a little better now. 

I will also look more closely at this code to see how they set up the paths for the ghosts, bc we can do it pretty similarly in our code for the one rat that will roam the maze. 

---

#### 5. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?

  I do kind of understand what is going on, like I get the basic functionality of the code, but I'm still having problems understanding how all the different functions and   classes interact, how to call on them and how to structure the whole code in a way that makes everything flow. 
  Coding out little game will definitely be a learning experience. 
---
