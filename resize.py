import time

window.activate('Development', switchDesktop=True)
window.resize_move('Development', xOrigin=-25, yOrigin=-25, width=200, height=200, matchClass=False)

keyboard.press_key('<alt>')
keyboard.press_key('<f8>')
keyboard.release_key('<alt>')
keyboard.release_key('<f8>')

keyboard.press_key('<shift>')

keyboard.press_key('<down>')
time.sleep(3)
keyboard.release_key('<down>')

keyboard.press_key('<right>')
time.sleep(5)
keyboard.release_key('<right>')
keyboard.release_key('<shift>')

# mouse buttons: left=1, middle=2, right=3
mouse.click_relative_self(100, 100, 3)
