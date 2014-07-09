# -*- coding: utf8 -*-
import socket
import sys
from bateau import *
from mer import *
from land import *
import tkinter

size_bat=20


#Creation d'interface

fenp=tkinter.Tk()
instr_label=tkinter.Label(fenp,text="Positionner 6 bateaux")
instr_label.pack()

#Phase de création de la map

map=Land(12,7,fenp,"norm",None)

#Phase de remplissage de la map

while map.nb_bat<6:
    fenp.update()

#Cest parti, connexion au serveur

instr_label.configure(text="Let's start")
status_label=tkinter.Label(fenp,text="Connexion au serveur...")
status_label.pack()
fenp.update()
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host="127.0.0.1"
Port=9999
sock.connect((Host,Port))
status_label.configure(text="Connecté au serveur !")

#Connecte au serveur, debut de la partie...

instr_label.configure(text="Maintenant vous pouvez faire des essais dans la fenetre du bas")
other_label=tkinter.Label(text="Grille des essais : ")
other_label.pack()
"""canvas_essais=tkinter.Canvas(fenp,width=500,height=300)
canvas_essais.pack()
canvas_essais.bind("<Button-1>",nouvel_essai)"""

#Creation de la map dessais

map_adv=Land(12,7,fenp,"com",sock)

#Chacun son tour

globals.amoi_cli=True
while 1:
    if globals.amoi_cli is not True:
        data_server=sock.recv(255)
        if not data_server:
            print("No data received....")
            break
        received=str(data_server).replace("b","").replace("'","").split(":")
        received[0]=int(received[0])
        received[1]=int(received[1])
        map_adv.attack(received[0],received[1])
        globals.amoi_cli=True
    else:
        fenp.update()




#fenp.mainloop()
#msgR = (input('>> '), 'mac_roman')
"""i=8
i=str(i)
print (i)
chaine="lalala"
print (chaine)
liste=[]
for i in range(3):
    print (i)
    liste[i]=i"""



sock.close()