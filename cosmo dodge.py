

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import os
import pygame.mixer
#pil is python imgagery library, image for handleing image and tmaketk for connecting image and tkinter



# Initialize pygame.mixer for music
pygame.mixer.init()

# Function to play background music



# Function to play background music for Tkinter
def play_music():
    try:
        pygame.mixer.music.load("music1.mp3")  
        pygame.mixer.music.play(-1)  # Play in a loop
        pygame.mixer.music.set_volume(1.0)  # Adjust volume (0.0 to 1.0)
    except Exception as e:
        print(f"Error Loading Music: {e}")

# Call play_music to play music when the Tkinter UI is active
play_music()  # Ensure this is called to start music in Tkinter part.



# Variables
score = 0
x = ''
m = ''
username = ''
password = ''
co=''
hr=''
user=''
skyv=''
songv=''


# CSV File creation for storing user data

f = open('data.csv', 'a+', newline='')
 
# Function to handle Sign Up
def sign_up():
    global user
    
    global username
    
    global password
    
    username = inputusernameforsignin.get()
    
    password = inputpasswordforsignin.get()
    
    user = username
    
    f.seek(0, 0)
    
    readerr = csv.reader(f, delimiter=',')
    
    writerr = csv.writer(f, delimiter=',')
    
    u = False
    
    for i in readerr:
        if i[0] == username:
            u = True
    if username == "" or password == "":
        messagebox.showerror("An Error Has Occurred!", "PLease Fill All The Details.")
    elif u:
        messagebox.showerror("An Error Has Occurred!", "Username Already Exists.")
    else:
        writerr.writerow([username, password, 0])
        messagebox.showinfo("Welcome!", "Sign-Up Successful!")
        inputusernameforsignin.delete(0, tk.END)
        inputpasswordforsignin.delete(0, tk.END)


# Function to handle Login
def login():
    global username

    global password

    global user

    username = entryusernameforlogin.get()

    password = entrypasswordforlogin.get()
      
    user=username

    ch = False

    f.seek(0, 0)

    if username == "" or password == "":
        messagebox.showerror("An Error Has Occurred!", "Please Fill All The Details.")
    else:
        readerr = csv.reader(f, delimiter=',')
        f.seek(0, 0)
        for i in readerr:
            if i[0] == username and i[1] == password:
                ch = True
        if not ch:
            messagebox.showerror("An Error Has Occurred!", "Invalid Username Or Password.")
        else:
            entryusernameforlogin.delete(0, tk.END)
            entrypasswordforlogin.delete(0, tk.END)
            switch_to_rules_screen()


# Function to switch between frames
def switch_to_signup():
    frame_login.pack_forget()
    frame_signup.pack(fill="both", expand=True)


def switch_to_login():
    frame_signup.pack_forget()
    frame_login.pack(fill="both", expand=True)


def switch_to_game_menu():
    frame_difficulty.pack_forget()
    frame_game_menu.pack(fill="both", expand=True)


def switch_to_rules_screen():
    frame_login.pack_forget()
    frame_rules.pack(fill="both", expand=True)


def switch_to_model_selection():
    frame_custom.pack_forget()
    frame_model_selection.pack(fill="both", expand=True)


def switch_to_difficulty(k):
    k.pack_forget()
    frame_difficulty.pack(fill="both", expand=True)


def switch_to_custom():
    frame_rules.pack_forget()
    frame_custom.pack(fill="both", expand=True)


def switch_to_sky():
    frame_model_selection.pack_forget()
    frame_sky.pack(fill="both", expand=True)


def switch_to_song():
    frame_sky.pack_forget()
    frame_song.pack(fill="both", expand=True)




