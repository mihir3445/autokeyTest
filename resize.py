import time

application='Development'
window.activate(application, switchDesktop=True)
window.resize_move(application, xOrigin=-25, yOrigin=-25, width=500, height=500, matchClass=False)

# resiz the window
keyboard.press_key('<alt>')
keyboard.press_key('<f8>')
keyboard.release_key('<alt>')
keyboard.release_key('<f8>')

#fast scale window
keyboard.press_key('<shift>')

#maximize vertically
keyboard.press_key('<down>')
time.sleep(3)
keyboard.release_key('<down>')

#maximize horizontally
keyboard.press_key('<right>')
time.sleep(3)
keyboard.release_key('<right>')
keyboard.release_key('<shift>')

keyboard.press_key('<f11>')
time.sleep(0.03)
keyboard.release_key('<f11>')

time.sleep(0.3)

keyboard.press_key('<f11>')
time.sleep(0.03)
keyboard.release_key('<f11>')

# mouse buttons: left=1, middle=2, right=3
mouse.click_relative_self(100, 100, 1)




