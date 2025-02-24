import pygame
from random import randint
#muzyczka
from pygame import mixer
bg_music = "Tomb.mp3"
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound("bg_music.mp3"), -1)
pygame.init() 
window = pygame.display.set_mode((1280,720))
left = pygame.mouse.get_pressed()[0]
level = 1
class Button_play:
    def __init__(self):
        self.image= pygame.image.load("play_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 490
        self.y_cord = 200
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_training:
    def __init__(self):
        self.image= pygame.image.load("training_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 490
        self.y_cord = 375
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_exit:
    def __init__(self):
        self.image= pygame.image.load("EXIT.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 1000
        self.y_cord = 600
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))

class Button_armour:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 90
        self.y_cord = 150
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_leggins:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 490
        self.y_cord = 150
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_boots:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 890
        self.y_cord = 150
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_helmet:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 90
        self.y_cord = 425
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))

class Button_sword:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 490
        self.y_cord = 425
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Button_bow:
    def __init__(self):
        self.image= pygame.image.load("buy_button.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 890
        self.y_cord = 425
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def tick(self):    
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))


class Player: 
    def __init__(self):
        self.isjump = False
        self.x_cord = 10
        self.y_cord = 0
        self.image= pygame.image.load("player_r.png")
        self.direction = '#'
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hp_img = pygame.image.load("hp/10hp.png")
        self.attack = 10
        self.armour = 0
        self.at_spd = 0.6
        
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord+92, self.width, 7)
        self.head= pygame.Rect(self.x_cord, self.y_cord, self.width, 7)
        self.body = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+9, self.width-60, self.height-18)
        self.right = pygame.Rect(self.x_cord + 60, self.y_cord+9, self.width-60, self.height-18)
        
        
    def tick(self,keys): 
        if self.hp>=10:
            self.hp_img=pygame.image.load("hp/1hp.png")
        if self.hp>=20:
            self.hp_img=pygame.image.load("hp/2hp.png")
        if self.hp>=30:
            self.hp_img=pygame.image.load("hp/3hp.png")
        if self.hp>=40:
            self.hp_img=pygame.image.load("hp/4hp.png")
        if self.hp>=50:
            self.hp_img=pygame.image.load("hp/5hp.png")
        if self.hp>=60:
            self.hp_img=pygame.image.load("hp/6hp.png")
        if self.hp>=70:
            self.hp_img=pygame.image.load("hp/7hp.png")
        if self.hp>=80:
            self.hp_img=pygame.image.load("hp/8hp.png")
        if self.hp>=90:
            self.hp_img=pygame.image.load("hp/9hp.png")
        if self.hp>=100:
            self.hp_img=pygame.image.load("hp/10hp.png")
        if self.direction=='r':
            self.image=pygame.image.load("player_r.png")
        else:
            self.image=pygame.image.load("player_l.png")
            
        
        
    

        self.head= pygame.Rect(self.x_cord, self.y_cord, self.width, 7)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord+self.height-7, self.width, 10)
        self.body = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+9, self.width-60, self.height-18)
        self.right = pygame.Rect(self.x_cord + 60, self.y_cord+9, self.width-60, self.height-18)
        
    def draw(self): 
        window.blit(self.image,(self.x_cord, self.y_cord))
        window.blit(self.hp_img,(0, 0))



class Floor:
    def __init__(self, a, b, c):
        
        self.x_cord=b
        self.y_cord=a
        self.width=c
    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, 10)
    def draw(self):
        pygame.draw.rect(window, (130, 130, 130), pygame.Rect(self.x_cord, self.y_cord, self.width, 10))
class Wall:
    def __init__(self, y, x, h):
        
        self.x_cord=x
        self.y_cord=y
        self.heigth=h
    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, (self.y_cord)-(self.heigth)+10, 10, self.heigth)
        self.top = pygame.Rect(self.x_cord, (self.y_cord)-(self.heigth), 10, 10)
    def draw(self):
        pygame.draw.rect(window, (135, 130, 130), pygame.Rect(self.x_cord, (self.y_cord)-(self.heigth), 10, self.heigth))

