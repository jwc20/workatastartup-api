from .core import *
from .companies import Companies
from .login import LogIn

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=500,1020")
# options.add_argument('--disable-gpu')
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

class WorkAtAStartUp(Companies, LogIn):
    def __init__(self, query=[], *args):
        self.driver = webdriver.Chrome(options=options)
        Companies.__init__(self, query=query, *args)
        LogIn.__init__(self, *args)



__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"