# Difficulty selection functions
def select_difficulty(level):
    global x
    global skyv
    if level=='super hard':
        f=open('data.csv','r',newline='')
        d=csv.reader(f,delimiter=',')
        g=False
        for i in d:
            
            if i[0]==user:
                if int(i[2])>200:
                    
                    g=True
        f.close()
        if g:
            x = level
            switch_to_game_menu()
            skyv='sky9.png'
        else:
            messagebox.showerror("ACHACHO! YOU ARE NOT READY YET (NOOB)!", "SCORE ABOVE 200 TO PLAY THIS LEVEL!")
    else:
        x = level
        switch_to_game_menu()

            

def custom():
    frame_rules.pack_forget()
    switch_to_model_selection()   
 

def default():
    global m
    global skyv
    global songv
    m ='spaceship1'
    skyv='pic1.jpg'
    songv=random.choice(['music.mp3']) 
    k=frame_custom
    switch_to_difficulty(k)


def set_model(model):
    global m
    m = model  # Update the model based on the button clicked
    switch_to_sky()


def set_sky(sky):
    global skyv
    skyv = sky # Update the model based on the button clicked
    
    k=frame_sky
    switch_to_difficulty(k)

def set_song(song):
    global songv
    songv= song  # Update the model based on the button clicked
    k=frame_song
    


def quit_application():
    global co
    co=False
    root.quit()
songv=random.choice(['music.mp3']) 

def quit_fullscreen(event=None):
    root.attributes('-fullscreen', False)  # Disable full-screen mode
    # Close the window


# Function to start the game and close tkinter
def start_game():
    global co
    co=True
    root.quit()  # Exit Tkinter


# Initialize the main tkinter window
root = tk.Tk()
root.title("Login / Sign Up / Game Menu")
root.geometry("1500x1000")
root.attributes('-fullscreen', True)
root.bind('<Escape>', quit_fullscreen)

# Load custom background image
background_image = Image.open('pic2.png') 
background_image = background_image.resize((1500, 1000))  # Resize to fit the window
background_photo = ImageTk.PhotoImage(background_image)


# Create frames for login, sign-up, game menu, difficulty, model selection, and rules
dominant_color = background_image.getpixel((int(background_image.width / 2), int(background_image.height / 2)))
dominant_color_hex = f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}"



frame_login = tk.Frame(root, bg=dominant_color_hex)
frame_signup = tk.Frame(root, bg=dominant_color_hex)
frame_game_menu = tk.Frame(root, bg=dominant_color_hex)
frame_model_selection = tk.Frame(root, bg=dominant_color_hex)
frame_difficulty = tk.Frame(root, bg=dominant_color_hex)
frame_rules = tk.Frame(root, bg=dominant_color_hex)
frame_custom = tk.Frame(root, bg=dominant_color_hex)
frame_sky = tk.Frame(root, bg=dominant_color_hex)
frame_song = tk.Frame(root, bg=dominant_color_hex)



# Add the background image to all frames
for frame in [frame_login, frame_signup, frame_game_menu, frame_model_selection, frame_difficulty, frame_rules,frame_custom,frame_sky,frame_song]:
    background_label = tk.Label(frame, image=background_photo)
    background_label.place(relwidth=1, relheight=1)



# Screen 1: Login Frame
label_username_login = tk.Label(frame_login, text="Username:", font=("Agency FB", 20), fg='white', bg=dominant_color_hex)
label_username_login.pack(pady=10)
entryusernameforlogin = tk.Entry(frame_login, font=("Agency FB", 20))
entryusernameforlogin.pack(pady=5)


label_password_login = tk.Label(frame_login, text="Password:", font=("Agency FB", 20), fg="white", bg=dominant_color_hex)
label_password_login.pack(pady=10)
entrypasswordforlogin = tk.Entry(frame_login, show="*", font=("Agency FB", 20))
entrypasswordforlogin.pack(pady=5)


button_login = tk.Button(frame_login, text="Login", font=("Agency FB", 20), command=login, bg=dominant_color_hex, fg="white")
button_login.pack(pady=10)

button_signup = tk.Button(frame_login, text="Sign Up", font=("Agency FB", 20), command=switch_to_signup, bg=dominant_color_hex, fg="white")
button_signup.pack(pady=10)

