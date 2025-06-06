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
#X = 800
#Y = 200


#Message lists
masterMessageList = ['messageList', 'directionInputList']
introList = ['Welcome to the Crypt. (Press enter to continue.)', 
               'You don\'t know how you got here. All you know is that the door behind you leads to the exit.'
               ]

directionInputList = "There are three rooms you can enter from here. You can either:\n A: Go forwards\nB: Go Left\nC: Go Right"
lines = directionInputList.split('\n')



currentMessage = lines

#Other message variables
counter = 0
speed = 3
activeMessage = 0
message = currentMessage[activeMessage]
textSound = pygame.mixer.Sound('sfx/text_scroll2.wav') #Implement sfx when animation bug is fixed
done = False

#Text wrapping function (Credit to the pygame website for providing base function)
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=True, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top + 10
    lineSpacing = 5

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
            
        surface.blit(image, (rect.left + 10, y))
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
        #pygame.mixer.Sound.play(textSound)

    elif counter >= speed * len(message):
        done = True
        #pygame.mixer.Sound.stop(textSound)

    #Quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        #Plays the next line of text
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_RETURN or pygame.K_SPACE) and done and activeMessage < len(message) - 1:
                activeMessage += 1
                done = False
                message = currentMessage[activeMessage]
                counter = 0      

    drawText(screen, message, 'white', textRect, font, True, None)
    
    pygame.display.flip()
pygame.quit()
