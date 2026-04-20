# TechBasics1_Karoline_Fischer

To complete this weeks assignment I wanted to make a little animation of an ASCII image. I chose a cat and made it dance for a couple of frames. 
In order to do this I first looked for a tutorial online and found some on Github, but because I have little to no prior knowledge of anything coding related, I had a hard time understanding anything, so I instead turned to the AcademicCloud AI, this time Anthropic Claude Sonnet 4.6. It explained everything very well. 

I tried to understand everything I was putting into the code and learned a few new things. When I didn't understand the purpose of a specific function, I asked the AI. To not forget immedeately, I also added comments into my code to explain most items. 

### ASCII
------
Here's the basic ASCII image I used for the animation:
<img width="118" height="269" alt="Screenshot 2026-04-20 022332" src="https://github.com/user-attachments/assets/ee67f50e-c050-45f3-bdb8-197918aa9d0d" />


I made it myself, because I needed something simple to animate. 

### Code
------
Main part of the code made with the help of Anthropic:
```python
def animate (frames, speed):
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(speed)

animate(frames, speed=0.05)
```
------
I'm really happy with how everything turned out! 
