# time for breaks between the frames
import time
# os to empty the console after each frame
import os

frames = [
    """
  ^  ^
 (  o.o)
o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
   ^  ^
  (  o.o)
o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
    ^  ^
   (  o.o)
 o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
     ^  ^
    (  o.o)
  o(uuuuuu)o
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
      ^  ^
     (  o.o)
   o(uuuuuu)o
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
       ^  ^
      (  o.o)
    o(uuuuuu)o
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
       ^  ^
      (  o.o)
     o(uuuuuu)o
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
      ^  ^
     (  o.o)
     o(uuuuuu)o
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
     ^  ^
    (  o.o)
    o(uuuuuu)o
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
    ^  ^
   (  o.o)
   o(uuuuuu)o
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
   ^  ^
  (  o.o)
  o(uuuuuu)o
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
  v    v
    """,
    """
  ^  ^
 (  o.o)
 o(uuuuuu)o
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  v    v
    """,
    """
  ^  ^
 (  o.o)
o(uuuuuu)o
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
    (uuuuuu)
  v    v
    """,
    """
   ^  ^
  (  o.o)
o(uuuuuu)o
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
     (uuuuuu)
  v    v
    """,
    """
    ^  ^
   (  o.o)
 o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
      (uuuuuu)
  v    v
    """,
    """
     ^  ^
    (  o.o)
  o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
      (uuuuuu)
     (uuuuuu)
  v    v
    """,
    """
      ^  ^
     (  o.o)
   o(uuuuuu)o
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
     (uuuuuu)
    (uuuuuu)
  v    v
    """,
    """
      ^  ^
     (  o.o)
    o(uuuuuu)o
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  v    v
    """,
    """
     ^  ^
    (  o.o)
    o(uuuuuu)o
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
   (uuuuuu)
  (uuuuuu)
  v    v
    """,
    """
    ^  ^
   (  o.o)
  o(uuuuuu)o
    (uuuuuu)
    (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
   ^  ^
  (  o.o)
  o(uuuuuu)o
   (uuuuuu)
   (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
  ^  ^
 (  o.o)
 o(uuuuuu)o
  (uuuuuu)
  (uuuuuu)
 (uuuuuu)
  (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,
    """
  ^  ^
 (  o.o)
o(uuuuuu)o
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
 (uuuuuu)
  v    v
    """,


]

#loop tied to while/if not function, while loop=true the while function will run
    #if loop=false --> while function will stop
    #has to be above everything else, bc it's the condition for it to run
#frames is just the string name
#frame gets defined on the spot though --> just a temporary name for the separate elements in the frames list
    #(could also be named 'banana' or whatever else)
def animate (frames, speed, loop=True):
  while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(speed)

    if not loop:
        break

#above are just the directions for the animate function, here is the actual order
animate(frames, speed=0.05, loop=True)
