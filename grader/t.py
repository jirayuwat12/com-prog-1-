from pynput.keyboard import Key,Controller
import time
t = 2243
keyboard = Controller()
time.sleep(3)
keyboard.type(f'fill -2133 62 {t} -2263 31 {t-4} air replace minecraft:kelp_plant')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.type(f'fill -2133 62 {t} -2263 31 {t-4} air replace seagrass\n')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.type(f'fill -2133 62 {t} -2263 31 {t-4} air replace tall_seagrass\n')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.type(f'fill -2133 62 {t} -2263 31 {t-4} air replace water\n')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

t -= 4
print('startting....')
time.sleep(2)