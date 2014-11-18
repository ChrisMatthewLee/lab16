# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590, fill='red')
player = drawpad.create_oval(390,580,410,600, fill="purple")
enemy = drawpad.create_rectangle(50,50,100,60, fill="pink")
rocket1Fired = False
hit = False
rockets = 3
counter = 3
direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()

#animating the enemy____________________________________________________________   
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        
        if rocket1Fired:
            if ry2 > 0:
                drawpad.move(rocket1,0,-10)
                self.collisionDetect()
            if ry2 < 0:
                px1,py1,px2,py2 = drawpad.coords(player)
                rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
                x = (px1 - rx1) + 7
                y = (py1 - ry1) + 3
                if rockets > 0:
                    drawpad.move(rocket1, x, y)
                rocket1Fired = False

        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)

#moving the player______________________________________________________________
    def key(self,event):
        global player
        global rocket1Fired
        global rockets
        global counter
        px1,py1,px2,py2 = drawpad.coords(player)
       
        
        #up
        if py1 > 0 and event.char == "w":
            drawpad.move(player,0,-4)
            drawpad.move(rocket1,0,-4)
         
        #down       
        if py2 < 600 and event.char == "s":
            drawpad.move(player,0,4)
            drawpad.move(rocket1,0,4)
           
        #left       
        if px1 > 0 and event.char == "a":
            drawpad.move(player,-4,0)
            drawpad.move(rocket1,-4,0)
            
        #right       
        if px2 < 800 and event.char == "d":
            drawpad.move(player,4,0)
            drawpad.move(rocket1,4,0)
            
        #space
        if event.char == " ":
            rocket1Fired = True
            rockets = rockets - 1
            if rockets > -1:
                self.rocketsTxt.configure(text = str(rockets))
    
    def collisionDetect(self):
         global rocket1
         global enemy
         global hit
         global drawpad
         global rockets
         rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
         ex1, ey1, ex2, ey2 = drawpad.coords(enemy)
         if (rx1 > ex1 and rx1 < ex2) and (ry1 > ey1 and ry1 < ey2 ):
             drawpad.delete(enemy)
             drawpad.delete(rocket1)
             rockets = rockets + 5
        
app = myApp(root)
root.mainloop()