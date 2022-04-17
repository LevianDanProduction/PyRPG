import P_8
from P_8 import *
import random
#from operator import itemgetter
#import copy
#import statusbar
import time
import simpleaudio as sa
import sys
import os


#Game itself
classes = ("Warrior","Mage")


sound3 = s('charactercreate')
sound4 = s('select')
sound5 = s('select')


print("Time to Create Your Character")
time.sleep(2)
sound3.playSound(0.5)
print("")

while True:
    name = input("What is your Name?: ")
    if not name == "":
        break
    
while True:
    gender = input(" What is your Gender ?: ")
    if not gender == "":
        break
    
while True:
    specialTitle =  input("Have any special title?: ") + " "
    if not specialTitle == "":
        break


while True:
    classType = input("Mage or Warrior: ")
    if classType in classes:
        break

input("\n      press anything to continue \n")
sound3.stopSound()











p1 = Player(name,gender,classType,specialTitle) #spawns in daniel
playerParty = [p1]


p2 = Player("Danielle","F","Warrior","☆ ") #spawns in lucy
playerParty.append(p2)

print(p1.name)
print(p1.Class,p1.hp)
print(Skill.skills[0].get("name"))
#print(Item.id1.get("name"))
p1.exp = 100
print(p1.lvl)
p1.level_up()
print(p1.lvl)
print(p1.expCap)
p1.gain_exp(1200)
p2.gain_exp(1200)

for x in range(len(playerParty)): 
    print (playerParty[x].name),
    
playerParty = team.partySort_speed(playerParty)

for x in range(len(playerParty)): 
    print (playerParty[x].name),

p1.fullRecover()
p2.fullRecover()

p3 = Enemy("Goblin",5,"Weak ")
p3.enemyStatSet()
p4 = Enemy("Goblin",1,"Lil Bro ")
p4.enemyStatSet()
p5 = Enemy("Goblin",15,"Big Bro ")
p5.enemyStatSet()
p6 = Enemy("Orc",15,"Boss ")
p6.enemyStatSet()

p666 = Enemy("Jason",30,"Demon Slayer ")
p666.enemyStatSet()

sound = s('story')
sound2 = s('select')

enemyGroup = [p3]
enemyGroup2 = [p4,p5]
enemyGroup3 = [p6]
Jason = [p666]


color.write("______________________________________________________________________________________\n","SYNC")

print("max hp: ",p1.max_hp)
print("defence: ",p1.defence)
p1.equipGear(Item.items[2])
print("max hp: ",p1.max_hp)
print("defence: ",p1.defence)
p1.unequipGear('head')
print("max hp: ",p1.max_hp)
print("defence: ",p1.defence)


color.write("______________________________________________________________________________________\n","SYNC")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
sound.playSound(0.5)
print("walking in the fields...")
input("\n      press anything to continue \n")
print("whoah!")
sound.stopSound()
time.sleep(2)
Battle(playerParty,enemyGroup,'battle')
sound.playSound(0.5)
print("\n\n you find yourself at the entrance of a creepy cave...")
input("\n      press anything to continue \n")
sound.stopSound()
print("whoah!")
time.sleep(2)
cbattle = Battle(playerParty,enemyGroup2,'battle')
if cbattle == True:
    pass
elif cbattle == False:
    while True:
        print("Goblin Bros : Jajajjajajjajajajajajajajjajajajajajajajajjajajajajajajajajjajajajajajaj")
        time.sleep(0.2)


team.partyHeal(playerParty)

print("\n\n It's the end of the creepy cave...")
input("\n      press anything to continue \n")
print("It's the boss!")
time.sleep(2)
cbattle = Battle(playerParty,enemyGroup3,'boss')

if cbattle == True:
    pass
elif cbattle == False:
    while True:
        print("Orc : uguguguguguguguguuguguguguguguguguguguugugugugugugugugugu")
        time.sleep(0.2)

sound.playSound(0.5)

print("\n\n After finally defeating the goblins, you take a rest")
input("\n      press anything to continue \n")
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
sound.stopSound()
team.partyHeal(playerParty)
print("Jason has awoken")
time.sleep(2)
finalbattle = Battle(playerParty,Jason,'jason')

if cbattle == True:
    print("Jason has been defeated, but so has this demo")
    print("Thanks 4 playing")
elif cbattle == False:
    while True:
        print("Jason: Jajajjajajjajajajajajajajjajajajajajajajajjajajajajajajajajjajajajajajaj")
        time.sleep(0.2)
