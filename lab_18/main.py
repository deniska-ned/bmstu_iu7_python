import random
import math

import pygame

import colors

MIN_SPEED = 7
MAX_SPEED = 20

MIN_DIVISOR = 2
MAX_DIVISOR = 10

TREE_FREQ = 50

class Sun:
    def __init__(self, y, screen_width):
        self.radius = 170
        self.sun = pygame.image.load("sun.png")
        self.sun_rect = self.sun.get_rect()
        self.x = 0
        self.y = 100
        self.sun_rect.center = (self.x, self.y)
        self.screen_width = screen_width

    def move(self):
        if self.x > self.screen_width + self.radius:
            self.x = -self.radius
        else:
            self.sun_rect.center = (self.x, self.y)
            self.x += 1

    def draw(self, screen):
        screen.blit(self.sun, self.sun_rect)
       

class Tree:
    def __init__(self, height, k, b):
        self._height = height
        self._screen_width, self._screen_height = pygame\
                .display.get_surface().get_size()

        self._k = k

        self._b = b + round(
                (self._screen_height / 2) /
                (self._screen_height / 2 - self._screen_height / 10) *
                (self._height - self._screen_height / 10)
                )

        self.x = self._screen_width
        self.y = round(self._k * self.x + self._b)

        self.speed = round(
                (self._height - self._screen_height / MAX_DIVISOR) /
                (self._screen_height / MIN_DIVISOR -
                self._screen_height / MAX_DIVISOR) *
                (MAX_SPEED - MIN_SPEED)
                ) + MIN_SPEED

        self.color = random.choice(colors.TREE_LIST)

    def draw(self, screen):
        x = self.x
        y = self.y

        dx = self._height // 6
        tree_points = ((x - dx, y), (x + dx, y), (x, y - self._height))
        pygame.draw.polygon(screen, self.color, tree_points)

        self.x -= self.speed
        self.y = round(self._k * self.x + self._b)

class Application:
    def __init__(self):
        self._running = True
        self._screen = None
        self.size = self.width, self.height = 1000, 700
        self._clock = pygame.time.Clock()

        self.trees = []

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size)
        self._running = True
        self.skier = pygame.image.load("skier.png")
        self.skier_original = pygame.image.load("skier.png")
        self.skier_rect = self.skier.get_rect()
        self.sun = Sun(y = 100, screen_width = self.width)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self, frame_num):
        # sky
        self._screen.fill(colors.SKY)

        # snown mauntain
        mountain_points = (
                (0, self.height // 3),
                (0, self.height),
                (self.width, self.height)
                )
        pygame.draw.polygon(self._screen, colors.MOUNTAIN, mountain_points)

        # sun
        self.sun.move()
        self.sun.draw(self._screen)

        # y = kx + b
        b = mountain_points[0][1]
        k = (self.height - b) / self.width

        # skier person
        x = self.width // 7
        y = round(k * x + b) - 30
        self.skier = pygame.transform.rotate(
                self.skier_original,
                -math.degrees(math.atan(k))
                )
        self.skier_rect.center = (x, y)
        self._screen.blit(self.skier, self.skier_rect)

        # tree
        if random.randint(0, TREE_FREQ) == 1:
            tree = Tree(
                    random.randint(
                        self.width // MAX_DIVISOR,
                        self.width // MIN_DIVISOR
                        ),
                    k,
                    b
                    )
            self.trees.append(tree)
        self.trees.sort(key = lambda tree: tree._height)
        self.trees.reverse()

        for i in range(len(self.trees) - 1, -1, -1):
            if self.trees[i].x < -100:
                self.trees = self.trees[:i] + self.trees[i + 1:]
            else:
                self.trees[i].draw(self._screen)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()
        
        frame_num = 0

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render(frame_num)

            self._clock.tick(60)
            frame_num += 1
        
        self.on_cleanup()

def main():
    app = Application()
    app.on_execute()

if __name__ == "__main__":
    main()
