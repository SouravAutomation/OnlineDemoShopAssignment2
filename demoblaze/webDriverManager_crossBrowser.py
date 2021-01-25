import keyboard as keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import time

browserName = 'chrome'     # Browser choice is made here
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager.install())
elif browserName == "opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    print("Please pass the correct browser name, current value is : " + browserName)
    raise Exception("Driver missing. Please pass correct browser name.")

driver.implicitly_wait(5)
driver.delete_all_cookies()
driver.get('https://www.demoblaze.com/index.html')

# print(driver.title)
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 350)")
#driver.implicitly_wait(5)
CATEGORIES = driver.find_element(By.XPATH, "//a[@id='cat']")
CATEGORIES.click()  # Category Navigation
Phones = driver.find_element(By.XPATH, "//a[contains(text(),'Phones')]")
# Phones.click()
Monitors = driver.find_element(By.XPATH, "//a[contains(text(),'Monitors')]")
# Monitors.click()
Laptops = driver.find_element(By.XPATH, "//a[contains(text(),'Laptops')]")
Laptops.click()   # Navigate to Laptop
driver.execute_script("window.scrollTo(0, 500)")  # Scroll down to view list of Laptops

# Add Sony Vivo i5
vivo = driver.find_element(By.XPATH, "//a[contains(text(),'Sony vaio i5')]")
vivo.click()
addToCart = driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]")
addToCart.click()
time.sleep(1)

try:
    alert = driver.switch_to.alert
    # print(alert.text)
    alert.accept()   # Accepts
except:
    print("no alert to accept")

# keyboard.press_and_release('Enter')   # Accepts the popup
Home = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
Home.click()
time.sleep(2)

#Add dell i7 8gb
driver.find_element(By.XPATH, "//a[contains(text(),'Laptops')]").click()
dell = driver.find_element(By.XPATH, "//a[contains(text(),'Dell i7 8gb')]")
dell.click()
driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()  # Adds item to cart
# driver.switch_to.alert.accept()
time.sleep(1)
try:
    alert = driver.switch_to.alert
    # print(alert.text)
    alert.accept()   # Accepts
except:
    print ("no alert to accept")
# keyboard.press_and_release('Enter')   # Accepts the popup
Cart = driver.find_element(By.XPATH, "//a[@id='cartur']")
Cart.click()    # Navigate to Cart

# before_xpath = str('//*[@id="tbodyid"]/tr[')
# after_xpath = str(']/td[2]')
# for r in range(1, 3):
 #   value = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr["+str(r)+"]/td[2]').text
    # value = driver.find_element(By.XPATH ('before_xpath++str(r)+after_xpath')).text
  #  print(value)

# rows = len(driver.find_elements_by_xpath('//*[@id="tbodyid"]/tr/td[1]'))
# cols = len(driver.find_elements_by_xpath('//*[@id="tbodyid"]/tr[1]/td'))
# print(rows)
# print(cols)
# for r in range(1, rows+2):
    # value = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr["+str(r)+"]/td[2]').text
    # print(value)

# Delete Dell laptop from Cart
value = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text
#print(value)
dele = "Dell i7 8gb"
if (dele in value):
    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
else:
    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr[2]/td[4]/a').click()
time.sleep(5)

PlaceOrder = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
PlaceOrder.click()
time.sleep(1)
# Fill general form with test data
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Sourav Kumar")
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Gurugram")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='card']").send_keys("123456789098")
driver.find_element(By.XPATH, "//input[@id='month']").send_keys("12")
driver.find_element(By.XPATH, "//input[@id='year']").send_keys("2022")
Purchase = driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
Purchase.click()
time.sleep(1)
driver.save_screenshot("orderDetailsSnip.png")
info = driver.find_element(By.XPATH, "/html/body/div[10]/p").text
#print(info)

print(info[:27])

purchaseAmount = (info.partition("Amount: ")[2].partition(" USD")[0])
#print(purchaseAmount)
expectedAmount = "790"
assert (purchaseAmount == expectedAmount), "Purchase amount does not match"
print("Purchase amount equals expected")

driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()




