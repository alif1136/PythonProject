from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

v = Options()
v.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=v)
driver.implicitly_wait(10)

# Website open
driver.get("https://carwebsite-five.vercel.app/login")
time.sleep(2)

# ---------- Login ----------
driver.find_element(By.NAME, "email").send_keys("junayetshiblu09@gmail.com")
time.sleep(1)

driver.find_element(By.NAME, "password").send_keys("123456")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)   # login successful dekhte

# ---------- Search ----------
search_box = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Search luxury cars, brands, models...']"
)
search_box.send_keys("Honda")
time.sleep(1)

search_box.send_keys(Keys.ENTER)
time.sleep(3)   # search result dekhte

# ---------- Product Click ----------
product = driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/allproduct/67b6c0949192e5b68df248ef']"
)
product.click()
time.sleep(3)

# ---------- Add To Cart ----------
add_to_cart = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Add To Cart')]"
)
add_to_cart.click()
time.sleep(2)

# ---------- Cart ----------
cart_button = driver.find_element(By.CSS_SELECTOR, "a[href='/cart']")
cart_button.click()
time.sleep(3)

# ---------- Remove Item ----------
del_button = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Remove item']"
)
del_button.click()
time.sleep(2)

# ---------- Logout ------
driver.find_element(
    By.XPATH,
    "//span[contains(@class,'bg-muted')]"
).click()
time.sleep(3)
logout_btn = driver.find_element(
    By.XPATH, "//div[contains(text(),'Logout')]"
)
logout_btn.click()

time.sleep(2)

print("✅ Test completed successfully")