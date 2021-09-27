from appium import webdriver
import time

desired_caps = {
    "platformName": "android",
    "deviceName": "emulator-5554",
    "appWaitForLaunch": "false",
    "app": "D:\\Internship\\Python Automation using appium\\app-debug.apk"


}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(1)
driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
time.sleep(2)
driver.find_element_by_id("com.ATG.World:id/login_email").click()
time.sleep(2)
email = driver.find_element_by_id("com.ATG.World:id/email")
email.send_keys("wiz_saurabh@rediffmail.com")
time.sleep(2)
password = driver.find_element_by_id("com.ATG.World:id/password")
password.send_keys("Pass@123")
time.sleep(4)
driver.find_element_by_id("com.ATG.World:id/email_sign_in_button").click()
time.sleep(5)
print("Successful")