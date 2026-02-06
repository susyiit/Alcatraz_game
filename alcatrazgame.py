
import random
import json

ART_TITLE= r"""                    
         ALCATRAZ  /__\         
       ____________|  |        
       |_|_|_|_|_|_|  |            
       |_|_|_|_|_|_|__|            
      A@\|_|_|_|_|_|/@@Aa          
   aaA@@@@@@@@@@@@@@@@@@@aaaA      
  A@@@@@@@@@@@DWB@@@@@@@@@@@@A 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
"""
ART_SKELETON= r"""       
           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------` """
ART_TROLL= r"""⠀⠀⠀⠀⠀⠀⠀⣠⢴⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⡄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠄⢇⠀⠀⠀⠀⣠⠒⡐⢂⠀⠀⠀⣸⠩⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡄⢠⠊⣙⠕⠁⠰⢀⣁⠼⡙⠕⡎⠢⢈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡄⣸⣰⢝⡎⠀⡆⠂⢐⣬⠉⢢⠈⣜⢪⣇⠠⢤⡀⠀
⠀⠀⠀⠀⡠⠋⠀⡔⠩⢿⠀⠘⢦⣀⡨⢟⣀⣸⠀⣟⠣⠕⠒⡀⢡⠀
⠀⠀⢀⢴⠁⠀⣜⡀⠀⠸⠀⠀⣀⢤⠒⣒⠺⠆⠀⡇⠀⢀⢤⠇⢀⡆
⡀⠀⣘⣵⢀⢠⡦⠇⠀⠀⡇⣬⣧⣆⣣⣋⣃⣸⣤⠁⠀⢸⣴⠀⠈⡹
⠻⡽⠭⢿⡟⢩⠁⠀⢀⡠⢗⠙⣉⣁⣒⡊⠒⡅⡎⠀⠀⠀⠑⠚⠚⠁
⠀⠈⡩⢋⠕⣉⠄⢊⢡⠔⠈⣇⠀⠀⠀⠀⢀⡇⠃⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢤⣭⡰⠬⠒⢁⠔⠈⠀⠈⠉⠉⠉⠁⠀⠑⠤⠁⢒⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠃⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⢀⠏⠀⠀⠀⠀
⠀⠀⠀⢀⣤⢤⠤⡃⠀⠱⠀⠀⠀⠀⠀⠀⢀⣜⠀⡠⢦⠠⣄⠀⠀⠀
⠀⠀⠀⠘⠣⠧⠤⠄⠀⠐⠁⠀⠀⠀⠀⠀⠘⠒⠒⠀⠘⠒⠛⠀⠀⠀"""
ART_GOBLIN= r"""           ,      ,
            /(.-""-.)\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\
      /       '----'       \ """
ART_ELF= r"""      -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//\
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ \
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) \
   / / / / |  |   |  |\  \  \ \
   / / // /|  |   |  |  \  \ \  VK
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
"""
ART_SWORD= r""" /| ________________
         O |===|* >________________>
                \|"""
ART_BOW= r"""(
    \
     )
##-------->
     )
    /
   ("""
ART_WAND= r"""
   * .  
 .  /  .
   /
  /
 /"""
ART_POT= r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠛⠛⠛⠛⠛⠛⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢻⡟⠛⠛⢻⡟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⡶⠾⠛⠛⠛⠿⢾⡇⠀⠀⢸⡷⠿⠛⠛⠛⠷⢶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣰⠟⠁⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠈⠻⣆⠀⠀⠀
⠀⠀⢰⡏⠀⠀⠀⣰⡿⠛⣩⣿⣿⣿⣆⣰⡟⣡⣾⣿⣿⣿⣆⠀⠀⠀⢹⡆⠀⠀
⠀⠀⢸⡇⠀⠀⢰⣿⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⢸⡇⠀⠀
⠀⠀⠘⣧⠀⠀⠸⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣼⠃⠀⠀
⠀⠀⠀⠹⣧⡀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢀⣼⠏⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣦⡀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⢀⣴⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢷⣄⠀⠈⠙⠿⣿⣿⠿⠋⠁⠀⣠⡾⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣄⠀⠈⠁⠀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣴⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

#             weapons

class weapon:
    def __init__(self,dmg,weapon_range,art):
        self.dmg = dmg
        self.weapon_range = weapon_range
        self.art = art
        
    def hit(self):
        return self.dmg
    
    def showart(self):
        print(self.art)

class sword(weapon):
    def __init__(self,dmg,weapon_range,art):
        super().__init__(dmg,weapon_range,art)
    
    def hit(self):
        crt = random.randint(1,5)
        if crt == 5:
            print("critical hit!!!")
            return self.dmg * 2
        else:
            return self.dmg
        
    def showart(self):
        super().showart()

    def block(self):
        pass

    def saytype(self):
        return "sword"
    
    def saystats(self):
        return f"{self.dmg} damage , {self.weapon_range} range"
        
