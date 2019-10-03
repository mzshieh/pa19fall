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

pyautogui.typewrite('https://www.nctu.edu.tw')

# 4. 按下 Enter 鍵

pyautogui.press('enter')
