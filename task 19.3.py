from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
paths = r"driver = webdriver.Chrome('/path/to/chromedriver')"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
import time

# Navigate to the URL
driver.get("https://www.saucedemo.com/")

# Locate the username and password fields and login button
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter credentials and log in
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Wait for the page to load
time.sleep(5)  # This is a simple way to wait for the page to load

# Fetch the title and current URL of the webpage
page_title = driver.title
current_url = driver.current_url

# Extract the entire contents of the webpage
page_source = driver.page_source

# Save the extracted content to a text file
with open(r"C:\Users\Merlin Archana\OneDrive\Desktop\upload\new task\webpage_tasl_11.txt", "w", encoding="utf-8") as file:
    file.write(f"Page Title: {page_title}\n")
    file.write(f"Current URL: {current_url}\n\n")
    file.write("Page Source:\n")
    file.write(page_source)
print(f"Page Title: {page_title}")
print(f"Current URL: {current_url}")


