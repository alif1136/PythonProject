from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

v = Options()
v.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=v)

# implicit wait (সব element এর জন্য auto wait করবে)
driver.implicitly_wait(10)

driver.get("https://carwebsite-five.vercel.app/login")

# Login
driver.find_element(By.NAME, "email").send_keys("junayetshiblu09@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Search
search_box = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Search luxury cars, brands, models...']"
)

search_box.send_keys("Honda")
search_box.send_keys(Keys.ENTER)
product = driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/allproduct/67b6c0949192e5b68df248ef']"
)
product.click()
add_to_cart = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Add To Cart')]"
)
add_to_cart.click()
cart_button = driver.find_element(By.CSS_SELECTOR, "a[href='/cart']")  # or button
cart_button.click()
remove_button = driver.find_element(By.CLASS_NAME, "lucide lucide-trash2")
remove_button.click()