class Chest:
    def __init__(self, y, x):
        
        self.image= pygame.image.load("chest.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x-self.width
        self.y_cord = y-self.height
        
        
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class achievement:
    def __init__(self, y, x, achievement):
        
        self.image= pygame.image.load(achievement)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x
        self.y_cord = y
        
        
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
    

class Zombie:
    def __init__(self, y, x,img):
        
        self.image= pygame.image.load(img)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x - self.width
        self.y_cord = y - self.height
        self.hp = 100 #robot
        self.at_spd = 0.8-0.05*level
        self.at_dmg=10+level
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)

    def tick(self):   
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)
    def draw(self):
        color=(57, 252, 3)
        if self.hp<80:
            color=(252, 248, 3)
        if self.hp<50:
            color=(252, 161, 3)
        if self.hp<30:
            color=(252, 44, 3)
        window.blit(self.image,(self.x_cord, self.y_cord))
        pygame.draw.rect(window, color, pygame.Rect(self.x_cord, self.y_cord-20, self.hp*(self.width/100), 10))

class BOSS:
    def __init__(self, y, x, img):
        
        self.image= pygame.image.load(img)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x - self.width
        self.y_cord = y - self.height
        self.hp = 150
        self.at_spd = 0.7-0.05*level
        self.at_dmg=13+level
        
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)

        
    def tick(self):   
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)

    def draw(self):
        color=(57, 252, 3)
        if self.hp<110:
            color=(252, 248, 3)
        if self.hp<70:
            color=(252, 161, 3)
        if self.hp<30:
            color=(252, 44, 3)
        window.blit(self.image,(self.x_cord, self.y_cord))
        pygame.draw.rect(window, color, pygame.Rect(self.x_cord, self.y_cord-20, self.hp*(self.width/150), 10))
class BOSS_LAST:
    def __init__(self, y, x, img):
        
        self.image= pygame.image.load(img)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x - self.width
        self.y_cord = y - self.height
        self.hp = 200
        self.at_spd = 0.3
        self.at_dmg= 20

        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)

        
    def tick(self):   
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.left = pygame.Rect(self.x_cord, self.y_cord+8, 5, self.height-16)
        self.right = pygame.Rect(self.x_cord + self.width-5, self.y_cord+8, 5, self.height-16)
        self.feet = pygame.Rect(self.x_cord, self.y_cord + self.height-5, self.width, 5)
        self.top= pygame.Rect(self.x_cord, self.y_cord, self.width, 5)

    def draw(self):
        color=(57, 252, 3)
        if self.hp<1500:
            color=(252, 248, 3)
        if self.hp<100:
            color=(252, 161, 3)
        if self.hp<50:
            color=(252, 44, 3)
        window.blit(self.image,(self.x_cord, self.y_cord))
        pygame.draw.rect(window, color, pygame.Rect(self.x_cord, self.y_cord-20, self.hp*(self.width/150), 10))
