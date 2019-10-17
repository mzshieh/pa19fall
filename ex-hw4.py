# 0. 引入所需要使用的套件，並初始化
#### 我要 pyautogui 並且指令間隔為 1 秒
import pyautogui
pyautogui.PAUSE = 0.5

#### 我還要 sleep function
#### 等待就是睡覺
from time import sleep

# 1. 打開小畫家

pyautogui.hotkey('win','r')
pyautogui.typewrite('mspaint')
pyautogui.press('enter')
# 或許需要忍一下，睡 3.21 秒
sleep(0.71)
pyautogui.hotkey('win','up') # 最大化

# 2. 畫六文錢
#### 一文錢畫六次，但要畫在正確的大小跟地方

# 2.0 先準備畫 一文錢的 function
##### 左上角 (x, y) 長寬 size
def ichimonsen(x, y, size):
    # 先畫一文錢的圓
    ##  選到圓 (橢圓)
    pyautogui.click(423, 65)
    ### 拉一個圓
    pyautogui.moveTo(x,y)
    pyautogui.dragRel(size, size, 0.3)
    # 再畫一文錢的方孔
    ## 選到矩形
    pyautogui.click(441, 64)
    ### 拉一個正方形
    pyautogui.moveTo(x+size//3, y+size//3)
    pyautogui.dragRel(size//3, size//3, 0.3)
    # 記得填滿
    ## 選到填滿工具
    pyautogui.click(270,75)
    ## 點一下圓跟正方形之間
    pyautogui.click(x+size//2,y+size//4)
    return

# 其實是要畫六次一文錢，但是位置不太一樣
# 左上角的 x 座標有 200, 320, 440
# 左上角的 y 座標有 200, 320
# 大小 90 應該差不多吧

# 東西很少可以直接用袋子裝資料
# for x in [200, 320, 440]:
#     for y in [200, 320]:
# 東西很多要考慮用數學生資料
for i in range(3):
    for j in range(2):
        x = 200 + 120 * i
        y = 200 + 120 * j
        ichimonsen(x, y, 110)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        