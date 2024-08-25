import pygame #підключення бібліотеки pygame
pygame.init()

back = (50, 45, 50) #створення кольору для головного вікна
mw = pygame.display.set_mode((1000, 750)) #створення головного вікна
mw.fill(back) #заповнення головного вікна
clock = pygame.time.Clock() #створення таймера
bd_image = pygame.image.load('fonn.png')

class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect() # "межі" персонажа
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
        self.gravity = 0.5 #гравітація (швидкість падіння вниз)
        self.jump_power = -13 #величина стрибка
        self.vel_y = 0 #швидкість руху в стрибку
        self.direction = "right"

    def move(self):
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.vel_y > 0:
                    self.rect.bottom = w.rect.top
                    self.vel_y = 0
                    self.can_jump = True
                elif self.vel_y < 0:
                    self.rect.top = w.rect.bottom
                    self.vel_y = 0

    def jump(self):
        if self.can_jump:
            self.vel_y = self.jump_power
            self.can_jump = False

    
    
    def enemy_move(self):
        if self.rect.x < 300:
            self.direction = "right"
        elif self.rect.x > 700:
            self.direction = "left"

        if self.direction == "right":
            self.rect.x += 5
        else:
            self.rect.x -= 5




class Wall:
    def __init__(self, x, y, width, height, color=(22, 26, 31)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(mw, self.color, self.rect)

walls = [Wall(0,550,1000,300), # 1 lvl
         Wall(150,400,50,200),
         Wall(300,300,50,300),
         Wall(450,200,100,400),
         Wall(650,300,50,300),
         Wall(800,400,50,200),
         Wall(-50,0,50,750),
         Wall(0,-50,1000,50),
         Wall(0,750,1000,50),
         Wall(1000,0,100,1000)]
shap = Player(1000,1000,200,50,'sharp1.png')
shap1 = Player(1000,1000,200,50,'sharp1.png')
sharp = Player(350, 500, 100, 50, 'sharp.png')
sharp1 = Player(550, 500, 100, 50, 'sharp.png')
player = Player(100, 100, 50, 50, 'ball.png')
coin = Player(470, 150, 50, 50, 'coin.png')
coin1 = Player(220, 500, 50, 50, 'coin.png')
coin2 = Player(720, 500, 50, 50, 'coin.png')
coin3 = Player(1000,1000, 50, 50, 'coin.png')
coin4 = Player(1000,1000, 50, 50, 'coin.png')
door = Player(1000,1000, 121, 121, 'door.png')
wrag = Player(1000,1000,100,100, 'wrag.png')





move_left = False
move_right = False

level1 = True
level2 = False
level3 = False
coins = 0
game = True
while game: #створення головного циклу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN: # якщо натиснута клавіша
            if event.key == pygame.K_d: # якщо клавіша "праворуч"
                move_right = True
            if event.key == pygame.K_a: # якщо клавіша "ліворуч"
                move_left = True

            if event.key == pygame.K_w:

                player.jump()

        elif event.type == pygame.KEYUP: # якщо клавіша відпущена
            if event.key == pygame.K_d: # якщо клавіша "праворуч"
                move_right = False
            if event.key == pygame.K_a: # якщо клавіша "ліворуч"
                move_left = False

        
        

    player.move()

    if move_right:
        player.rect.x += 3
    if move_left:
        player.rect.x -= 3

    if move_right:
        player.rect.x += 3
        for w in walls:
            if player.rect.colliderect(w.rect):
                player.rect.right = w.rect.left  # змінюємо позицію гравця, щоб він не міг пройти крізь стіну
    if move_left:
        player.rect.x -= 3
        for w in walls:
            if player.rect.colliderect(w.rect):
                player.rect.left = w.rect.right  # змінюємо позицію гравця, щоб він не міг пройти крізь стіну
    mw.blit(bd_image, (0,0)) #заповнення головного вікна

    if level1:
        if player.rect.colliderect(sharp.rect):
            player.rect.x, player.rect.y = 50, 450

        if player.rect.colliderect(sharp1.rect):
            player.rect.x, player.rect.y = 50, 450

        if player.rect.colliderect(coin.rect):
            coin.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin1.rect):
            coin1.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin2.rect):
            coin2.rect.x = 2000
            coins += 1
        mw.blit(player.image, (player.rect.x, player.rect.y))
        mw.blit(coin.image, (coin.rect.x, coin.rect.y))
        mw.blit(coin1.image, (coin1.rect.x, coin1.rect.y))
        mw.blit(coin2.image, (coin2.rect.x, coin2.rect.y))
        mw.blit(sharp.image, (sharp.rect.x, sharp.rect.y))
        mw.blit(sharp1.image, (sharp1.rect.x, sharp1.rect.y))
        if coins == 3:
            walls.pop(9)
            coins = 0
        if player.rect.x > 1000: # настройки для lvl 2
            player.rect.x = 50
            player.rect.y = 400
            player.vel_y = 0
            player.can_jump = True
            walls = [Wall(0,550,1000,300), # 2 lvl
                     Wall(200,400,100,200),
                     Wall(400,300,100,300),
                     Wall(700,400,200,50),
                     Wall(0,300,100,50),
                     Wall(100,200,50,150),
                     Wall(100,150,200,50),
                     Wall(850,0,50,300),
                     Wall(900,250,100,50),
                     Wall(-50,0,50,750),
                     Wall(0,-50,1000,50),
                     Wall(0,750,1000,50),
                     Wall(1000,0,100,1000)]
            coin.rect.x, coin.rect.y = 220, 350
            coin1.rect.x, coin1.rect.y = 200, 100
            coin2.rect.x, coin2.rect.y = 20, 250
            coin3.rect.x, coin3.rect.y = 750,350
            door.rect.x, door.rect.y = 900,150
            sharp.rect.x, sharp.rect.y =900,500
            shap.rect.x, shap.rect.y =500,500
            shap1.rect.x, shap1.rect.y =700,500
            coins = 0
            level1 = False
            level2 = True

    
    elif level2:
        mw.blit(door.image, (door.rect.x, door.rect.y))
        mw.blit(player.image, (player.rect.x, player.rect.y))
        mw.blit(coin.image, (coin.rect.x, coin.rect.y))
        mw.blit(coin1.image, (coin1.rect.x, coin1.rect.y))
        mw.blit(coin2.image, (coin2.rect.x, coin2.rect.y))
        mw.blit(coin3.image, (coin3.rect.x, coin3.rect.y))
        mw.blit(sharp.image, (sharp.rect.x, sharp.rect.y))
        mw.blit(shap.image, (shap.rect.x, shap.rect.y))
        mw.blit(shap1.image, (shap1.rect.x, shap1.rect.y))
        if player.rect.colliderect(coin.rect):
            coin.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin1.rect):
            coin1.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin2.rect):
            coin2.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin3.rect):
            coin3.rect.x = 2000
            coins += 1
        if coins == 4:
            walls.pop(7)
            coins = 0
        
        if player.rect.colliderect(door.rect): # настройки для lvl 3
            player.rect.x = 50
            player.rect.y = 400
            player.vel_y = 0
            player.can_jump = True
            walls = [Wall(0,550,1000,300), # 
                     Wall(200,400,100,150),
                     Wall(800,400,100,150),
                     Wall(0,250,100,50),
                     Wall(400,0,50,250),
                     Wall(400,250,300,50),
                     Wall(650,0,50,250),
                     Wall(-50,0,50,750),
                     Wall(0,-50,1000,50),
                     Wall(0,750,1000,50),
                     Wall(1000,0,100,1000)]
            coin.rect.x, coin.rect.y = 0, 200
            coin1.rect.x, coin1.rect.y = 800, 350
            wrag.rect.x, wrag.rect.y = 400, 465
            level2 = False
            level3 = True
    elif level3:
        mw.blit(player.image, (player.rect.x, player.rect.y))
        mw.blit(wrag.image, (wrag.rect.x, wrag.rect.y))
        mw.blit(coin.image, (coin.rect.x, coin.rect.y))
        mw.blit(coin1.image, (coin1.rect.x, coin1.rect.y))
        if wrag.rect.top == player.rect.bottom:
            player.rect.x, player.rect.y = 50, 400
        wrag.enemy_move()
        if player.rect.colliderect(coin.rect):
            coin.rect.x = 2000
            coins += 1
        if player.rect.colliderect(coin1.rect):
            coin1.rect.x = 2000
            coins += 1
        

        if player.rect.x > 1000: # настройки для lvl 3
            player.rect.x = 50
            player.rect.y = 400
            player.vel_y = 0
            player.can_jump = True
            walls = [Wall(0,550,1000,300), # 
                     Wall(200,400,50,150),
                     Wall(850,400,50,150),
                     Wall(950,250,50,100),
                     Wall(500,150,300,50),
                     Wall(325,150,50,50),
                     Wall(0,150,200,50),
                     Wall(150,0,50,200),
                     Wall(-50,0,50,750),
                     Wall(0,-50,1000,50),
                     Wall(0,750,1000,50),
                     Wall(1100,0,100,1000)]
            wrag.rect.x, wrag.rect.y = 400, 450
            level3 = False
            level4 = True
    elif level4:
        mw.blit(player.image, (player.rect.x, player.rect.y))
        mw.blit(wrag.image, (wrag.rect.x, wrag.rect.y))
        mw.blit(coin.image, (coin.rect.x, coin.rect.y))
        mw.blit(coin1.image, (coin1.rect.x, coin1.rect.y))



    for w in walls:
        w.draw(mw)
 
    pygame.display.update() #оновлення кадрів
    clock.tick(60) # фпс