frame_login.pack(fill="both", expand=True)

# Sign-Up Frame
label_username_signup = tk.Label(frame_signup, text="Username:", font=("Agency FB", 20), bg=dominant_color_hex, fg='white')
label_username_signup.pack(pady=10)
inputusernameforsignin = tk.Entry(frame_signup, font=("Agency FB", 20))
inputusernameforsignin.pack(pady=5)

label_password_signup = tk.Label(frame_signup, text="Password:", fg='white', font=("Agency FB", 20), bg=dominant_color_hex)
label_password_signup.pack(pady=10)
inputpasswordforsignin = tk.Entry(frame_signup, show="*", font=("Agency FB", 20))
inputpasswordforsignin.pack(pady=5)



button_signup_action = tk.Button(frame_signup, text="Sign Up", font=("Agency FB", 20), command=sign_up, bg=dominant_color_hex, fg="white")
button_signup_action.pack(pady=10)

button_login_action = tk.Button(frame_signup, text="Login", font=("Agency FB", 20), command=switch_to_login, bg=dominant_color_hex, fg="white")
button_login_action.pack(pady=10)

rules_label = tk.Label(frame_rules, text="Welcome To Our Game :)\n \n Game Rules:\n\n1. Avoid The Obstacles.\n2. Use WASD Keys To Move.\n3. Use The Space Bar To Jump. \n4. Score Points By Dodging Obstacles.\n5. Press 'K' To Pause The Game.\n6. Press 'P'/'Q' To Pause And Play Music. \n7. Score Above 200 To Play The Super Hard Level.\n8. Survive For As Long As You Can!\n\nGood Luck!", font=("Agency FB", 20), bg=dominant_color_hex,fg='white')
rules_label.pack(pady=70)



# Model Selection Frame

label_model = tk.Label(frame_model_selection, text="Select Your Model:", font=("Agency FB", 20), fg='white', bg=dominant_color_hex)
label_model.pack(pady=20)

spaceship1_button = tk.Button(frame_model_selection, text="Spaceship", font=("Agency FB", 25), command=lambda: set_model("spaceship1"), bg=dominant_color_hex, fg="white")
spaceship1_button.pack(pady=40)


spaceship2_button = tk.Button(frame_model_selection, text="Airplane", font=("Agency FB", 25), command=lambda: set_model("spaceship2"), bg=dominant_color_hex, fg="white")
spaceship2_button.pack(pady=35)


spaceship3_button = tk.Button(frame_model_selection, text="Submarine", font=("Agency FB", 25), command=lambda: set_model("spaceship3"), bg=dominant_color_hex, fg="white")
spaceship3_button.pack(pady=35)

default_spaceship_button = tk.Button(frame_model_selection, text="default", font=("Agency FB", 25), command=lambda: set_model("spaceship1"), bg=dominant_color_hex, fg="white")
default_spaceship_button.pack(pady=35)



# Difficulty Selection Frame
label_diff = tk.Label(frame_difficulty, text="Select Your Difficulty:", font=("Agency FB", 20), fg='white', bg=dominant_color_hex)
label_diff.pack(pady=20)

easy_button = tk.Button(frame_difficulty, text="Easy (Best For Beginners)", font=("Agency FB", 25), command=lambda: select_difficulty("easy"), bg=dominant_color_hex, fg="white")
easy_button.pack(pady=40)

medium_button = tk.Button(frame_difficulty, text="Medium", font=("Agency FB", 25), command=lambda: select_difficulty("medium"), bg=dominant_color_hex, fg="white")
medium_button.pack(pady=35)

hard_button = tk.Button(frame_difficulty, text="Hard", font=("Agency FB", 25), command=lambda: select_difficulty("hard"), bg=dominant_color_hex, fg="white")
hard_button.pack(pady=35)

specialhard_button = tk.Button(frame_difficulty, text="Super Hard", font=("Agency FB", 25), command=lambda: select_difficulty("super hard"), bg=dominant_color_hex, fg="white")
specialhard_button.pack(pady=35)




