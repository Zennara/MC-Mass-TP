import pyautogui
import time

# switch to minecraft window automatically
SWITCH_WINDOW = True

PLAYER_COUNT = 10
TIME_BETWEEN_TPS = 1


def switch_window():
    if SWITCH_WINDOW:
        # Find the Minecraft window by its title
        minecraft_windows = [window for window in pyautogui.getAllTitles() if window.startswith('Minecraft')]

        if minecraft_windows:
            # Activate the first Minecraft window found
            minecraft_window = pyautogui.getWindowsWithTitle(minecraft_windows[0])[0]
            minecraft_window.maximize()
            minecraft_window.activate()
        else:
            print("Minecraft window not found")


switch_window()
count = 1
for x in range (0, PLAYER_COUNT):
    # open chat
    pyautogui.press('t')
    pyautogui.typewrite('/tpahere ')
    for x in range(0, count):
        pyautogui.press('tab')
    count += 1
    pyautogui.press('enter')
    time.sleep(TIME_BETWEEN_TPS)