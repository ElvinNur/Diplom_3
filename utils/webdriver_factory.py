from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    @staticmethod
    def get_driver(browser_type):
        if browser_type == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--force-device-scale-factor=0.8")
            driver = webdriver.Chrome(options=options)
            return driver
        elif browser_type == "firefox":
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            options.set_preference("layout.css.devPixelsPerPx", "0.8")
            driver = webdriver.Firefox(options=options)
            return driver
        else:
            raise ValueError(f"Неизвестный тип браузера: {browser_type}")
