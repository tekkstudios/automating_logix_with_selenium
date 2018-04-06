"""This is a class and method for converting literal values
into unicode num pad values that exist in in the Keys class
provided by selenium."""
from selenium.webdriver.common.keys import Keys

"""Class converts numbers"""
class NumConvert:
    """Method converts string objects into a format that can be
    interpreted by selenium webdriver."""
    def convert(self, string):
        new_stuff = []
        stuff = list(string)
        for i in stuff:
            if '0' == i:
                new_stuff.append(Keys.NUMPAD0)
            elif '1' == i:
                new_stuff.append(Keys.NUMPAD1)
            elif '2' == i:
                new_stuff.append(Keys.NUMPAD2)
            elif '3' == i:
                new_stuff.append(Keys.NUMPAD3)
            elif '4' == i:
                new_stuff.append(Keys.NUMPAD4)
            elif '5' == i:
                new_stuff.append(Keys.NUMPAD5)
            elif '6' == i:
                new_stuff.append(Keys.NUMPAD6)
            elif '7' == i:
                new_stuff.append(Keys.NUMPAD7)
            elif '8' == i:
                new_stuff.append(Keys.NUMPAD8)
            elif '9' == i:
                new_stuff.append(Keys.NUMPAD9)
            else:
                new_stuff.append(i)
        return ''.join(new_stuff)
