import pyautogui

# 当前位置
print(pyautogui.position())

# 当前屏幕分辨率
print(pyautogui.size())

# 移动到指定位置
pyautogui.moveTo(566, 566, duration=0.5)

# 点击
pyautogui.click()

# 输入
pyautogui.typewrite('Hello world!\n', interval=0.2)

# 截图
pyautogui.screenshot("screenshot.png")

# 弹出框
pyautogui.alert('This displays some text with an OK button.')


