import pygame
import coords
import copy
from os import system, path

win = pygame.display.set_mode((800, 800))
turret = pygame.image.load(path.join("assets", "turret.png"))
turret = pygame.transform.scale(turret, (60, 60))
pygame.display.set_caption("tower defense")
pathList = []
towers = []

def loadPath():
    global pathList
    for i in coords.coords:
        system("cls")
        pathRect = pygame.Rect(i[0], i[1], i[2], i[3])
        pathList.append(pathRect)
        print(pathList)

class Tower:
    def __init__(self, rect, type = ""):
        self.towerRect = rect
        self.type = type

    def tr(self):
        return self.towerRect


def main():
    global towers
    loadPath()
    clock = pygame.time.Clock() 
    running = True
    turretBox = pygame.Rect(0, 0, 60, 60)
    while running:

        # high priority
        turretBox.x, turretBox.y = pygame.mouse.get_pos()
        turretBox.x -= turretBox.width / 2
        turretBox.y -= turretBox.height / 2

        # misc

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if True:
                    colliding = False
                    for i in pathList:
                        if pygame.Rect.colliderect(i, turretBox):
                            colliding = True
                    for i in towers:
                        if pygame.Rect.colliderect(i.tr(), turretBox):
                            colliding = True
                    if not pygame.Rect(0, 0, 800, 800).collidepoint(turretBox.x, turretBox.y):
                        colliding = True
                    if not colliding:
                        towers.append(Tower(copy.copy(turretBox)))
                        print(towers)

        # drawing
        clock.tick(60)
        win.fill((50, 160, 50))

        for i in pathList:
            pygame.draw.rect(win, (150, 75, 0), i)

        for i in towers:
            win.blit(turret, (i.tr().x, i.tr().y))
        win.blit(turret, (turretBox.x, turretBox.y))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

