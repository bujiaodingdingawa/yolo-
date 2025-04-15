import pygame

pygame.init()
running = True
clock = pygame.time.Clock()

pygame.joystick.init()
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        num_axes = joystick.get_numaxes()
        for axis_id in range(num_axes):
            axis_value = joystick.get_axis(axis_id)
            #print(f"Axis {axis_id}: {axis_value}")
        num_buttons = joystick.get_numbuttons()
        for button_id in range(num_buttons):
            button_value = joystick.get_button(button_id)
            #print(f"Button {button_id}: {button_value}")
        hats = joystick.get_numhats()


    clock.tick(30)
pygame.quit()