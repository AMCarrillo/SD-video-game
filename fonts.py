import pygame.freetype 

pygame.init()

window = pygame.display.set_mode((640, 192))
window.fill((255, 255, 255))

Sprint2 = pygame.freetype.Font("Sprint2.ttf", 32)
positions = [[32, 64], [36, 128]]
lines = ["Hello there!", "Welcome to the"]

for line, pos in zip(lines, positions):
    text, rect = Sprint2.render(line, (0, 0, 0))
    rect.topleft = pos
    window.blit(text, rect)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()