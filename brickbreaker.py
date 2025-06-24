import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Breaker')
clock = pygame.time.Clock()

running = True

score = 0
lives = 3

#Paddle Class
paddle = Paddle('black',200,10)
paddle.rect.x = 400
paddle.rect.y = 560

#Ball class
ball = Ball('red',10,10)
ball.rect.x = 400
ball.rect.y = 530

#Sprites Group
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_bricks = pygame.sprite.Group()

#Bricks
for i in range(7):
    brick  = Brick('white',80,30)
    brick.rect.x = 60  + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick  = Brick('yellow',80,30)
    brick.rect.x = 60  + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick  = Brick('green',80,30)
    brick.rect.x = 60  + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

#Main game looop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Keyboard Inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    
    
    #Making sure
    if ball.rect.x >= 790 :
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            text = pygame.font.Font(None,32)
            word = text.render(f'GAMEOVER',1,'red')
            screen.fill('black')
            screen.blit(word,(350,HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
    
    if pygame.sprite.collide_mask(ball,paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font('None',20)
            text = font.render(f'Level Complete',1,'red')
            screen.fill('green')
            screen.blit(text,(200,300))
            pygame.display.flip()
            time = pygame.time.wait(3000)
            running = False
    
    #Score and Lives
    screen.fill('blue')
    pygame.draw.line(screen,'black',[0,38],[800,38],10)
    font = pygame.font.Font(None,20)
    text = font.render("Score:" + str(score),1,'white')
    screen.blit(text,(0,10))
    text = font.render("Lives:" + str(lives), 1,'white')
    screen.blit(text,(650,10))
    

        
   
    
    
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    
    pygame.display.flip()


    clock.tick(60)
    