import pygame
from sys import exit
from random import randint , choice
import math 

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha() 
		player_walk_2 = pygame.image.load('Graphics/player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2] #self makes sure the data is stored in object itself in this case the Player
		self.player_index = 0
		self.player_jump = pygame.image.load('Graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0
		self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
		self.jump_sound.set_volume(0.3)
    

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()
			

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300
			self.gravity = 0

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.2
			if self.player_index >= len(self.player_walk): self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]
            
	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		self.type = type
		
		if type == 'fly' or type == "sine_fly":
			self.frames = [pygame.image.load('Graphics/fly/Fly1.png').convert_alpha(),pygame.image.load('Graphics/fly/Fly2.png').convert_alpha()]
			y_pos = 210
			
		else:
			snail_1 = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
			snail_2 = pygame.image.load('Graphics/snail/snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
		self.time=0
		self.base_y=randint(69,160) #;)

	def animation_state(self):
		self.animation_index += 0.2
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()

		self.rect.x-=speed
		
		if self.type =="sine_fly": 
			self.time+= 0.08
			self.rect.y = self.base_y + math.sin(self.time)*20
		self.collision_rect = self.rect.inflate(-10, -10)
		self.destroy() 
		

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()



def display_score():

    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)
    return current_time


def collision_sprite():
	for obstacle in obstacle_group:
		if obstacle.collision_rect.colliderect(player.sprite.rect):
			obstacle_group.empty()
			return False
	return True

def move_background():
    global bg_x1, bg_x2
    sky_speed = speed * 0.35
    bg_x1 -= sky_speed
    bg_x2 -= sky_speed

    if bg_x1 <= -800:
        bg_x1 = 800

    if bg_x2 <= -800:
        bg_x2 = 800

    screen.blit(sky_surface, (int(bg_x1), 0))
    screen.blit(sky_surface, (int(bg_x2), 0))
def move_ground():
    global ground_x1, ground_x2

    ground_x1 -= speed
    ground_x2 -= speed

    if ground_x1 <= -800:
        ground_x1 = 800
    if ground_x2 <= -800:
        ground_x2 = 800

    screen.blit(ground_surface, (int(ground_x1), 300))
    screen.blit(ground_surface, (int(ground_x2), 300))

bg_x1 = 0
bg_x2 = 800     
ground_x1 = 0
ground_x2 = 800
base_speed=5.5
pygame.init()
screen = pygame.display.set_mode((800,400))  
clock = pygame.time.Clock()  
test_font = pygame.font.Font("font/Pixeltype.ttf",50)
game_active = False
start_time = 0
score = 0
bg_music=pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(.5)
bg_music.play(loops=-1)


#Groups
player= pygame.sprite.GroupSingle() #This player is not a sprite it is just a group single of a sprite
player.add(Player())

obstacle_group=pygame.sprite.Group()

pygame.display.set_caption("Runny Bunny")

sky_surface = pygame.image.load("Graphics/sky.png").convert() 
ground_surface = pygame.image.load("Graphics/ground.png").convert()


# Intro Screen 
player_stand = pygame.image.load("Graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200));

game_name = test_font.render("Runny Bunny","False",(111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))

game_msg = test_font.render("Press space to run", False ,(111,196,169))
game_msg_rect = game_msg.get_rect(center=(400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1

Base_Delay = 1500  
Min_delay = 900  
Step = 100          
Milestone = 15    
last_mile = 0

current_spawn_delay = Base_Delay
pygame.time.set_timer(obstacle_timer, current_spawn_delay)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.sprite.rect.collidepoint(event.pos) and player.sprite.rect.bottom == 300 : 
                        player.sprite.gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.sprite.rect.bottom == 300 :
                    player.sprite.gravity = -21

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["sine_fly","fly","snail","snail","snail"])))
                
            
            #Spawning animation 
            
            

            
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active =1 
                
                start_time=int(pygame.time.get_ticks()/1000)

       

               
    if game_active:
        
        
        
        
		
        calculated_speed=base_speed+score*.05
        speed = min(calculated_speed, 14)
        move_ground()
        move_background()
        score = display_score()


		

		
		
        milestone = score // Milestone
		
		
        if milestone != last_mile:
            last_mile = milestone
            desired_spawn_delay = Base_Delay - (milestone * Step)
            desired_spawn_delay = max(desired_spawn_delay, Min_delay)
            current_spawn_delay = desired_spawn_delay
            pygame.time.set_timer(obstacle_timer, current_spawn_delay)

        # Player 
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #Collision
        game_active = collision_sprite()


    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        player.sprite.rect.midbottom = (80,300)
        player.sprite.gravity=0


        score_message = test_font.render(f"Your Score: {score}", False ,(111,196,169))
        score_message_rect = score_message.get_rect(center=(400,330))
        screen.blit(game_name,game_name_rect)
        if score == 0: screen.blit(game_msg,game_msg_rect)
        else: screen.blit(score_message,score_message_rect)
       


    pygame.display.update()
    clock.tick(60)  


