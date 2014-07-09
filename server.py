# -*- coding: utf8 -*-
import socket
import sys
import globals
from bateau import *
from mer import *
from land import *
import tkinter

list_bat=[]
nb_bat=0
size_bat=20


#Creation d'interface

fenp=tkinter.Tk()
instr_label=tkinter.Label(fenp,text="Positionner 6 bateaux")
instr_label.pack()

#Phase de création de la map

map=Land(12,7,fenp,"norm",None)

#Remplissage de la map

while map.nb_bat<6:
    fenp.update()


"""global list_essais_adv
list_essais_adv=()"""
instr_label.configure(text="Let's start")
status_label=tkinter.Label(fenp,text="Attente d'un nouveau client...")
status_label.pack()
fenp.update()

#Configuration du terrain local terminée, on passe a la connexion

sock_serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host="127.0.0.1"
Port=9999
sock_serv.bind((Host,Port))
sock_serv.listen(1)
sock_client, add_client = sock_serv.accept()

#Nouvelle connexion, on creer le nouveau terrain dessais

status_text="connection dun nouveau client ! Adresse :",add_client[0]
status_label.configure(text=status_text)
other_label=tkinter.Label(text="Grille des essais : ")
other_label.pack()
map_adv=Land(12,7,fenp,"com",sock_client)
fenp.update()

#Boucle des échanges

globals.amoi_serv=False
while 1:
    if globals.amoi_serv is not True:
        data_client=sock_client.recv(255)
        if not data_client:
            break
        received=str(data_client).replace("b","").replace("'","").split(":")
        received[0]=int(received[0])
        received[1]=int(received[1])
        map_adv.attack(received[0],received[1])
        globals.amoi_serv=True
    else:
        fenp.update()



sock_client.close()

    
