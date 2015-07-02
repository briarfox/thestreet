from robobrowser import RoboBrowser

class BlockedException(Exception):
    pass

class FakeMail(object):
    def __init__(self):
        self.browser = RoboBrowser(history=True)
        self.browser.open('http://10minutemail.com/')
        with open('10minmail.txt', 'w') as f:
            f.write(str(self.browser.parsed))
        if self.browser.get_link('Blocked'):
            raise BlockedException('to many login Attempts')


    def get_address(self):
        address = self.browser.find("div", {"id": "copyAddress"})
        print address

    def read_mail(self):
        pass

if __name__ == '__main__':
    try:
        fakeMail = FakeMail()
        fakeMail.get_address()
    except BlockedException, e:
        print e