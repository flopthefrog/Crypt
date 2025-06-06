#James Shetlar
#6/2/25

#Imports
import pygame
import time

pygame.init()

#Variables
font = pygame.font.Font('Font/Bitmgothic.otf', 32)
screen = pygame.display.set_mode([800,500])
timer = pygame.time.Clock()

#Message lists
masterMessageList = ['messageList']
messageList = ['Welcome to the Crypt.', 'This is a second message.',
               'This is the final message!']

#Other message variables
snip = font.render('', True, 'white')
counter = 0
speed = 3
activeMessage = 0
message = messageList[activeMessage]
textSound = pygame.mixer.Sound('sfx/text_scroll2.wav')
done = False

#Game Loop
run = True

while run:
    screen.fill('brown')
    pygame.display.set_caption('The Crypt')
    timer.tick(60)
    pygame.draw.rect(screen, 'black', [0, 300, 800, 200])
    pygame.mixer.set_num_channels(1)
    #Determines text print speed
    if counter < speed *len(message):
        counter += 1
        pygame.mixer.Sound.play(textSound)

    elif counter >= speed*len(message):
        done = True
        pygame.mixer.Sound.stop(textSound)
    
    #Quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        #Plays the next line of text
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_RETURN or pygame.K_SPACE) and done and activeMessage < len(messageList) - 1:
                activeMessage += 1
                done = False
                message = messageList[activeMessage]
                counter = 0      

    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 310))
    
    numChannels = pygame.mixer.Sound.get_num_channels(textSound)
    print(numChannels)

    pygame.display.flip()
pygame.quit()
