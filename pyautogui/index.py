from time import sleep
import pygetwindow as gw

# 获取当前活动窗口
active_window = gw.getActiveWindow()

print('active_window.title:'+active_window.title)
print('active_window.size:'+str(active_window.size))
print('active_window.left:'+str(active_window.left))
print('active_window.top:'+str(active_window.top))
print('active_window.right:'+str(active_window.right))
print('active_window.bottom:'+str(active_window.bottom))
print('active_window.width:'+str(active_window.width))
print('active_window.height:'+str(active_window.height))
print('active_window.isMaximized:'+str(active_window.isMaximized))
print('active_window.isMinimized:'+str(active_window.isMinimized))

active_window.activate()

active_window.restore()

active_window.resizeTo(800, 600)

active_window.moveTo(100, 100)

# active_window.maximize()

# active_window.minimize()



# 最小化窗口
# active_window.minimize()
# sleep(2)
# active_window.activate()
