""" 
-------------------------------------------------------------------------
Name:   main.py
Purpose:  Produce a python program demonstrating my understanding of a variety of topics in the course.

Author: Tam.S

Date: 22/03/2021
-------------------------------------------------------------------------
"""

import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
YELLOW   = ( 225, 225,   0)
ORANGE   = ( 245, 200,  88)
BLUE     = (  90, 140, 255)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (750, 580)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Stephanie's CPT")

# Load graphics
background_image = pygame.image.load("background.jpg").convert()

# Set image sizes
background_image = pygame.transform.scale(background_image,(750,580))

# Set positions of graphics
background_position = [0, 0]

# Load text
# Captions
title_font = pygame.font.SysFont('Arial', 30, True, False)
text_font = pygame.font.SysFont('Arial', 16, True, False)
header_font = pygame.font.SysFont('Arial', 20, True, False)

line_1 = title_font.render("Find the Computer Components!", True, YELLOW)

line_2 = header_font.render("Is your MEMORY good enough?", True, BLUE)

# Text descriptions for components
line_a = text_font.render("A GRAPHICS CARD, GPU, renders an image to a display device.", True, WHITE)

line_b = text_font.render("The MOTHERBOARD serves as a single platform that connects all the", True, WHITE)
line_ba = text_font.render("components of the computer together.", True, WHITE)

line_c = text_font.render("A MONITOR is an output device that displays information in pictorial form.", True, WHITE)

line_d = text_font.render("A HARD DRIVE stores data for long term use.", True, WHITE)

line_e = text_font.render("The CENTRAL PROCESSING UNIT is the primary component of a", True, WHITE)
line_ea = text_font.render("computer that processes instructions.", True, WHITE)

line_f = text_font.render("The POWER SUPPLY powers the different components in a computer.", True, WHITE)

line_g = text_font.render("The MOUSE detects movement on a surface and translate it to a", True, WHITE)
line_ga = text_font.render("pointer on a display.", True, WHITE)

line_h = text_font.render("A KEYBOARD inputs information by characters and functions into a", True, WHITE)
line_ha = text_font.render("computer system using buttons and keys.", True, WHITE)

line_i = text_font.render("RANDOM ACCESS MEMORY is memory that is used as a short-term", True, WHITE)
line_ia = text_font.render("storage space for the computer.", True, WHITE)

line_j = header_font.render("CONGRATULATIONS!!", True, RED)

# Starting position of the rectangle
rect_x = 199
rect_y = 139
rect_width = 85
rect1 = True

rect2_x = 333
rect2_y = 139
rect2_width = 85
rect2 = True

rect3_x = 469
rect3_y = 139
rect3_width = 85
rect3 = True

rect4_x = 199
rect4_y = 249
rect4_width = 85
rect4 = True

rect5_x = 333
rect5_y = 249
rect5_width = 85
rect5 = True

rect6_x = 469
rect6_y = 249
rect6_width = 85
rect6 = True

rect7_x = 199
rect7_y = 359
rect7_width = 85
rect7 = True

rect8_x = 333
rect8_y = 359
rect8_width = 85
rect8 = True

rect9_x = 469
rect9_y = 359
rect9_width = 85
rect9 = True

# Set booleans
button1_answer = False
button2_answer = False
button3_answer = False
button4_answer = False
button5_answer = False
button6_answer = False
button7_answer = False
button8_answer = False
button9_answer = False

# Define initial round
round = 1

mouse_click_position = [0,0]

#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------  
    # --- Game logic should go here
