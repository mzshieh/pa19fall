# 0. 載入所有需要的工具、模組等等，並做基礎設定
import pyautogui
pyautogui.PAUSE = 1

# 1. 打開瀏覽器

pyautogui.hotkey('win','r')
# pyautogui.press('shift') # 如果會卡中文輸入法，請記得切換，可去除開頭 #
pyautogui.typewrite('chrome')
pyautogui.press('enter')

# 2. 點擊網址列

pyautogui.click(146,52)

# 3. 輸入網址

pyautogui.typewrite('https://www.geogebra.org/classic')

# 4. 按下 Enter 鍵

pyautogui.press('enter')

# 5.0 拖延時間，等網頁應用程式載入

pyautogui.moveRel(0, 0, 5)

# 5.1 點擊游標選項，換手寫筆

pyautogui.click(22,99)
pyautogui.click(20,238)

# 6. 移動到作畫區

pyautogui.moveTo(901,223)

# 7. 拉出三條邊

pyautogui.dragRel(50,100,3)
pyautogui.dragRel(-100,0,3)
pyautogui.dragRel(50,-100,3)

































