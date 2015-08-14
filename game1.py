import pygame
import os
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
SPRINGG = (0, 255, 127)
RED = (255, 0, 0)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

        
    def changecolor(self, COLOR):
        self.image.fill(COLOR)
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            self.image = pygame.Surface([10,10])
            self.image.fill(RED)
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    # tree image change
    #def changeimage(self):
      # try:
       #     self.image = pygame.image.load(os.path.join("data","tree3.png"))
        #except:
         #   self.image.fill(WHITE)
    # end tree image
    
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 8, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
# Tree image Code
#difference1 = 0
#x1,y1,w1,h1 = 0,0,0,0
#count = 0

#for j in range(1,31):
    #wall = Wall(difference1,y1+count,w1,h1)
    #wall.changeimage()
    #wall_list.add(wall)
    #all_sprite_list.add(wall)
    #count+=20
    #difference1+=0
# end tree code 
wall = Wall(8, 0, 792, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

#raihan bottom wall
wall = Wall(10, 592, 790, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

#raihan right wall
wall = Wall(792, 8, 8, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

#raihan bottom straight line
wall = Wall(120, 490, 790, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

#raihan top straight line
wall = Wall(120, 100, 630, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

#raihan right line
wall = Wall(120, 100, 8, 400)
wall_list.add(wall)
all_sprite_list.add(wall)

 #first middle
 
wall = Wall(225, 220, 430, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

# second middle

wall = Wall(225, 225, 8, 163)
wall_list.add(wall)
all_sprite_list.add(wall)

# third middle

wall = Wall(230, 380, 480, 8)
wall_list.add(wall)
all_sprite_list.add(wall)

# connecting line

wall = Wall(675, 200, 8, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

#Start:
wall = Wall(230, 350, 50, 30)
wall_list.add(wall)
all_sprite_list.add(wall)

#End:
wall = Wall(700, 540, 100, 100)
wall_list.add(wall)
all_sprite_list.add(wall)


#raihan inner left wall maze
x=220
for i in range(4):
    wall = Wall(145, x, 85, 8)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x=x+50

#upper loop
x1=150
y1=0
w1=8
h1=80

x2=175
y2=50
w2=8
h2=150
for n in range(1,23):
    if n%2==0:
        wall = Wall(x1,y1,w1,h1)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        x1+=50
    else:
        wall = Wall(x2,y2, w2, h2)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        x2+=50


#inner upper line maze
x=250
for i in range(9):
    wall = Wall(x,135,8,180)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x=x+50

#inner lower line maze
x=275
for i in range(9):
    wall = Wall(x,280,8,100)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x=x+50

#inner lower back line maze
x=250
for i in range(9):
    wall = Wall(x,385,8,80)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x=x+50
    

#raihan right maze
x = 120
for i in range(8):
    wall = Wall(0, x, 80, 8)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x = x+50

#raihan left wall maze
x = 130
for i in range(5):
    wall = Wall(710, x, 80, 8)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x = x+50

#raihan left outer line maze
x = 145
for i in range(7):
    wall = Wall(50, x, 130, 8)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x = x+50

#raihan bottom line maze
y1 = 125
y2 = 150
for i in range(1,25):
    if i%2==0:
        wall = Wall(y1, 420, 8, 130)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        y1=y1+50
    else:
        wall = Wall(y2, 520, 8, 100)
        wall_list.add(wall)
        all_sprite_list.add(wall)
        y2=y2+50

#raihan right maze
x = 155
for i in range(4):
    wall = Wall(675, x, 80, 8)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x = x+50


#sound:
pygame.mixer.music.load('the-borderline-round.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()
 
# Create the player paddle object
player = Player(220, 335)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 90 
done = False
 
while not done:
    screen.fill(SPRINGG)
    # Calculate total seconds
    total_seconds = frame_count // frame_rate
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [20, 10])
 
    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
 
    # Blit to the screen
    text = font.render(output_string, True, BLACK)
 
    screen.blit(text, [20, 30])
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    # Limit to 20 frames per second
    clock.tick(frame_rate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    all_sprite_list.update()
 
    
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
