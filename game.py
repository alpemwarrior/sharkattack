import pygame

pygame.init()

win = pygame.display.set_mode((1000, 750))

pygame.display.set_caption("Shark Attack!")


walkRight_e = [pygame.image.load('A0R.png'), pygame.image.load('A0R.png'), pygame.image.load('A0R.png'),
             pygame.image.load('A1R.png'), pygame.image.load('A1R.png'), pygame.image.load('A1R.png'),
             pygame.image.load('A2R.png'), pygame.image.load('A2R.png'), pygame.image.load('A2R.png')]

walkLeft_e = [pygame.image.load('A0L.png'), pygame.image.load('A0L.png'), pygame.image.load('A0L.png'),
             pygame.image.load('A1L.png'), pygame.image.load('A1L.png'), pygame.image.load('A1L.png'),
             pygame.image.load('A2L.png'), pygame.image.load('A2L.png'), pygame.image.load('A2L.png')]

walkRight = [pygame.image.load('B0R.png'), pygame.image.load('B0R.png'), pygame.image.load('B0R.png'),
             pygame.image.load('B1R.png'), pygame.image.load('B1R.png'), pygame.image.load('B1R.png'),
             pygame.image.load('B2R.png'), pygame.image.load('B2R.png'), pygame.image.load('B2R.png')]

walkLeft = [pygame.image.load('B0L.png'), pygame.image.load('B0L.png'), pygame.image.load('B0L.png'),
             pygame.image.load('B1L.png'), pygame.image.load('B1L.png'), pygame.image.load('B1L.png'),
             pygame.image.load('B2L.png'), pygame.image.load('B2L.png'), pygame.image.load('B2L.png')]


bg = pygame.image.load('Undersea.jpg')
char = pygame.image.load('A0R.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        pygame.draw.ellipse(win, self.color, (self.x, self.y, 50, 5), 0)
#'''
def redrawGameWindow():

    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

#'''
def redrawGameWindowBG():
    win.fill([0, 0, 0])
    win.blit(bg, (0, 0))

#____________________________________________

class josele(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft_e[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight_e[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight_e[0], (self.x, self.y))
            else:
                win.blit(walkLeft_e[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

class projectilej(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        pygame.draw.ellipse(win, self.color, (self.x, self.y, 50, 5), 0)



def redrawGameWindowj():

    josele.draw(win)
    for bulletj in bulletsj:
        bulletj.draw(win)



# mainloop


man = player(850, 600, 200, 70, 8)
bullets = []

josele = josele(150, 150, 200, 70, 8)
bulletsj = []

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 0 < bullet.x < 1000:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, (0, 0, 255), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        man.standing = True
        man.walkCount = 0

    if keys[pygame.K_UP]:
        if man.y > 0:
            man.y -= man.vel

    if keys[pygame.K_DOWN]:
        if man.y < (750 - man.height):
            man.y += man.vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bulletj in bulletsj:
        if 0 < bulletj.x < 1000:
            bulletj.x += bulletj.vel
        else:
            bulletsj.pop(bulletsj.index(bulletj))

    keys = pygame.key.get_pressed()
#
    if keys[pygame.K_q] or keys[pygame.K_c]:
        if josele.left:
            facing = -1
        else:
            facing = 1

        if len(bulletsj) < 5:
            bulletsj.append(
                projectilej(round(josele.x + josele.width // 2), round(josele.y + josele.height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_a] and josele.x > josele.vel:
        josele.x -= josele.vel
        josele.left = True
        josele.right = False
        josele.standing = False
    elif keys[pygame.K_d] and josele.x < 1000 - josele.width - josele.vel:
        josele.x += josele.vel
        josele.right = True
        josele.left = False
        josele.standing = False
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    else:
        josele.standing = True
        josele.walkCount = 0

    if keys[pygame.K_w]:

        if josele.y > 0:
            josele.y -= josele.vel

    if keys[pygame.K_s]:
        if josele.y < (750 - josele.height):
            josele.y += josele.vel

    for bullet in bullets:
        if bullet.y - bullet.radius < josele.hitbox[1] + josele.hitbox[3] and bullet.y + bullet.radius > josele.hitbox[1]:
            if bullet.x + bullet.radius > josele.hitbox[0] and bullet.x - bullet.radius < josele.hitbox[0] + josele.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                run = False
                print('Player 1 wins!')

    for bullet in bulletsj:
        if bullet.y - bullet.radius < man.hitbox[1] + man.hitbox[3] and bullet.y + bullet.radius > man.hitbox[1]:
            if bullet.x + bullet.radius > man.hitbox[0] and bullet.x - bullet.radius < man.hitbox[0] + man.hitbox[2]:
                bulletsj.pop(bulletsj.index(bullet))
                run = False
                print('Player 2 wins!')
    
    redrawGameWindowBG()
    redrawGameWindow()
    redrawGameWindowj()
    pygame.display.update()




pygame.quit()


