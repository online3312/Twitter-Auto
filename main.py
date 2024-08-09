from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximize window on startup
    service = Service(executable_path="path/to/chromedriver")  # Replace with your path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_to_twitter(driver, username, password):
    driver.get("https://twitter.com/login")

    try:
        # Wait for username field and input username
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        ).send_keys(username + Keys.RETURN)

        # Wait for password field and input password
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(password + Keys.RETURN)

        # Wait for the main page to load and verify login
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="SideNav_AccountSwitcher_Button"]'))
        )
        print("Logged in successfully!")

    except Exception as e:
        print(f"An error occurred during login: {e}")
        driver.quit()
        exit()

def follow_user(driver, username):
    baseurl = "https://x.com/"
    url = baseurl + username
    driver.get(url)

    try:
        # Wait for the follow button to be clickable and click it
        follow_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="follow"]'))
        )
        follow_button.click()
        print(f"Followed {username} successfully!")

    except Exception as e:
        print(f"An error occurred while following the user: {e}")

    finally:
        # Wait a bit before closing
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    username = input("Enter your Twitter username: ")
    password = input("Enter your Twitter password: ")
    target_user = input("Enter the username to follow: ")

    login_to_twitter(driver, username, password)
    follow_user(driver, target_user)