class bow(weapon):
    def __init__(self,dmg,weapon_range,ammo,art):
        super().__init__(dmg,weapon_range,art)
        self.ammo = ammo
    
    def hit(self):
        if self.ammo > 0:
            self.ammo -= 1
            return self.dmg
        else:
            return 0
        
    def saytype(self):
        return "bow"
    
    def saystats(self):
        return f"{self.dmg} damage , {self.weapon_range} range ,{self.ammo} ammo"
    
    def addammo(self,amount):
        self.ammo += amount

    def showart(self):
        super().showart()
    
class wand(weapon):
    def __init__(self,dmg,weapon_range,manapower,art):
        super().__init__(dmg,weapon_range,art)
        self.manapower = manapower

    def hit(self):
        return super().hit()
    
    def heal(self):
        pass

    def saytype(self):
        return "wand"
     
    def saystats(self):
        return f"{self.dmg} damage , {self.weapon_range} range ,{self.manapower} mana"
    
    def showart(self):
        super().showart()
    
    def hpup(self):
        return self.manapower
    
    def saytype(self):
        return "wand"
    
    def decreasemana(self,a):
        self.manapower -= a

################ENEMİES#############

class enemy:
    def __init__(self,hp,dmg,name,erange,art):
        self.name   = name
        self.hp     = hp
        self.dmg    = dmg
        self.erange = erange
        self.art    = art
    
    def hit(self):
        return self.dmg

    def getdamage(self,a):
        self.hp -= a

    def sayname(self):
        return self.name
    
    def sayhp(self):
        return self.hp
    
    def showart(self):
        print(self.art)
    
