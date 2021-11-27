import time
import pywinauto
from pywinauto.application import Application

app = Application(backend='uia').start('putty.exe')
time.sleep(2)
window = app.PuTTYConfigBox
window.set_focus()
window[u'Host Name (or IP adress):Edit'].type_keys('192.168.100.1')
window[u'Port:Edit'].set_text('21')
time.sleep(2)
window["Open"].click()