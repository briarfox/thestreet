from robobrowser import RoboBrowser

def get_report(ticker):
    browser = RoboBrowser(history=True)
    browser.open('http://www.thestreet.com/')
    with open('thestreet.txt', 'w') as f:
        f.write(str(browser.parsed))

if __name__ == '__main__':
    get_report('ORCL')