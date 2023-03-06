from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webDriver.Firefox()

# Navigate to the online store
driver.get("https://example.com")

# Find the search bar and enter a search query
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("Product Name")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

 
# Check that the search results contain the expected product
search_results = driver.find_elements_by_class_name("search-result")
assert any("Product Name" in result.text for result in search_results)

# Click on the product to go to its detail page 
product_link = driver.find_element_by_xpath("//a[contains(text(), 'Product Name')]")
product_link.click()

# Wait for the product page to load
wait.until(EC.presence_of_element_located((By.ID, "product-detail")))

# Check that the product page contains the expected product name and and price 
product_name = driver.find_element_by_xpath("//h1[contains@class, 'product-name')]")
assert product_name.text == "Product name"
product_price = driver.find_elment_by_xpath(//span[contains@class, 'product-price')]")
assert product_price.text = "$19.99"

# Add the product to the cart 
add_to_cart_button = driver.find_element_by_xpath("//button[contains@class, 'add-to-cart')]")
add_to_cart_button.click()

# Wait for the cart to update
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-items-count), "1"))


# Check that the cart contains the expected product
cart_items = driver.find_elements_by_class_name("cart-item")
assert any("Product Name" in item.text for item in cart_items)


#Close the browser window
driver.quit
