class iPhone6:
    def home(self):
        print('Home button pressed')


class iPhoneX(iPhone6):
    def home(self):
        print('Home button touched')


i6 = iPhone6()
ix = iPhoneX()

i6.home()
ix.home()
