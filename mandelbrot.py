from PIL import Image, ImageDraw
import numpy as np
import pygame

np.warnings.filterwarnings("ignore")


def PIL_mandelbrot():
    # function to save an image of mandelbrot. 
    # {Note: Iterates through each point instead of using np arrays}
    ITER = 50
    WIDTH = 1200
    HEIGHT = 1200

    BLACK = (0, 0, 0)

    def mandelbrot(comp):
        z = 0
        for n in range(ITER):
            z = z*z + comp
            if abs(z)>2:
                break
        return n

    mbot = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
    draw = ImageDraw.Draw(mbot)


    x_plot = (-2, 1)
    y_plot = (1.5, -1.5)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            comp = complex((x_plot[0] + (x/WIDTH)*(x_plot[1] - x_plot[0])),
                           (y_plot[0] + (y/HEIGHT)*(y_plot[1] - y_plot[0])))

            color = mandelbrot(comp)
            color = int((color*255)/ITER)
            
            draw.point((x, y), (color, color, color))

    mbot.save("mandelbrot.png", "PNG")

def np_mandelbrot(ITER = 20, WIDTH = 500, HEIGHT = 500):
    # initialise arrays
    X = np.linspace(-2, 0.5, num = WIDTH).reshape(1, WIDTH)
    Y = np.linspace(1.5, -1.5, num = HEIGHT).reshape(HEIGHT, 1)
    C = np.tile(X, (HEIGHT, 1)) + 1j*np.tile(Y, (1, WIDTH))

    Z = 0

    # mandelbrot
    for i in range(ITER):
        Z = Z*Z + C

    # calculate color
    color_array = np.uint8(Z*200)

    return color_array
def window():
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                pass

        surf = pygame.surfarray.make_surface(np_mandelbrot(20, 500, 500))
        screen.blit(surf, (0,0))
        pygame.display.update()


if __name__ == "__main__":
    window()
    