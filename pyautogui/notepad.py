import pyautogui
# 移动鼠标到屏幕中心
pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2)
# 在后台打开Notepad程序，并等待几秒钟
pyautogui.press('win')
pyautogui.typewrite('Notepad')
pyautogui.press('enter')
pyautogui.sleep(1)
# 在Notepad中输入一段文本，并保存
pyautogui.typewrite('Hello, world!')
pyautogui.hotkey('ctrl', 's')
# 切换至英文输入法
pyautogui.hotkey('shift')
pyautogui.typewrite('test.txt')
pyautogui.press('enter')
