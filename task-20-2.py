"""
Goto the menu whose name is documents and  monthly progress report and download it
"""


from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# Exception
from selenium.common.exceptions import NoSuchElementException

# Alerts
from selenium.webdriver.common.alert import Alert
#import requests
import requests
class LabourEmployee:

     def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def boot(self):
        """
        This method open the url and maximize the window
        :return:None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

     def findElement(self):
      """
      This method find the element from  webpage. it find documents and monthly progress report anchor tdg

      :return: None
      """
      try:

          document_link = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/nav/div/div/div/ul/li[7]/a")
          achains = ActionChains(self.driver)
          achains.move_to_element(document_link).perform()
          document_submenu = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/nav/div/div/div/ul/li[7]/ul/li[2]/a")
          document_submenu.click()
          sleep(10)

      except NoSuchElementException:
          #particular element is not there then this block is execute
         print(" The element is not present")

     def alertAccept(self):
         """
         This method accept the pop-up box
         :return:None
         """
         downloadbutton = self.driver.find_element(by=By.XPATH,value="/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a")
         downloadbutton.click()
         alert = Alert(self.driver)
         alert.accept()
         sleep(15)

     def window_Handle(self):
         """
         This method give current url of the webpage
         :return:None
         """
         self.window_handles = self.driver.window_handles
         self.driver.switch_to.window(self.window_handles[1])
         self.current_url=self.driver.current_url
         sleep(5)


     def downloadMonthlyProgressReport(self):
         """
         This method download the monthly progress  report
         :return:
         """
         url=self.current_url
         response =requests.get(url)
         if response.status_code == 200:
          with open(r"C:\Users\dines\PycharmProjects\selenium introduction\monthly progress report.txt","wb") as file:
              file.write(response.content)
              print("download is complete")
         else:
             print("error")

     def close(self):
         """
         This method close the driver
         :return:
         """
         self.driver.quit()




url = "https://labour.gov.in/"
obj = LabourEmployee(url)
obj.boot()
obj.findElement()
obj.alertAccept()
obj.window_Handle()
obj.downloadMonthlyProgressReport()

