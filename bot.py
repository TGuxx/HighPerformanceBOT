import time
import pyautogui

#COLORS
BLITZ_COLOR = (0,226,88)
WITHDRAW_COLOR = (0,199,77)
CAPTCHA_COLOR = (249,249,249)

#POSITIONS
px_blitz_1 = (460,654)
px_blitz_2 = (645,654)
px_blitz_3 = (830,654)
px_blitz_4 = (1015,654)
px_blitz_5 = (1200,654)
px_blitz_6 = (1385,654)
px_blitz_7 = (1570,654)

WITHDRAW_POS = (1690,330)
CAPTCHA_POS = (860,600)
CAPTCHA_POS_CLICK = (750,620)
pocitadlo = 0

def SolveCaptcha():
    start_time = time.time()
    seconds = 3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # SCREENSHOT
        im = pyautogui.screenshot()

        # CHECKING PHASE
        cap_pos = im.getpixel(CAPTCHA_POS)
        if cap_pos == CAPTCHA_COLOR:
            pyautogui.click(CAPTCHA_POS_CLICK)
            break
        if elapsed_time > seconds:
            main()
    main()


def StartWithdraw():
    start_time = time.time()
    seconds = 2

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # SCREENSHOT
        im = pyautogui.screenshot()

        # CHECKING PHASE
        withdraw_pos = im.getpixel(WITHDRAW_POS)
        if withdraw_pos == WITHDRAW_COLOR:
            pyautogui.click(WITHDRAW_POS)
            break

        if elapsed_time > seconds:
            main()
    SolveCaptcha()

def main():

    while True:
        # SCREENSHOT
        im = pyautogui.screenshot()

        # CHECKING PHASE
        b_pos1 = im.getpixel(px_blitz_1)
        if b_pos1 == BLITZ_COLOR:
            pyautogui.click(460, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos2 = im.getpixel(px_blitz_2)
        if b_pos2 == BLITZ_COLOR:
            pyautogui.click(645, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos3 = im.getpixel(px_blitz_3)
        if b_pos3 == BLITZ_COLOR:
            pyautogui.click(830, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos4 = im.getpixel(px_blitz_4)
        if b_pos4 == BLITZ_COLOR:
            pyautogui.click(1015, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos5 = im.getpixel(px_blitz_5)
        if b_pos5 == BLITZ_COLOR:
            pyautogui.click(1200, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos6 = im.getpixel(px_blitz_6)
        if b_pos6 == BLITZ_COLOR:
            pyautogui.click(1385, 612)
            time.sleep(0.06)
            StartWithdraw()

        b_pos7 = im.getpixel(px_blitz_7)
        if b_pos7 == BLITZ_COLOR:
            pyautogui.click(1570, 612)
            time.sleep(0.06)
            StartWithdraw()
print("Running...")
main()