from selenium_addons import Record
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import cv2
service = Service(
    "C:/Users/Roshan Yadav/Documents/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
try:
    driver.get("chrome://dino")
except:
    pass
driver.maximize_window()
# to capture whole screen pass driver object as below OR to capture element pass webelement object
window = Record(driver, file_name="firearch")

while True:
    frame = window.get_frame()  # Get New Frame
    if frame is False:
        cv2.destroyAllWindows() # if cv2.imshow is used

        # if browser closed or quit (window.get_frame() return False ) then save captured frames and break loop
        window.save()
        break
    cv2.imshow("image",frame) # to show captured frame live

    # capture coming frame
    window.capture()