class armored(enemy):
    def __init__(self,hp,dmg,armor,name,erange,art):
        super().__init__(hp,dmg,name,erange,art)
        self.armor = armor

    def hit(self):
        return super().hit()

    def getdamage(self,a):
        self.hp -= a // self.armor
        da = a - (a // self.armor)
        print(f"\n{da} damage absorbed by enemies armor")

    def sayname(self):
        return super().sayname()

    def sayhp(self):
        return super().sayhp()
    
    def showart(self):
        super().showart()

class rogue(enemy):
    def __init__(self,hp,dmg,name,erange,art):
        super().__init__(hp,dmg,name,erange,art)

    def hit(self):
        return super().hit()

    def getdamage(self,a):
        c = random.randint(1,10)
        if c <= 6:
            super().getdamage(a)
        else:
            print("\nenemy dodged your attack!")

    def sayname(self):
        return super().sayname()
    
    def sayhp(self):
        return super().sayhp()
    
    def showart(self):
        super().showart()
         
class arch(enemy):
    def __init__(self,hp,dmg,name,erange,eammo,art):
        super().__init__(hp,dmg,name,erange,art)
        self.eammo =eammo
    
    def hit(self):
        self.eammo -= 1
        if self.eammo < 0:
            print(f"{self.name} run out of ammo !")
            return 0
        else:
            return super().hit()
        
    def getdamage(self,a):
        super().getdamage(a)

    def sayname(self):
        return super().sayname()
    
    def sayhp(self):
        return super().sayhp()
    
    def showart(self):
        super().showart()

#                saving sytem

def save():
    global playerhp , playerweapon , enemydistance , ne1 , roomtype
    global newwp

    if ne1 == None:
        enemydistance = 0
        ne1hp         = 0
        ne1dmg        = 0
        ne1name       = "none"
        ne1erange     = 0
        ne1art        = "0"
        ne1extra      = 0
    else:
        ne1hp     = ne1.hp
        ne1dmg    = ne1.dmg
        ne1name   = ne1.name
        ne1erange = ne1.erange
        ne1art    = ne1.art

        if ne1.sayname() == "armored troll":
            ne1extra = ne1.armor
        elif ne1.sayname() == "elf":
            ne1extra = ne1.eammo
        else:
            ne1extra = 0

    if newwp == None:
        newwptype         = 0
        newwpdmg          = 0
        newwpweapon_range = 0
        newwpart          = 0
        newwpexx          = 0
    else:
        newwptype         = newwp.saytype()
        newwpdmg          = newwp.dmg
        newwpweapon_range = newwp.weapon_range
        newwpart          = newwp.art

        if newwp.saytype()=="wand":
            newwpexx = newwp.manapower
        elif newwp.saytype()=="bow":
            newwpexx = newwp.ammo
        else:
            newwpexx = 0

    if playerweapon.saytype()=="wand":
        playerweaponextra = playerweapon.manapower
    elif playerweapon.saytype()=="bow":
        playerweaponextra = playerweapon.ammo
    else:
        playerweaponextra = 0
    

    save_dosyası =[roomtype,
          playerhp,
          playerweapon.saytype(),
          playerweapon.dmg,
          playerweapon.weapon_range,
          playerweapon.art,
          enemydistance,
          ne1hp,
          ne1dmg,
          ne1name,
          ne1erange,
          ne1art,
          newwptype,
          newwpdmg,
          newwpweapon_range,
          newwpart,
          playerweaponextra,
          ne1extra,
          newwpexx
          ]
    
    try:
        with open("dungeonsave.txt","w") as file:
            json.dump(save_dosyası,file)
            print("saved!")
    except:
        print("saving eror")

def load():
    global playerhp
    global playerweapon
    global enemydistance
    global ne1
    global roomtype
    global newwp
    
    try:
        with open("dungeonsave.txt","r") as file:
            data = json.load(file)

        roomtype = data[0]
        playerhp = data[1]
        w_type = data[2]
        playerweapondmg = data[3]
        playerweaponweapon_range = data[4]
        playerweaponart = data[5]
        enemydistance = data[6]
        ne1hp = data[7]
        ne1dmg = data[8]
        ne1name = data[9]
        ne1erange = data[10]
        ne1art = data[11]
        newwpsaytype = data[12]
        newwpdmgg = data[13]
        newwprangee = data[14]
        newwpartt = data[15]
        playerweaponextra = data[16]
        ne1exxtr = data[17]
        newwpexx = data[18]

        if w_type == "sword":
            playerweapon = sword(playerweapondmg,playerweaponweapon_range,playerweaponart)
        elif w_type == "bow":
            playerweapon = bow(playerweapondmg,playerweaponweapon_range,playerweaponextra,playerweaponart)
        elif w_type == "wand":
            playerweapon = wand(playerweapondmg,playerweaponweapon_range,playerweaponextra,playerweaponart)
        
        
        if roomtype == "war":
            if warroom(ne1hp,ne1dmg,ne1name,ne1erange,ne1exxtr,ne1art) == 0:
                return 0

        elif roomtype == "treasure1":
            tr1()
        elif roomtype == "treasure2":
            tr2(newwpdmgg,newwprangee,newwpexx,newwpartt,newwpsaytype)
    except:
        print("load eror..")
        playerweapon = weapon(1,1,0)

#               rooms
def start():
    global playerweapon
   
    print(ART_TITLE)
    firstchoice = input("\nCHOOSE YOUR DESTINY:\n"
                        f"1-) SWORD {ART_SWORD}\n"
                        f"2-) BOW {ART_BOW}\n"
                        f"3-) WAND {ART_WAND}\n"
                        "4-) alredy have a save?\n"
                        "> ")

    if firstchoice== "1":
        playerweapon = sword(10,3,ART_SWORD)
    elif firstchoice == "2":
        playerweapon = bow(6,15,10,ART_BOW)
    elif firstchoice == "3":
        playerweapon = wand(4,10,20,ART_WAND)
    elif firstchoice == "4":
        if load() == 0:
            return 0
    else:
        print("\nyou choose fists???")
        playerweapon = weapon(1,1,0)

def warroom(enhp,endmg,enname,enrange,enex,enart):
    global playerhp
    global enemydistance
    global ne1
    if enhp == 0:
        c = random.randint(1,4)
        if c == 1:
            ne1= enemy(15,5,"skeleton",5,ART_SKELETON)
        elif c == 2:
            ne1= armored(15,5,2,"armored troll",1,ART_TROLL)
        elif c == 3:
            ne1= rogue(10,7,"goblin",3,ART_GOBLIN)
        elif c == 4:
            ne1= arch(10,7,"elf",10,5,ART_ELF)
    else:
        if enname == "skeleton":
            ne1 = enemy(enhp,endmg,enname,enrange,enart)
        elif enname == "armored troll":
            ne1 = armored(enhp,endmg,enex,enname,enrange,enart)
        elif enname == "goblin":
            ne1 = rogue(enhp,endmg,enname,enrange,enart)
        elif enname == "elf":
            ne1 = arch(enhp,endmg,enname,enrange,enex,enart)


    print(f"a {ne1.sayname()} appeared before you!")

    while True:
        ne1.showart()
        print(f'\n the {ne1.sayname()} have {ne1.sayhp()} hp, you have {playerhp} hp and {enemydistance} meters from enemy. \nyour range is {playerweapon.weapon_range} what will you do? \n 1-) attack\n 2-) step back\n 3-) step forward')
        if playerweapon.saytype() == "wand":
            print("4-) heath magic")
        action1 = input("0-) save and exit\n")
        if action1 == "2":
            enemydistance += 6
        elif action1 == "3":
            if enemydistance - 5 < 0:
                enemydistance = 0
                print(f"you step forward. now {enemydistance} meters btween you")
            else :
                enemydistance -= 5
                print(f"you step forward. now {enemydistance} meters btween you")
        elif action1 == "1":           #SALDIRI
            
            if playerweapon.weapon_range < enemydistance:
                print("you too far")
            else:     
                ndamage = playerweapon.hit()
                if ndamage == 0:
                    print("no ammo")
                else:    
                    ne1.getdamage(ndamage)
                    print(f'{ne1.sayname()} have {ne1.sayhp()} hp right now')
        elif action1 == "4":
            if playerweapon.saytype() == "wand":
                if playerweapon.manapower >= 5:
                    hpup= 5
                    playerweapon.decreasemana(hpup)
                    playerhp += hpup
                    print("hp up")
                else:
                    print(" not enough mana")
            else:
                pass
        elif action1 == "0":
            save()
            return 0
        else:
            print("you get paniced and cant do anything")

        if ne1.sayhp() <= 0:
            print(f"you defeated the {ne1.sayname()}")
            return 1

        # dusmanın sırası
        print(f"{ne1.sayname()}'s turn...\n")


        if enemydistance > ne1.erange: # adım atar

            if enemydistance - 5 <0:
                enemydistance = 0
                print(f"{ne1.sayname()} took a step towards you. now {enemydistance} meters btween you")
            else :
                enemydistance -= 5
                print(f"{ne1.sayname()} took a step towards you. now {enemydistance} meters btween you")
        else:   # saldırır
            hasar = ne1.hit()
            playerhp -= hasar
            print(f'{ne1.sayname()} hit you! now yor hp is {playerhp}')

        if playerhp <= 0:
            print("you die")
            return 0

def tr1():
    global roomtype
    global playerhp
    roomtype = "treasure1"
    if playerweapon.saytype() == "bow":
        ammo_amount = 10
        print(f"you found {ammo_amount} ammo")
        playerweapon.addammo(ammo_amount)
    print(ART_POT)
    ans = input("you found a healt pot! arent you drink it? \n 1-) yes \n 2-) no\n 0-) save and exit\n")
    if ans == "1":
        playerhp += 10
        print(f'your hp is {playerhp} now')
    elif ans == "0":
        save()
        return "save"
    else:
        print("you walkaway")
    
def tr2(nwdmg,nwrange,nwextra,nwart,nwtype):
    global roomtype
    global playerweapon
    global newwp
    roomtype = "treasure2"
    if nwtype == 0:
        wt = random.randint(1,3)
        if wt == 1:
            dg , rang = random.randint(5,15) , random.randint(1,5)
            newwp = sword(dg,rang,ART_SWORD)
        elif wt ==2 :
            dg , rang , am =random.randint(3,8),random.randint(7,15) , random.randint(3,20)
            newwp = bow(dg,rang,am,ART_BOW)
        elif wt == 3:
            dg,rang,mana = random.randint(3,7),random.randint(5,15),random.randint(10,50)
            newwp = wand(dg,rang,mana,ART_WAND)
    elif nwtype == "sword":
        newwp = sword(nwdmg,nwrange,nwart)
    elif nwtype == "bow":
        newwp = bow(nwdmg,nwrange,nwextra,nwart)
    elif nwtype == "wand":
        newwp = wand(nwdmg,nwrange,nwextra,nwart)
    newwp.showart()
    print(f"there is a {newwp.saytype()}!! \n it has {newwp.saystats()}")
    nee = input(f"arent you take it?\n(your weapons stats {playerweapon.saystats()})\n 1-) yes \n 2-) no\n 0-) save and exit\n")
    if nee == "1":
        playerweapon = newwp
    elif nee == "0":
        save()
        return "save"
    else:
        print("you walked away")

def treasureroom():
    global playerhp
    global playerweapon
    global newwp
    treasure = random.randint(1,5)
    if treasure > 2:
        a = tr1()
        if a == "save":
            return a
    elif treasure <= 2:
        a = tr2(0,0,0,0,0)
        if a == "save":
            return a
        

#             ROOM SELECTOR


while True:
    playerhp = 20
    playerweapon = None
    enemydistance = 10
    roomtype = "start"
    newwp = None
    ne1 = None
    
    if start() == 0:
        break
    while True:
        nr = random.randint(1,10)
        if nr > 4:
            enemydistance = random.randint(0,10)
            ne1 = None
            roomtype = "war"
            print("you entered a dark room, there is some bad noises..")
            print("------------------------------------------------------------------------------------")
            afterwar= warroom(0,1,1,1,1,1)
            if afterwar == 1:
                pass
            else:
                break
        elif nr <= 4:
            print("\nyou entered a treasure room")
            print("-----------------------------------------------------------------------------------")
            b = treasureroom()
            if b == "save":
                break


    print("      GAME OVER !      ")
    pa = input("press 1 and play again")
    if pa == "1":
        pass
    else:
        break

    
            


    