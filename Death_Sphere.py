from Tkinter import *
import random
import math
import os

root = Tk()
root.title("Death Sphere")
root.geometry("1000x600+0+0")
root.attributes('-alpha',.80)

canvas = Canvas(root,width=1000,height=600,bg="black")


target_list = []
bullet_list = []

class Encryption(object):
    def __init__(self,encryptme,decryptme):
        self.encryptme = encryptme
        self.decryptme = decryptme
            
    def encrypt(self):
        key = ''
        for emptyspace in range(0,10):
            emptyspace = random.randint(0,9)
            key += str(emptyspace)
        
        
        score2 = self.encryptme ** 2
        score3 = str(score2)[::-1]
     
        return str(key) + str(key).join(str(score3))
       
    def decrypt(self):
        tbd = self.decryptme
        oldkey = (tbd[0]+ tbd[1] + tbd[2] + tbd[3] + tbd[4]+ tbd[5]+ tbd[6]+ tbd[7]+ tbd[8]+ tbd[9])
            
        newtbd = tbd.split(oldkey)
        newtbd = "".join(newtbd)
    
        decoded = newtbd.split(oldkey)
        decoded = "".join(decoded)
            
        decoded2 = decoded[::-1]
        return math.sqrt(int(decoded2))

    
    
    
    

    
class Bullets(object):
    def __init__(self):
        
        if cannon.timer > 10:
            self.diameter = 45
        else:
            self.diameter = 16
        self.x = canvas.coords(cannon.mag_line)[0] - self.diameter
        self.y = canvas.coords(cannon.mag_line)[1] - self.diameter
        self.circle = canvas.create_oval(self.x,self.y,self.x+self.diameter*2,self.y+self.diameter*2,fill=cannon.color)
        
    
        
        
class Targets(object):
    def __init__(self):
        def make_coords():
            self.coords = [0,0]
            #set up list to place the coords into
            
            
            self.xpos_neg = random.randint(0,1)
            self.ypos_neg = random.randint(0,1)
            #1 is positive, 2 is negative
            
            
            
            
            
            if self.xpos_neg == 1:
                self.coords[0] = cannon.x + cannon.radius + random.randint(50,450)
            elif self.xpos_neg == 0:
                self.coords[0] = cannon.x + cannon.radius + random.randint(-450,-50)
                
            if self.ypos_neg == 1:
                self.coords[1] = cannon.y + cannon.radius + random.randint(50,250)
            elif self.ypos_neg == 0:
                self.coords[1] = cannon.y + cannon.radius + random.randint(-250,-50)
                
        make_coords()
                
            
        
        for powerup in target_list:
            if "powerup" in canvas.gettags(powerup.circle):
                for line in powerup.llist:
                    canvas.delete(line)
                for target in target_list:
                    if target != powerup:
                        powerup.connect_line = canvas.create_line(powerup.coords[0]+powerup.diameter/2,powerup.coords[1]+powerup.diameter/2,target.coords[0]+target.diameter/2,target.coords[1]+target.diameter/2,fill="purple")
                        powerup.llist.append(powerup.connect_line)
                
    
        if random.choice(range(0,80)) == 5 and len(canvas.find_withtag("powerup")) < 1:
            self.llist = []
            self.diameter = 30
            self.circle = canvas.create_oval(self.coords[0],self.coords[1],self.coords[0]+self.diameter,self.coords[1]+self.diameter,fill="purple",tags=("target","powerup"))
            target_list.append(self)
            self.line = canvas.create_line(cannon.x+cannon.vector/2,cannon.y+cannon.vector/2,self.coords[0]+self.diameter/2,self.coords[1]+self.diameter/2,fill="purple",tags="powerup")
            self.coords = canvas.coords(self.circle)
            for i in target_list:
                if i != self:
                    self.connect_line = canvas.create_line(self.coords[0]+self.diameter/2,self.coords[1]+self.diameter/2,i.coords[0]+i.diameter/2,i.coords[1]+i.diameter/2,fill="purple")
                    self.llist.append(self.connect_line)
        else:
            self.diameter = random.randint(20,50)
            self.circle = canvas.create_oval(self.coords[0],self.coords[1],self.coords[0]+self.diameter,self.coords[1]+self.diameter,fill=cannon.target_color,tags="target")
            target_list.append(self)
            self.line = canvas.create_line(cannon.x+cannon.vector/2,cannon.y+cannon.vector/2,self.coords[0]+self.diameter/2,self.coords[1]+self.diameter/2,fill=cannon.target_color)
            self.coords = canvas.coords(self.circle)
        
            
    
