from mer import *
from tkinter import *
from bateau import *


class Land:
    def __init__(self,width,height,fenp,type,sock):
        self.width=width
        self.height=height
        self.type=type
        self.canvas=Canvas(fenp,width=480,height=280)
        self.canvas.pack()
        self.canvas.bind("<Button-1>",self.new_try)
        self.land=[ [ 0 for i in range(self.height) ] for j in range(self.width) ]
        self.nb_bat=0
        self.sock=sock
        print(self.land)
        for ligne in range(self.width-1):
            for colonne in range(self.height-1):
                self.land[ligne][colonne]=Mer()
                for_canvas=self.normCanvas(ligne,colonne)
                self.canvas.create_rectangle(for_canvas[0],for_canvas[1],for_canvas[0]+40,for_canvas[1]+40,fill="lightblue")
                
                
    def getPoint(self,ligne,colonne):
        if(ligne<=self.width and colonne<=self.height):
            return self.land[ligne][colonne].type
    
    
    def putBat(self,new):
        if new.type == "Bateau":
            self.land[new.x][new.y]=new
            forcanvas=self.normCanvas(new.x, new.y)
            self.canvas.create_rectangle(forcanvas[0],forcanvas[1],forcanvas[0]+40,forcanvas[1]+40,fill="red")
            self.nb_bat+=1
        else:
            print("Wrong type for the addition")
    
    def new_try(self,event):
        norm=self.normMat(event.x,event.y)
        if(self.getPoint(norm[0],norm[1])=="Bateau"):
            pass
        else:
            bateau=Bateau(norm[0],norm[1])
            self.putBat(bateau)
        if self.type=="com":
            """if sock.send(bytes(norm[0],'mac roman')) == 0:
                print("there was an error sending the try")
            if sock.send(bytes(norm[1],'mac roman')) == 0:
                print("there was an error sending the try")"""
            tosend="{0}:{1}".format(norm[0],norm[1])
            if self.sock.send(bytes(tosend,'mac roman')) == 0:
                print("there was an error sending the try")
            
    
    def attack(self,i,j):
        if(self.getPoint(i,j)=="Bateau"):
            pass
        else:
            bateau=Bateau(i,j)
            self.putBat(bateau)
            print("WATER")
    
    def normMat(self,x,y):
        return int(x/40),int(y/40)
        
    
    def normCanvas(self,i,j):
        return i*40,j*40
    
    def afficher_land(self):
        for i in range(self.width):
            for j in range(self.height):
                print (self.land[i][j].type)