while done == False:
  button_pressed = False
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          print("User asked to quit.")
          done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
          button_pressed = True
          print("User pressed a mouse button")
          mouse_click_position = pygame.mouse.get_pos()
      
    # check if the mouse click is in the button area
    
  # Set 'if statement' conditions for button1_answer

  if button_pressed:
    #round 1
    if (rect8_x <= mouse_click_position[0] and mouse_click_position[0] <= rect8_x + rect8_width) and (rect8_y <= mouse_click_position[1] and mouse_click_position[1] <= rect8_y + rect8_width) and button8_answer == False:
      rect8 = not(rect8)
      if round == 1:
        button8_answer = True
        round += 1    

    #round 2
    if (rect_x <= mouse_click_position[0] and mouse_click_position[0] <= rect_x + rect_width) and (rect_y <= mouse_click_position[1] and mouse_click_position[1] <= rect_y + rect_width) and button1_answer == False:
      rect1 = not(rect1)
      if round == 2:
        button1_answer = True
        round += 1

    #round 3
    if (rect4_x <= mouse_click_position[0] and mouse_click_position[0] <= rect4_x + rect4_width) and (rect4_y <= mouse_click_position[1] and mouse_click_position[1] <= rect4_y + rect4_width) and button4_answer == False:
      rect4 = not(rect4)
      if round == 3:
        button4_answer = True
        round += 1    

    #round 4
    if (rect2_x <= mouse_click_position[0] and mouse_click_position[0] <= rect2_x + rect2_width) and (rect2_y <= mouse_click_position[1] and mouse_click_position[1] <= rect2_y + rect2_width) and button2_answer == False:
      rect2 = not(rect2)
      if round == 4:
        button2_answer = True
        round += 1    

    #round 5
    if (rect5_x <= mouse_click_position[0] and mouse_click_position[0] <= rect5_x + rect5_width) and (rect5_y <= mouse_click_position[1] and mouse_click_position[1] <= rect5_y + rect5_width) and button5_answer == False:
      rect5 = not(rect5)
      if round == 5:
        button5_answer = True
        round += 1    

    #round 6
    if (rect7_x <= mouse_click_position[0] and mouse_click_position[0] <= rect7_x + rect7_width) and (rect7_y <= mouse_click_position[1] and mouse_click_position[1] <= rect7_y + rect7_width) and button7_answer == False:
      rect7 = not(rect7)
      if round == 6:
        button7_answer = True
        round += 1    

    #round 7
    if (rect6_x <= mouse_click_position[0] and mouse_click_position[0] <= rect6_x + rect6_width) and (rect6_y <= mouse_click_position[1] and mouse_click_position[1] <= rect6_y + rect6_width) and button6_answer == False:
      rect6 = not(rect6)
      if round == 7:
        button6_answer = True
        round += 1    
    
    #round 8
    if (rect9_x <= mouse_click_position[0] and mouse_click_position[0] <= rect9_x + rect9_width) and (rect9_y <= mouse_click_position[1] and mouse_click_position[1] <= rect9_y + rect9_width) and button9_answer == False:
      rect9 = not(rect9)
      if round == 8:
        button9_answer = True
        round += 1   

    #round 9
    if (rect3_x <= mouse_click_position[0] and mouse_click_position[0] <= rect3_x + rect3_width) and (rect3_y <= mouse_click_position[1] and mouse_click_position[1] <= rect3_y + rect3_width) and button3_answer == False:
      rect3 = not(rect3)
      if round == 9:
        button3_answer = True
        round += 1    

  # --- Drawing code should go here
    
  # First, clear the screen to white or whatever background colour. 
  # Don't put other drawing commands above this, or they will be erased with this command.
  screen.fill(WHITE)

  # Copy image to screen:
  screen.blit(background_image, background_position)

  # Draw the rectangle
  if rect1 == True:
    pygame.draw.rect(screen, ORANGE, [rect_x, rect_y, rect_width, rect_width])

  if rect2 == True:
    pygame.draw.rect(screen, ORANGE, [rect2_x, rect2_y, rect2_width, rect2_width])

  if rect3 == True:
    pygame.draw.rect(screen, ORANGE, [rect3_x, rect3_y, rect3_width, rect3_width])

  if rect4 == True:
    pygame.draw.rect(screen, ORANGE, [rect4_x, rect4_y, rect4_width, rect4_width])

  if rect5 == True:
    pygame.draw.rect(screen, ORANGE, [rect5_x, rect5_y, rect5_width, rect5_width])

  if rect6 == True:
    pygame.draw.rect(screen, ORANGE, [rect6_x, rect6_y, rect6_width, rect6_width])

  if rect7 == True:
    pygame.draw.rect(screen, ORANGE, [rect7_x, rect7_y, rect7_width, rect7_width])

  if rect8 == True:
    pygame.draw.rect(screen, ORANGE, [rect8_x, rect8_y, rect8_width, rect8_width])

  if rect9 == True:
    pygame.draw.rect(screen, ORANGE, [rect9_x, rect9_y, rect9_width, rect9_width])

  # Put the image of the text on the screen
  screen.blit(line_1, [135, 40])
  screen.blit(line_2, [220,90])

  # Button output with text
  if round == 1:
    screen.blit(line_h, [100, 500])
    screen.blit(line_ha, [100, 520])

  if round == 2:
    screen.blit(line_a, [100, 500])

  if round == 3:
    screen.blit(line_d, [100, 500])

  if round == 4:
    screen.blit(line_b, [100, 500])
    screen.blit(line_ba, [100, 520])

  if round == 5:
    screen.blit(line_e, [100, 500])
    screen.blit(line_ea, [100, 520])

  if round == 6:
    screen.blit(line_g, [100, 500])
    screen.blit(line_ga, [100, 520])

  if round == 7:
    screen.blit(line_f, [100, 500])
    
  if round == 8:
    screen.blit(line_i, [100, 500])
    screen.blit(line_ia, [100, 520])

  if round == 9:
    screen.blit(line_c, [100, 500])
    
  if round == 10:
    screen.blit(line_j, [270, 500])
    
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()

  # --- Limit to 60 frames per second
  clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()