class Cannon(object):
    def __init__(self):
        self.vector = 100
        self.max_vector = 100
        self.radius = self.vector / 2
        
        
        self.x = 500 - self.radius
        self.y = 300 - self.radius
        
        
        self.color_list = ["orange","green","red","white","yellow","pink","purple","LightBlue1","NavajoWhite2"]
        self.color = "green"
        self.target_color = "green"
        self.cursor_color = "green"
        self.bg_color = "black"
        
        
        self.len = 10
        self.state = "growing"
        self.count = 0
        self.score = 0
        self.alive = True
        self.delay = 100
        self.timer = 0
        
        
        
        
        self.circle = canvas.create_oval(self.x,self.y,self.x+self.vector,self.y+self.vector,fill=self.color)
        self.outline = canvas.create_oval(self.x,self.y,self.x+self.vector,self.y+self.vector,outline="white")
        
        
        
        
        
        
        
        
        
        self.cursor_loop()
        self.bullet_loop()
        self.update()
        
    def update(self):
            
        
        if self.count < 5:
            self.count += 1
        elif self.count >= 0 and self.alive == True and len(target_list) < 20:
            self.count = 0
            if self.delay > 40:
                self.delay -= 1
            target = Targets()
        
        self.enemies_on_canvas = False
        self.in_canvas = canvas.find_all()
        for i in self.in_canvas:
            if "target" in canvas.gettags(i):
                self.enemies_on_canvas = True
        
        if self.vector >= 5 and self.enemies_on_canvas == True:
            if self.timer < 4:
                self.timer = 0
                self.vector -= 4 # 4
                self.x += 2 # 2
                self.y += 2 # 2
            else:
                self.timer -= 4
            
            
        elif self.vector < 5 and self.alive == True:
            self.alive = False
            
            with open('high_score.txt','r') as read_old_score:
                decryptsoon = read_old_score.read()
                doody = Encryption(decryptme=decryptsoon,encryptme="Ignore Me!")
                self.highest_score = doody.decrypt()
                
                
        
            death = Toplevel()
            death.title('You Died!')
            text = Text(death,bg=self.bg_color,fg=self.color)
            death.geometry("250x150+375+225")
            text.insert(INSERT,"YOUR HIGH SCORE IS %s \nYOUR SCORE IS %s" % (self.score,int(self.highest_score)))
            if self.score > self.highest_score:
                text.insert(INSERT,"\n!!NEW HIGH SCORE!!")
            text.config(state=DISABLED)
            text.pack()
            
            
            if self.score > self.highest_score:
                with open('high_score.txt','w') as new_high_score:
                    poopy = Encryption(encryptme = self.score,decryptme="Ignore Me!")
                    new_high_score.write(poopy.encrypt())
                
                
                
        
        if self.score >= 300:
            self.color = "black"
            self.target_color = "black"
            self.cursor_color = "black"
            self.bg_color = "white"
            canvas.config(bg="white")
            
                
            
        elif self.score >= 200:
            self.color = "orange"
            self.target_color = "orange"
            self.cursor_color = "orange"
        elif self.score >= 100:
            self.color = "red" 
            self.target_color = "red"  
            self.cursor_color = "red"
        elif self.score >= 50:
            self.color = "white" 
            self.target_color = "white"
            self.cursor_color = "white"
        
            
            
        
        
            
        
        canvas.delete(self.circle)
        try:
            canvas.delete(self.label)
        except AttributeError:
            pass        
        self.circle = canvas.create_oval(self.x,self.y,self.x+self.vector,self.y+self.vector,fill=self.color)
        
        
        
        
        ###^^drain health^^
        
        
        
        
        
        
        
        #root.after(int(self.delay),self.update)
        root.after(self.delay,self.update)
    def cursor_loop(self):
        try:
            canvas.delete(self.xcross)
            canvas.delete(self.ycross)
            canvas.delete(self.mag_line)
        except AttributeError:
            pass
        
        self.mx, self.my = canvas.winfo_pointerxy()
        self.mx -= 4
        self.my -= 52
        self.xcross = canvas.create_line(self.mx-self.len,self.my,self.mx+self.len,self.my,fill=self.cursor_color)
        self.ycross = canvas.create_line(self.mx,self.my-self.len,self.mx,self.my+self.len,fill=self.cursor_color)
        
        
        self.mag_line = canvas.create_line(self.x+self.vector/2,self.y+self.vector/2,self.mx,self.my,fill=self.target_color)
        
        if self.state == "growing":
            self.len += 1
            if self.len >= 30:
                self.state = "shrinking"
        elif self.state == "shrinking":
            
            self.len -= 1
            if self.len <= 0:
                self.state = "growing"
                
        root.after(1,self.cursor_loop)
    def fire(self,event):
        
        if self.alive == True:
            bullet = Bullets()
        
            bullet.bullet_vector = [canvas.coords(self.mag_line)[2] - canvas.coords(self.mag_line)[0], canvas.coords(self.mag_line)[3] - canvas.coords(self.mag_line)[1]]
        
            bullet.m1 = bullet.bullet_vector[0] ** 2
            bullet.m2 = bullet.bullet_vector[1] ** 2
        
            bullet.bullet_mag = math.sqrt(bullet.m1+bullet.m2)
            bullet.velocity = [bullet.bullet_vector[0] / bullet.bullet_mag,bullet.bullet_vector[1] / bullet.bullet_mag]
        
            bullet.velocity[0] *= 12
            bullet.velocity[1] *= 12
        
            bullet_list.append(bullet)
        
        
    def bullet_loop(self):
        try:
            for bullet in bullet_list:
                canvas.move(bullet.circle,bullet.velocity[0],bullet.velocity[1])
                
                self.bullet_bbox = canvas.bbox(bullet.circle)
                self.bullet_overlap = canvas.find_overlapping(*self.bullet_bbox)
                
                for i in self.bullet_overlap:
                    if "target" in canvas.gettags(i):
                        if "powerup" in canvas.gettags(i):
                            self.timer = 300
                            
                            
                            
                        self.needed = self.max_vector - self.vector
                        self.rad = self.needed / 2
                        self.x -= self.rad
                        self.y -= self.rad
                        self.vector += self.needed
                        
                        try:
                            if self.timer == 0:
                                canvas.delete(bullet.circle)
                                bullet_list.remove(bullet)
                        
                            canvas.delete(i)
                        except ValueError:
                            pass
                        
                        self.score += 1
                        #score
        
                        self.zeros = 10 - len(str(self.score))
        
        
                        self.label = Label(root,text="%s%s" % ( "0" * self.zeros,self.score))
                        self.label.config(bg=self.bg_color,fg=self.color)
                        self.label.place(x=461,y=220)
                        #the label with 10 digits is 79 pixels wide
                        #score
                        
                        
                if canvas.coords(bullet.circle)[0] > 1000 or canvas.coords(bullet.circle)[0] < 0 or canvas.coords(bullet.circle)[1] < 0 or canvas.coords(bullet.circle)[1] > 600:
                    canvas.delete(bullet.circle)
                    bullet_list.remove(bullet)
                        
                        
            for target in target_list:
                if target.circle not in canvas.find_all():
                    
                    if "powerup" in canvas.gettags(target.line):
                        for i in target.llist:
                            canvas.delete(i)
                            
                    canvas.delete(target.line)
                    target_list.remove(target)
                    
                    
                    
                    
                
                
        except (IndexError,ValueError):
            pass
        
            
        
            
        root.after(1,self.bullet_loop)
            
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        


class Menu(object):
    def __init__(self):
        global slider
        self.window = Toplevel()
        self.window.geometry("300x100+350+200")
        self.window.config(bg="black")
        
    
        self.button = Button(self.window,text="Begin Game",bg="black",command=self.game_start)
        self.button.config(highlightbackground="black")
        self.button.pack()
        
        self.author = Label(self.window,text="Created by Adrian Cisneros",bg="black",fg="green")
        self.author.pack()
        
        root.lower(belowThis=None)
        self.window.lift(aboveThis=None)
    
    
        
        
    def game_start(self):
        global cannon
        cannon = Cannon()
        root.bind("<ButtonPress-1>",cannon.fire) 
        
        self.window.destroy()
        
menu = Menu()





      



canvas.pack()
root.mainloop()