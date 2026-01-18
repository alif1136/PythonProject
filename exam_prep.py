from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- Browser Setup ----------
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

driver.get("https://carwebsite-five.vercel.app/login")

# ---------- LOGIN ----------
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(
    "junayetshiblu09@gmail.com"
)
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# ---------- WAIT FOR DASHBOARD ----------
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "input[placeholder*='Search']")
))

# ---------- SEARCH & ADD MULTIPLE PRODUCTS ----------
cars = ["Honda", "BMW", "Audi"]

for car in cars:
    search_box = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder*='Search']")
    ))
    search_box.clear()
    search_box.send_keys(car)
    search_box.send_keys(Keys.ENTER)

    # wait product list
    product = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a[href^='/allproduct/']")
    ))
    product.click()

    add_to_cart = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Add To Cart')]")
    ))
    add_to_cart.click()

    time.sleep(2)
    driver.back()
    time.sleep(2)

# ---------- GO TO CART ----------
cart_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "a[href='/cart']")
))
cart_button.click()

# ---------- REMOVE ALL ITEMS ----------
while True:
    try:
        remove_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Remove item']")
        ))
        remove_button.click()
        time.sleep(1)
    except:
        break

# ---------- LOGOUT ----------
profile_btn = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[aria-label='profile']")
))
profile_btn.click()

logout_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Logout')]")
))
logout_btn.click()

print("✅ TEST COMPLETED SUCCESSFULLY")