class arrow:
    def __init__(self, y, x, q):
        
        
        
        self.image= pygame.image.load("arrow_r.png")
        self.x_cord = x
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        if q=='l':
            self.x_cord = x-self.width
            self.image= pygame.image.load("arrow_l.png")
            

        self.y_cord = y-self.height
        self.direction = q
        
    def tick(self):
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Portal:
    def __init__(self, x, y):
        self.image= pygame.image.load("portal.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x
        self.y_cord = y-self.height
        
    def tick(self):
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
class Grave:
    def __init__(self, y, x):
        self.image= pygame.image.load("grave.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = x
        self.y_cord = y+self.height+20
        
        self.hitbox= pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    def draw(self):
         window.blit(self.image,(self.x_cord, self.y_cord))
    
def main():
    v=0                     #skok
    player=Player()     #gracz
    max_hp_player = 100 #maksymalne życie
    run = True      #czy gra trwa
    game = False    #czy gra trwa
    button_p = Button_play() #przycisk play
    button_t = Button_training() #przycisk train
    armour = Button_armour()
    leggins = Button_leggins()
    boots = Button_boots()
    helmet = Button_helmet()
    sword = Button_sword()
    bow = Button_bow()
    button_exit=Button_exit()
    
    player.hp=100   #życie gracza(startowe)
    clock = 0       #czas gracz
    clock_z = 0     #czas zombie
    clock_b = 0 # czas BOSS
    score =0        #wynik
    floor = []      # lista z podłoga
    graves = [] #lista grobów
    d=False  #czy spadek
    fly = False # czy leci strzała
    walls=[]    #lista ze scianami
    chests=[]   #lista ze skrzynkami
    zombies=[]  #lista z zombi
    arrows = [] #lista strzał
    skeleton_arrows=[]
    arrow_at_spd = 0.75 #szybkość ataku strzał
    Bosses=[] #lista bossów
    buttons = [] #lista przycisków
    money=0    #pieniądze
    portals=[] #lista portali
    z_speed = 5 #szybkość zombie
    b_speed = 7 #szybkość Bossa
    speed=15 #szybkość gracza
    speed_a = 20 # szybkość strzały
    a=1      #szybkość spadku
    life_z = 0 #życie zombie na poziomie
    color_red = (255,0,0)   #kolor czerwony
    color_green = (0,255,0) #kolor zielony
    shop = False    #czy sklep
    arrow_attack = 8 #atak strzały
    jump = 17       #skok
    money_armour = 80 #początkowa cena napierśnika
    money_leggins = 80 #początkowa cena spodni
    money_boots = 80 #początkowa cena butów
    money_helmet = 80   #początkowa cena hełmu
    money_sword = 80    #początkowa cena miecza
    money_bow = 80  #początkowa cena łuku
    armour_armour = 0.05 #podstawowe do kupowania
    leggins_at_spd = 0.04 #podstawowe do kupowania
    boots_speed = 2 #podstawowe do kupowania
    helmet_bow_at_spd = 0.04 #podstawowe do kupowania
    sword_attack = 2 #podstawowe do kupowania
    bow_attack = 2  #podstawowe do kupowania
    clicked_button_p = False    #czy clicknięty
    
    training = False #czy w trybie trening
    killed_zombies = 0 #zabite zombie
    ghost_level = False #level ghost
    skeleton_level = False #level skeleton
    vampire_level = False #level vampire
    zombie_level = False #level zombie
    mumia_level = False #level mumia
    last_level = False  # ostatni level
    achievements = []   # achievementy
    portal_appear = False   #czy portal się pojawił
    level_complete = "ingame" #czy się level skonczył
    armour_times = 0 #ile razy kupione
    leggins_times = 0 #ile razy kupione
    boots_times = 0 #ile razy kupione
    helmet_times = 0 #ile razy kupione
    sword_times = 0 #ile razy kupione
    bow_times = 0   #ile razy kupione
    spawn = False   #do spawnowania drugich zombie
    spawn_2 = False #do spawnowania drugich zombie
    tomb=[]#fake skrzynie
    level=1

    
    
                
    
    
    
    

    font=pygame.font.Font('minecraft_font.ttf', 24)
    font_big=pygame.font.Font('minecraft_font.ttf', 100)
    text = font.render("Hello, World", True, (0, 128, 0))
    
    background = pygame.image.load("bg.png") #tło
    
    
    
    
    

    
    
    #dopóki gra
    while run:
        time=pygame.time.Clock().tick(60)/900
        clock += time #czas gracza
        clock_z += time
        clock_b += time
        pygame.time.Clock().tick(60) 

        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
        keys= pygame.key.get_pressed()
        position = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        #jeżeli gramy
        if game and level_complete == "ingame" or training and level_complete == "ingame":
            player.tick(keys)

        

        money_image  = font.render(f"Money: {money}", True, (255, 214, 8)) #wynik
        shop_image = font_big.render("SKLEP", True, (255, 214, 8))   #tytuł
        title = font_big.render("DUNGEON BUSTER", True, (255, 214, 8))   #tytuł
        armour_image = font.render(f"ARMOUR  +{int(armour_armour*100)}" "% armour", True, (255, 214, 8))
        leggins_image = font.render(f"LEGGINS  +{int(leggins_at_spd*100)}""% attack speed", True, (255, 214, 8))
        boots_image = font.render(f"BOOTS  +{boots_speed}"" speed", True, (255, 214, 8))
        helmet_image = font.render(f"HELMET  +{int(helmet_bow_at_spd*100)}" "% bow attack speed", True, (255, 214, 8))
        sword_image = font.render(f"SWORD  +{sword_attack}"" attack", True, (255, 214, 8))
        bow_image = font.render(f"BOW  +{bow_attack}"" arrow attack", True, (255, 214, 8))
        money_armour_image = font.render(f"Cost: {money_armour}", True, (255, 214, 8))
        money_leggins_image = font.render(f"Cost: {money_leggins}", True, (255, 214, 8))
        money_boots_image = font.render(f"Cost: {money_boots}", True, (255, 214, 8))
        money_helmet_image = font.render(f"Cost: {money_helmet}", True, (255, 214, 8))
        money_sword_image = font.render(f"Cost: {money_sword}", True, (255, 214, 8))
        money_bow_image = font.render(f"Cost: {money_bow}", True, (255, 214, 8))
        
        killed_zombies_image = font.render(f"KILLED MONSTERS: {killed_zombies}", True, (255, 214, 8)) #zabite zombie
        
        
        
                
        #pokazywanie menu głównego
        
        window.blit(background,(0,0))
        window.blit(title,(150,50))
        #button działanie
        Button_play.draw(button_p)
        
        
        
        if button_p.hitbox.collidepoint(position) and left_click and game == False and clicked_button_p == False and shop == False:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("Tomb.mp3"), -1)
            skeleton_level = True
            clicked_button_p = True
            game = True
            
            level = 1
            
            floor.append(Floor(240, 0, 1000))
            floor.append(Floor(480, 280, 1000))
            floor.append(Floor(710, 0, 1280))
            floor.append(Floor(0, 0, 1280))
            floor.append(Floor(360, 1150, 180))
            floor.append(Floor(600, 0, 150))
            zombies.append(Zombie(240,600, "skeleton.png"))
            chests.append(Chest(360,1250))
            chests.append(Chest(600,100))
            player.x_cord = 0
            player.y_cord = 10
            killed_zombies = 0
            z_speed = 5
            b_speed = 7
        
            
                
        if training:
            window.blit(background,(0,0))
            window.blit(killed_zombies_image,(950,5))
            for xd in zombies:
                xd.draw()
                xd.tick()
                if xd.hp <= 0:
                    zombies.remove(xd)
                    clock_z = 0
                    xd.hp = 100
                    z_speed += level
                    level += 1
                    
                    

        if game:
            #pokazywanie obiektów
            window.blit(background,(0,0))
            window.blit(money_image,(1000,5))
        #kiedy sklep
        if shop:
            
            window.blit(background,(0,0))
            window.blit(money_image,(1000,5))
            window.blit(shop_image,(400,0))
            Button_armour.draw(armour)
            Button_leggins.draw(leggins)
            Button_boots.draw(boots)
            Button_helmet.draw(helmet)
            Button_sword.draw(sword)
            Button_bow.draw(bow)
            window.blit(armour_image,(90,120))
            window.blit(leggins_image,(460,120))
            window.blit(boots_image,(890,120))
            window.blit(helmet_image,(40,395))
            window.blit(sword_image,(490,395))
            window.blit(bow_image,(890,395))
            window.blit(money_armour_image,(90,300))
            window.blit(money_leggins_image,(460,300))
            window.blit(money_boots_image,(890,300))
            window.blit(money_helmet_image,(40,575))
            window.blit(money_sword_image,(490,575))
            window.blit(money_bow_image,(890,575))
            button_exit.draw()
            
            #tworzenie levelu 2
        if level == 2:
               
               zombie_level = True
               if button_exit.hitbox.collidepoint(position) and left_click and shop:
                    player.hp = max_hp_player
                    shop = False
                    level_complete = "ingame"
                    game = True
                    
                    floor.append(Floor(120, 0, 200))
                    floor.append(Floor(480, 1050, 200))
                    floor.append(Floor(710, 0, 1280))
                    floor.append(Floor(0, 0, 1280))
                    floor.append(Floor(360, 400, 550))
                    floor.append(Floor(580, 300, 700))
                    floor.append(Floor(240, 75, 200))
                    zombies.append(Zombie(360,600, "zombie.png"))
                    zombies.append(Zombie(360,800, "zombie.png"))
                    
                    chests.append(Chest(240,175))
                    chests.append(Chest(480,1200))
                    player.x_cord = 0
                    player.y_cord = 10
        if level == 3:
               
               ghost_level = True
               if button_exit.hitbox.collidepoint(position) and left_click and shop:
                    player.hp = max_hp_player
                    shop = False
                    
                    level_complete = "ingame"
                    game = True
                    
                    floor.append(Floor(400, 0, 1280))
                    floor.append(Floor(200, 0, 200))
                    floor.append(Floor(200, 300, 1000))
                    walls.append(Wall(400, 300, 75))
                    walls.append(Wall(400, 600, 75))
                    zombies.append(Zombie(300,900, "ghost.png"))
                    
                    chests.append(Chest(400,1200))
                    player.x_cord = 0
                    player.y_cord = 10
        if level == 4:
               
               skeleton_level=True
               
               if button_exit.hitbox.collidepoint(position) and left_click and shop:
                    player.hp = max_hp_player
                    shop = False
                    
                    level_complete = "ingame"
                    game = True
                    
                    
                    zombies.append(Zombie(550,900, "BOSS_s.png"))
                    zombies[-1].hp+=50
                    floor.append(Floor(600, 0, 1280))
                    floor.append(Floor(710, 0, 1280))
                    floor.append(Floor(0, 0, 1280))
                    floor.append(Floor(360, 1150, 180))
                    floor.append(Floor(480, 900, 180))
                    floor.append(Floor(360, 700, 180))
                    floor.append(Floor(240, 500, 180))
                    floor.append(Floor(120, 700, 180))
                    chests.append(Chest(480,900))
                    chests.append(Chest(360,1200))
                    player.x_cord = 500
                    player.y_cord = 100
        
       
        if armour.hitbox.collidepoint(position) and left_click and money >= money_armour and armour_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            armour_times += 1
            money -= money_armour
            money_armour += 40 + 10*armour_times
            player.armour  += armour_armour
            armour_armour += 0.05
                
                
        if leggins.hitbox.collidepoint(position) and left_click and money >= money_leggins and leggins_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            leggins_times += 1
            money -= money_leggins
            money_leggins += 20 + 10*leggins_times
            player.at_spd -= leggins_at_spd
            leggins_at_spd += 0.03
            

                #kupowanie butów
        if boots.hitbox.collidepoint(position) and left_click and money >= money_boots and boots_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            boots_times += 1
            money -= money_boots
            money_boots += 20 + 10*boots_times
            speed += boots_speed
            boots_speed += 2
                
                #kupowanie hełmu
        if helmet.hitbox.collidepoint(position) and left_click and money >= money_helmet and helmet_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            helmet_times += 1
            money -= money_helmet
            money_helmet += 20 + 10*helmet_times
            arrow_at_spd -= helmet_bow_at_spd
            helmet_bow_at_spd += 0.03
                
                #kupowanie mieczu
        if sword.hitbox.collidepoint(position) and left_click and money >= money_sword and sword_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            sword_times += 1
            money -= money_sword
            money_sword += 30 + 10*sword_times
            player.attack += sword_attack
            sword_attack += 2
                
               #kupowanie łuku 
        if bow.hitbox.collidepoint(position) and left_click and money >= money_bow and bow_times <=6 and shop:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("buy.mp3"), 0)
            bow_times += 1
            money -= money_bow
            money_bow += 30 + 10*bow_times
            arrow_attack += bow_attack
            bow_attack += 2

        
            
              
        #tworzenie strzał
        if keys[pygame.K_s] and clock > arrow_at_spd:
            clock = 0
            direction='r'
            for xd in zombies:
                if xd.x_cord<player.x_cord:
                    direction='l'
                    arrows.append(arrow(player.y_cord + 45, player.x_cord, direction))
                else:
                    arrows.append(arrow(player.y_cord + 45, player.x_cord, direction))
            
        for xd in arrows:
            xd.draw()
            xd.tick()
        for xd in graves:
            xd.draw()
        for xd in zombies:
            
            xd.draw()
            xd.tick()
            #atak gracza i zombie
            
                
                    
            if player.body.colliderect(xd.hitbox):
                if  keys[pygame.K_q] and clock > player.at_spd:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("attackp.mp3"), 0)
                    clock = 0
                    xd.hp -= player.attack+10
            if clock_z > xd.at_spd:
                if clock_z < xd.at_spd + 0.5:
                    if player.body.colliderect(xd.hitbox) and skeleton_level == False:
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound("attackz.mp3"), 0)
                        clock_z = 0
                        player.hp -= round(xd.at_dmg *(1-player.armour),(1))
                    #tworzenie strzał skeleton
                    if skeleton_level:
                        clock_z = 0
                        direction='l'
                        if xd.x_cord<player.x_cord:
                            direction='r'
                            skeleton_arrows.append(arrow(xd.y_cord + 45, xd.x_cord-xd.width, direction))
                        else:
                            skeleton_arrows.append(arrow(xd.y_cord + 45, xd.x_cord+xd.width, direction))
                        
                else:
                    clock_z = 0
            else:
                if skeleton_level == False:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound("zombie_growl.mp3"), 1)
                

            c, e=True, True
            
            #działanie podłogi, chodzenia i spadku zombie
            for aaa in walls:
                aaa.tick()
                if aaa.hitbox.colliderect(xd.left):
                    c=False
                if aaa.hitbox.colliderect(xd.right):
                    e=False
            for aaa in floor:
                aaa.tick()
                if aaa.hitbox.colliderect(xd.left):
                    e=False
                if aaa.hitbox.colliderect(xd.right):
                    c=False
            
            if level==(3 or 5):
                c, e =True, True
            if  c:
                if xd.x_cord<player.x_cord:
                    xd.x_cord+=z_speed
            if e:
                if xd.x_cord>player.x_cord:
                    xd.x_cord-=z_speed
            
                
         
        
            d=True
            f= True
            
            for aaa in floor:
                aaa.tick()                     
                if aaa.hitbox.colliderect(xd.top):
                    f = False
                if aaa.hitbox.colliderect(xd.feet):
                    d=False
                
                
            if d:
                xd.y_cord+=z_speed
                
            #śmierć zombie  
            if xd.hp <= 0:
                zombies.remove(xd)
                graves.append(Grave(xd.y_cord, xd.x_cord))
                money+=randint(50, 70)+10*level
                clock_z = 0
                killed_zombies+=1
                if level==1 or killed_zombies==3: #level 2
                    
                    portals.append(Portal(1190,710))
                if level==3:
                    portals.append(Portal(1190,400))
                if level==4:
                    portals.append(Portal(700,120))
                
                
                    
                    
                
                
                if training == False:
                    life_z += 1
                
            if killed_zombies==5:
                while(True):
                    window.blit(pygame.image.load("win.png"), (0, 0))
                    
                
            #śmierć gracza
            if player.hp <= 0:
                
                training = False
                game = False
                level =1
                portals=[]
                floor=[]
                walls=[]
                chests=[]
                zombies = []
                Bosses = []
                graves =[]
                clock = 0
                achievements.append(achievement(0,0,"game_over.png"))
                level_complete = "game_over"
                clicked_button_p == False
                attack_zombie_image = pygame.draw.rect(window, color_red, pygame.Rect(player.x_cord+10, (player.y_cord)-7, 0, 0))
                
        #regeneracja
        if zombies == [] and Bosses == []: 
            if player.hp < max_hp_player:
                if clock > 0.5:
                    clock = 0
                    player.hp +=10
        for aaa in arrows:
            arrow_number=len(arrows)
            aaa.tick()
            for xd in walls:
                if aaa.hitbox.colliderect(xd.hitbox):
                    arrows.remove(aaa)
            for xd in zombies:
                if aaa.hitbox.colliderect(xd.hitbox)and not ghost_level:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound("arrow_shoot.mp3"), 0)
                        xd.hp = xd.hp - arrow_attack
                        if len(arrows)==arrow_number:
                            arrows.remove(aaa)
            if aaa.direction == 'l':
                    aaa.x_cord -= speed_a
            elif aaa.direction == 'r':
                    aaa.x_cord += speed_a
                        
            if aaa.x_cord < 0 or aaa.x_cord > 1280:
                            arrows.remove(aaa)
        
        if skeleton_level:
            for aaa in skeleton_arrows:
                aaa.tick()
                aaa.draw()
                if aaa.hitbox.colliderect(player.body):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("arrow_shoot.mp3"), 0)
                    player.hp = player.hp - arrow_attack
                    skeleton_arrows.remove(aaa)
                if aaa.direction == 'l':
                    
                    aaa.x_cord -= speed_a
                elif aaa.direction == 'r':
                    
                    aaa.x_cord += speed_a
        
                    
        #działanie skrzyń            
        for xd in chests:
            xd.draw()
            if player.body.colliderect(xd.hitbox):
                chests.remove(xd)
                money+=randint(30, 50)+10*level
                
        d=True
        #działanie portalu
        for xd in portals:
            xd.draw()
            xd.tick()
            if player.body.colliderect(xd.hitbox):
                z_speed += level
                b_speed += level
                level+=1
                floor=[]
                walls=[]
                chests=[]
                Bosses = []
                graves =[]
                skeleton_level=False
                ghost_level=False
                zombie_level=False
                level_complete = "achievement"
                if level > 1:
                    portals = []
                    game = False
                    shop=True
                    
                
        for xd in achievements:
            xd.draw()
            if level_complete == "achievement" and clock > 0.75:
                achievements = []
                shop = True
                skeleton_level = False
                vampire_level = False
                zombie_level = False
                mumia_level = False
                last_level = False
                ghost_level = False
                game = False
            if level_complete == "game_over" and clock > 0.5:
                game = False
                achievements =[]
                ghost_level = False
                skeleton_level =False
                vampire_level = False
                zombie_level = False
                mumia_level = False
                last_level = False
                
            
        for xd in floor:
            xd.draw()
            xd.tick()
        #skakanie    
        if player.isjump == False:
            if keys[pygame.K_w]:
                player.isjump = True
        #działanie ściany gracz
        for xd in walls:
            xd.draw()
            xd.tick()
            if player.hitbox.colliderect(xd.top):
                v=0
                d=False
                player.isjump=False
        
        


        
        
        
        #działanie podłogi
        for xd in floor:
            
            if player.hitbox.colliderect(xd.hitbox):
                v=0
                d=False
                player.isjump=False
            if player.head.colliderect(xd.hitbox):
                v=10

       
                
        #chodzenie i skakanie gracz
        if keys[pygame.K_w] and not player.isjump:
            player.isjump=True
            v = -jump
        if keys[pygame.K_a] and player.x_cord>0:
            q=True
            for xd in walls:
                xd.tick()
                
                if player.left.colliderect(xd.hitbox):
                    if last_level:
                        q = True
                    else:
                        q=False
            for xd in floor:
                xd.tick()
                if player.left.colliderect(xd.hitbox):
                        q=False
               
            if q:
                player.x_cord -= speed
                player.direction='l'
            
            
        if keys[pygame.K_d] and player.x_cord<1280-player.width:
            q=True
            for xd in walls:
                xd.tick()
                if player.right.colliderect(xd.hitbox):
                    if last_level:
                        q = True
                    else:
                        q=False
            for xd in floor:
                xd.tick()
                if player.right.colliderect(xd.hitbox):
                        q=False
            if q:
                player.x_cord += speed
                player.direction='r'
        if d or player.isjump:
            if v<=10:
                v+=a
        
            
            player.y_cord+=v
        if game and level_complete == "ingame" or training and level_complete == "ingame":
            player.draw()
        
        pygame.display.update()
        

    print(score)
        
if __name__== "__main__":
    main()
