from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/")
    print("Page title:", driver.title)

    assert "Selenium" in driver.title
    print("PASS: Selenium test successful!")

finally:
    driver.quit()
