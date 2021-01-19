import time

window.activate('gedit', switchDesktop=True)
window.resize_move('gedit', xOrigin=0, yOrigin=0, width=200, height=200, matchClass=False)
keyboard.send_keys("<alt>+<F8>")

keyboard.press_key('<alt>')
keyboard.press_key('<f8>')
keyboard.release_key('<alt>')
keyboard.release_key('<f8>')

keyboard.press_key('<down>')
time.sleep(4)
keyboard.release_key('<down>')

keyboard.press_key('<right>')
time.sleep(4)
keyboard.release_key('<right>')

# mouse buttons: left=1, middle=2, right=3
mouse.click_relative_self(5120, 100, 3)

#geo = window.get_active_geometry()
#    winGeometry = 'X-origin: %s\nY-origin: %s\nWidth: %s\nHeight: %s'  %(geo[0], geo[1], geo[2], geo[3])
#    dialog.info_dialog(title='Window geometry', message=winGeometry)
    
#winClass = window.get_active_class()
#dialog.info_dialog(title='Window class', message=winClass)