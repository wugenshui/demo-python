import pyautogui
# 使用pyautogui打开计算器输入10+5=，然后按回车键计算结果
# 打开计算器
pyautogui.hotkey('winleft')
pyautogui.typewrite('calc\n', interval=0.25)
# 等待计算器打开
pyautogui.sleep(1)
# 输入10
pyautogui.typewrite('10')
# 点击+
pyautogui.click(x=160, y=380)
# 输入5
pyautogui.typewrite('5')
# 点击=
pyautogui.click(x=400, y=380)
# 点击回车
pyautogui.press('enter')
# 等待结果
pyautogui.sleep(1)
