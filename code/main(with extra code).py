#James Shetlar
#6/2/25

#Imports
import pygame


pygame.init()

#Variables
font = pygame.font.Font('Font/Bitmgothic.otf', 32)
userFont = pygame.font.Font('Font/Bitmgothic.otf', 64)
screen = pygame.display.set_mode([800,500])
timer = pygame.time.Clock()

textRect = pygame.Rect(0, 200, 800, 400)
userRect = pygame.Rect(350, 50, 100, 100)


#Message lists

introText = ['Welcome to the Crypt. (Press enter to continue.)', 
               'You don\'t know how you got here. All you know is that the door behind you leads to the exit.', 
               'There are three rooms you can enter from here. You can either:                                                                F: Go forwards                                                           L: Go Left                                                                R: Go Right                                                             Press enter when you make your choice.']
forwardRoomText = ['You decide go forward, heading into the room right in front of you.', 
                   'As you enter, something feels off.', 
                   'Before you can even react, the door behind you slams shut, locking you inside.', 'You\'re trapped with no means of escaping.',
                   'You Lose.']
leftRoomText = ['You decide to enter the room to your left.', 'The room is bare, and shabby brick walls encase the room.', 
                'While searching, your hand finds a loose brick in the wall.', 
                'You find a key behind the loose brick, and unlock the door.',
                'You Win!']
rightRoomText = ['You carefully enter the room to your right, as wood splinters surround the door.',
                 'As you enter, your foot seems to shift down, and a mechanism whirrs to life.',
                 'Before you can grasp the situation, wooden spikes jut out from the floor.',
                 'You Lose.']

masterMessageList = [introText, forwardRoomText, leftRoomText, rightRoomText]
currentMessage = masterMessageList[0]



#Other message variables
#counter = 0
#speed = 3
activeMessage = 0
message = currentMessage[activeMessage]
user_text = ''
allowed_chars = 'f, F, l, L, r, R'

#textSound = pygame.mixer.Sound('sfx/text_scroll2.wav') #Implement sfx when animation bug is fixed
#done = False

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
            #image = font.render(text[:i][0:counter//speed], aa, color)
            #snip = font.render(text[:i], True, color)
            image = font.render(text[:i], aa, color) #Nullifies all animation for text, will be removed when animation functions properly
            
        surface.blit(image, (rect.left + 10, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text



#Game Loop
run = True

while run:
    screen.fill('brown')
    
    pygame.draw.rect(screen, 'black', textRect)
    pygame.draw.rect(screen, 'black', userRect, 2)
    
    text_surface = userFont.render(user_text, True, 'white')
    pygame.display.set_caption('The Crypt')
    timer.tick(60)
    pygame.mixer.set_num_channels(1)
    
    #Animates text (Not used for now)
    #if counter < speed * len(message):
        #counter += 1
        #pygame.mixer.Sound.play(textSound)
    #Not used
    #elif counter >= speed * len(message):
        #done = True
        #pygame.mixer.Sound.stop(textSound)

    #Quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        #Inputs for the user to choose which direction and plays the next line of text
        if event.type == pygame.KEYDOWN:
            
            #Takes user input and displays the result
            if event.unicode in allowed_chars:

                if event.key == pygame.K_f:
                    user_text = "F"
                    currentMessage = masterMessageList[1]
                    activeMessage = -1
                    
            
                elif event.key == pygame.K_l:
                    user_text = "L"
                    currentMessage = masterMessageList[2]
                    activeMessage = -1
                    
                elif event.key == pygame.K_r:
                    user_text = "R"
                    currentMessage = masterMessageList[3]
                    activeMessage = -1

            #Plays the next line of text via the enter key
            elif event.key == pygame.K_RETURN and activeMessage < len(message) - 1:
                activeMessage += 1
                message = currentMessage[activeMessage]
                counter = 0
                user_text = ''      
            
            
                
            
            


    drawText(screen, message, 'white', textRect, font, True, None)
    screen.blit(text_surface, (userRect.x + 25, userRect.y + 20))
    

    pygame.display.flip()
pygame.quit()
