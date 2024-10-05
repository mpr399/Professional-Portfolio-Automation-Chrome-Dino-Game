import pyautogui
from PIL import Image, ImageGrab
import time

# This game automate the Google dino game.
# URL = chrome://dino
# start this script and immediately switch screen to chrome full screen with game on
# The App need to know the coordinates on the screen when to detect an incoming object
# Use the rectangle function at the bottom to experiment with the right coordinates

WHITE_MODE = True

x_cor_cactus = [250, 1000]
y_cor_cactus = [1290, 1300]

x_cor_bird = [250, 1000]
y_cor_bird = [1140, 1150]


def detect_mode(image_data):
    global WHITE_MODE

    if image_data[x_cor_cactus[0], y_cor_cactus[0]] < 100:
        WHITE_MODE = False
    else:
        WHITE_MODE = True


def press_key(key):
    pyautogui.press(key)
    return


def check_to_jump_or_duck(image_data):
    if WHITE_MODE:
        # cactus
        for x in range(x_cor_cactus[0], x_cor_cactus[1]):
            for y in range(y_cor_cactus[0], y_cor_cactus[1]):
                if image_data[x, y] < 100:
                    press_key("up")
                    return
        # birds
        for x in range(x_cor_bird[0], x_cor_bird[1]):
            for y in range(y_cor_bird[0], y_cor_bird[1]):
                if image_data[x, y] < 100:
                    press_key("down")
                    return
    else:
        # cactus
        for x in range(x_cor_cactus[0], x_cor_cactus[1]):
            for y in range(y_cor_cactus[0], y_cor_cactus[1]):
                if image_data[x, y] > 100:
                    press_key("up")
                    return
        # birds
        for x in range(x_cor_bird[0], x_cor_bird[1]):
            for y in range(y_cor_bird[0], y_cor_bird[1]):
                if image_data[x, y] > 100:
                    press_key("down")
                    return

    return


if __name__ == "__main__":
    time.sleep(5)
    press_key('space')

    screenshot = ImageGrab.grab().convert('L')
    image_data = screenshot.load()
    detect_mode(image_data)

    while True:
        screenshot = ImageGrab.grab().convert('L')
        image_data = screenshot.load()
        check_to_jump_or_duck(image_data)

        """


        # For detecting the pixel ranges (x and y coordinates) for incoming collision when setting up the game

        # # Draw the rectangle for cactus
        for x in range(x_cor_cactus[0], x_cor_cactus[1]):
            for y in range(y_cor_cactus[0], y_cor_cactus[1]):
                print(image_data[x, y])
                image_data[x, y] = 0

        # # # Draw the rectangle for birds
        for x in range(x_cor_bird[0], x_cor_bird[1]):
            for y in range(y_cor_bird[0], y_cor_bird[1]):
                print(image_data[x, y])
                image_data[x, y] = 171

        screenshot.show()
        break
        
        """

