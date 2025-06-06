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
messageList = ['Welcome to the Crypt. (Press enter or space to continue along as this is a really long message.)', 'This is a second message.',
               'This is the final message.']

#Other message variables
#snip = font.render('', True, 'white')
counter = 0
speed = 3
activeMessage = 0
message = messageList[activeMessage]
textSound = pygame.mixer.Sound('sfx/text_scroll2.wav')
done = False


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=True, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
            
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            
            #image = font.render(text[0:counter//speed], True, 'white')
            image = font.render(text[:i][0:counter//speed], aa, color)
            #snip = font.render(text[:i], True, color)
            #image = font.render(text[:i], aa, color)
            
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text






#Game Loop
run = True

while run:
    screen.fill('brown')
    textRect = pygame.draw.rect(screen, 'black', [0, 300, 800, 200])
    pygame.display.set_caption('The Crypt')
    timer.tick(60)
    pygame.mixer.set_num_channels(1)
    
    #Determines text print speed
    if counter < speed * len(message):
        counter += 1
        pygame.mixer.Sound.play(textSound)

    elif counter >= speed * len(message):
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

    drawText(screen, message, 'white', textRect, font, True, None)
    
    pygame.display.flip()
pygame.quit()