customize_button = tk.Button(frame_custom, text="Customize Your Settings", font=("Agency FB", 25), command=switch_to_model_selection, bg=dominant_color_hex, fg="white")
customize_button.place(relx=0.5, rely=0.3, anchor="center")

default_button = tk.Button(frame_custom, text="Use Default Settings", font=("Agency FB", 25), command=lambda: default(), bg=dominant_color_hex, fg="white")
default_button.pack(pady=300)



label_sk = tk.Label(frame_sky, text="Select Your Battle Region:", font=("Agency FB", 20), fg='white', bg=dominant_color_hex)
label_sk.pack(pady=20)

sky1_button = tk.Button(frame_sky, text="Space", font=("Agency FB", 25), command=lambda: set_sky("pic1.jpg"), bg=dominant_color_hex, fg="white")
sky1_button.pack(pady=45)


sky2_button = tk.Button(frame_sky, text="Sky", font=("Agency FB", 25), command=lambda: set_sky("sky10.png"), bg=dominant_color_hex, fg="white")
sky2_button.pack(pady=35)


sky3_button = tk.Button(frame_sky, text="Underwater", font=("Agency FB", 25), command=lambda: set_sky("sky11.jpg"), bg=dominant_color_hex, fg="white")
sky3_button.pack(pady=35)

defaultsky_button = tk.Button(frame_sky, text="Default Sky", font=("Agency FB", 25), command=lambda: set_sky("pic1.jpg"), bg=dominant_color_hex, fg="white")
defaultsky_button.pack(pady=35)



label_sg = tk.Label(frame_song, text="Select Your Music:", font=("Agency FB", 20), fg='white', bg=dominant_color_hex)
label_sg.pack(pady=20)


song1_button = tk.Button(frame_song, text="Avengers Theme Music", font=("Agency FB", 25), command=lambda: set_song("music.mp3"), bg=dominant_color_hex, fg="white")
song1_button.pack(pady=45)


song2_button = tk.Button(frame_song, text="Singappenney", font=("Agency FB", 25), command=lambda: set_song("music3.mp3"), bg=dominant_color_hex, fg="white")
song2_button.pack(pady=35)


song3_button = tk.Button(frame_song, text="Flute Instrumental", font=("Agency FB", 25), command=lambda: set_song("music4.mp3"), bg=dominant_color_hex, fg="white")
song3_button.pack(pady=35)

defaultsong_button = tk.Button(frame_song, text="Any Song", font=("Agency FB", 25), command=lambda: set_song(random.choice(['music.mp3',"music4.mp3","music3.mp3"])), bg=dominant_color_hex, fg="white")
defaultsong_button.pack(pady=35)



# Game Menu Frame
start_button = tk.Button(frame_game_menu, text="Start Game", font=("Agency FB", 25), command=start_game, bg=dominant_color_hex, fg="white")
start_button.place(relx=0.5, rely=0.3, anchor="center")

quit_button = tk.Button(frame_game_menu, text="Quit", font=("Agency FB", 25), command=quit_application, bg=dominant_color_hex, fg="white")
quit_button.pack(pady=300)


next_button = tk.Button(frame_rules, text="Next", font=("Bank Gothic", 25), command=switch_to_custom, bg=dominant_color_hex, fg="white")
next_button.pack(pady=1)

play_music()

# Run the application
root.mainloop()

f.close()






#from here the ursina based codes starts

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

pygame.mixer.music.stop()#to stop tkinter music



