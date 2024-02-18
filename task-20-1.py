"""
click  the FAQ and Partners anchor tag present on the home page and open two new windows now,you have to fetch the opened frameID  and kindly close the new windows and come back to home page also
"""

from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementNotVisibleException
class Automationtesting:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def FAQ(self):
        """
        This method check whether FAQ anchor tag is clickable or not and after clicking anchor tag it redirect to another page
        :return:str
        """
        try:
           faq_link = self.driver.find_element(by=By.LINK_TEXT, value="FAQ")
           faq_link.click()
           print("FAQ link clicked")
           self.wait(5)
        except ElementNotVisibleException:
           print("Element is not visible")
    def partners(self):
        """
        This method check whether PARTNERS anchor tag is clickable or not and after clicking anchor tag it redirect to another page
        :return:partners link clicked
        """
        try:
           partners_link = self.driver.find_element(by=By.LINK_TEXT, value="PARTNERS")
           partners_link.click()
           print("partners link clicked")
           self.wait(5)
        except ElementNotVisibleException:
            print("element is not visible")
    def window_handle(self):
        """
        this method display of all  open windows
        :return: FRAME ID
        """
        self.window_handles = self.driver.window_handles
        for handle in self.window_handles:
            print("window", handle)
    def close_new_window(self):
        """
        this method close two new windows and come back to home page
        :return:None
        """
        for handle in self.window_handles[1:]:
            self.driver.switch_to.window(handle)
            self.driver.close()
        # switch back to the home page
        self.driver.switch_to.window(self.window_handles[0])
        self.wait(5)
        # close the home page
        self.driver.close()
    def wait(self,seconds):
        """
        this method hold on the screen as per given seconds
        :param seconds:
        :return:None
        """
        sleep(seconds)
    def quit(self):
        """
        this method quit the driver
        :return:None
        """
        self.driver.quit()
    def script(self):
       self.boot()
       self.FAQ()
       self.partners()
       self.window_handle()
       self.close_new_window()

url = "https://www.cowin.gov.in/"
obj = Automationtesting(url)
obj.script()


