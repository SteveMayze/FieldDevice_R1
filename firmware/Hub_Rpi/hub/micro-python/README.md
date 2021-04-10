


https://docs.micropython.org/en/latest/esp8266/quickref.html#networking

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    

import webrepl_setup

import webrepl
webrepl.start()


micropythoN