def show_game_over():
        global hr
        pygame.mixer.music.pause()
        f=open('data.csv',"r")
        readerr=csv.reader(f)
        for i in readerr:
            if i[0]==username:
                hr=int(i[2])
        f.close()


        global score
        if score>hr:
            hr=score-2       
        f=open('data.csv','r')
        g=open('signin1.csv','w',newline='')
        writerr=csv.writer(g)
        readerr=csv.reader(f,delimiter=',')
        for i in readerr:
            if i[0]==username:
                if int(i[2])<score-2:
                    i.pop()
                    i.append(score-2)
                writerr.writerow(i)
            else:
                writerr.writerow(i)

        g.close()
        f.close()

        os.remove('data.csv')
        os.rename('signin1.csv',"data.csv")

        
        
    
        
        root = tk.Tk()

        # Set the background color of the window to pink
        root.config(bg='lightblue')

        var = "Game Over :) \n \n  Your Score: " + str(score-2)+ '\n\n' + 'Your High Score: ' +str(hr)
        root.title("Game Over")

        score = 0

        # Label with pink background
        label = tk.Label(root, text=var, font=("Agency FB", 35), bg='pink', fg='black')
        label.pack(padx=200, pady=200)

        # Set the window size
        root.geometry("4000x3000")

        # Button with pink background
        button1 = tk.Button(root, text="Close",font=("Agency FB", 25), bg='pink', command=root.quit)
        button1.pack(pady=30)

        root.mainloop()



if skyv=='pic1.jpg' or skyv=='sky10.png':
   
    a=size_x = random.randint(10, 15) ; b=size_y = random.randint(10, 15)  ;c=size_z = random.randint(10, 15)  
    z=6
   
    h=['rock.png','rock2.jpg','rock3.jpg','rock4.jpg','rock5.jpg']
    


elif skyv=='sky11.jpg':
       
    z=7
    h='sky9.jpg'


else :
    a=size_x = random.randint(10, 15) ; b=size_y = random.randint(10, 15)  ;c=size_z = random.randint(10, 15)  
    z=6
    h=['rock.png','rock2.jpg','rock3.jpg','rock4.jpg','rock5.jpg']
    m='spaceship1'


class Obstacle(Entity):

    def __init__(self, direction, speed, **kwargs):#__init is for initalizing class automatically called when the class is used
        super().__init__(model='shark.obj' if skyv=='sky11.jpg' else 'Rock.obj', collider="box", **kwargs)#kwarg it is a keyword argument to accept n no, of parameters
        self.direction = direction #super() gives access to methods and properties of a parent or superclass.
        self.speed = x* 3
        self.time_alive = 0 


    def move(self):
        self.time_alive += time.dt  


        
        if self.direction == 'xaxisneg': 
            self.x += self.speed * time.dt



        elif self.direction == 'xaxispos':  
            self.x -= self.speed * time.dt



        elif self.direction == 'zaxispos': 
            self.z -= self.speed * time.dt
            


        elif self.direction == 'zaxisneg': 
            self.z += self.speed * time.dt

        

        if self.time_alive > 40:
            obstacles.remove(self)
            destroy(self)
            spawn_obstacle()




app = Ursina()

window.fullscreen = True 


window.fps_counter.enabled = False
window.collider_counter.enabled = False
window.entity_counter.enabled = False


#  to stop the music if necessary and then restart it in Ursina section
pygame.mixer.music.stop()  # Stop the music from Tkinter part if needed (or leave it if continuous)

# Music settings for Ursina game
music_file = songv  # Choose a music file randomly
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)  # Play the music in a loop
pygame.mixer.music.set_volume(1.0)  # Adjust volume (0.0 to 1.0)





controls = FirstPersonController()  
controls.speed=20
controls.gravity=1
controls.jump_height = 20


if x=='easy':
    x=4
    y=8


elif x=='medium':
    x=9
    y=11


elif x=='hard':
    x=11
    y=14


elif x=='super hard':
    x=12
    y=15




if m=='spaceship1':
    o=1.2
    m='spaceship4'


elif m=='spaceship2':
    m='airplane.glb'
    o=0.2
   

elif m=='spaceship3':
    m='submarine.glb'
    o=2


player = Entity(model=m, scale=o, position=(0, 6, 0), parent=controls, collider="box") 


ground = Entity(model="cube", scale=(155, 2, 155), collider="box", texture=skyv if skyv!='sky11.jpg' else 'sky11.jpg', texture_scale=(1,1))


texture_my= skyv 
Sky(texture=texture_my)

camera.position = (0, 7, -80)

camera.rotation_x = 30

camera.look_at(player)


obstacles = []


def spawn_obstacle():

   
     edges = {'xaxisneg': (-75, 14, random.randint(-75, 75)), 'xaxispos': (75, 14, random.randint(-75, 75)),   'zaxisneg': (random.randint(-75, 75), 14, -75),  'zaxispos': (random.randint(-75, 75), 14, 75) }  if skyv!='sky11.jpg' else {'xaxisneg': (-75, 4, random.randint(-75, 75))}
    
       
    

 

     speed = random.uniform(x,y)

 
     direction, position = random.choice(list(edges.items()))
 
     obstacle = Obstacle( direction=direction,speed=speed,scale=z,position=position,texture= 'blue1.jpg' if skyv=='sky11.jpg' else random.choice(['rock3.jpg','rock2.jpg','rock4.jpg','rock5.jpg']) )
    

     obstacles.append(obstacle)


spawn_obstacle()


# Initialize the paused state
# Initialize the paused state

is_paused = False

paused_text = None  # To hold the "Paused" screen text


last_pause_time = 0  # To track the last time 'K' was pressed


def k_pause():

    global is_paused, paused_text, last_pause_time


    current_time = time.time()  # Get the current time
    if current_time - last_pause_time < 0.3:  # Prevent rapid toggling (debounce)
        return


    last_pause_time = current_time  # Update the last pause time


    is_paused = not is_paused  # Toggle the paused state

    if is_paused:

        # Stop obstacles and disable controls
        for obstacle in obstacles:
            obstacle.speed = 0
        controls.enabled = False


        pygame.mixer.music.pause()
        # Show "Paused" text
        paused_text = Text(
            f"Game Paused\nPress 'K' to Resume\nYour Score: {score-2}",
            scale=2,
            origin=(0, 0),
            color=color.white,
            position=(0, 0),
        )
    else:

        # Resume obstacles and enable controls
        for obstacle in obstacles:
            obstacle.speed = x * 3 
        controls.enabled = True
        if not c:
            pygame.mixer.music.unpause()

        # Remove the "Paused" text
        if paused_text:
            destroy(paused_text)
            paused_text = None


score_text = Text(f"Score: {score}", scale=1.5, position=(-0.8, 0.45), color=color.white)

score=0


# Update function
def update():
    global hr, score

    # Handle pause functionality with the 'K' key
    if held_keys['k']:
        k_pause()
        return  # Skip the rest of the update loop when pausing

    if is_paused:
        return  # Skip updates when paused

    # Update the score display
    score_text.text = f"Score: {score-2}"  # Dynamically update the score text

    if score<50:
        p=5

    elif score<100:
        p=8

    elif score <150 :
        p=12

    else:
        p=15

    if len(obstacles) < p:
        if random.random() < 0.02:
            spawn_obstacle()



    for obstacle in obstacles[:]:  # Iterate over obstacles
        obstacle.move()

        # Check for collision
        if player.intersects(obstacle).hit:
            show_game_over()  # Show game over screen
            application.quit()

        # Remove obstacles that move out of bounds
        if abs(obstacle.x) > 75 or abs(obstacle.z) > 75:
            obstacles.remove(obstacle)
            destroy(obstacle)
            score += 2  # Increment score for dodging an obstacle

        if abs(player.x) > 75 or abs(player.z) > 75:
            show_game_over()  # Show game over screen
            application.quit()
            

    global c
    # Music controls
    if held_keys['q']:  # Stop music with 'Q'
        pygame.mixer.music.pause()
        c=True   

    if held_keys['p']:  # Resume music with 'P'
        pygame.mixer.music.unpause()
        c=False
c=False        
if co:
  app.run()