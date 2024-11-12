import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def iniciar_chrome():
    ruta = ChromeDriverManager().install()
    options = Options()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
    options.add_argument(f"user-agent={user_agent}")

    options.add_argument("--window-size=500,1080")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port=9222")

    exp_opt = [
        "enable-automation",
        "ignore-certificate-errors",
        "enable-logging"
    ]
    options.add_experimental_option("excludeSwitches", exp_opt)

    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languages": ["en-US", "en"],
        "credentials_enable_service": False
    }
    options.add_experimental_option("prefs", prefs)

    s = Service(ruta)
    driver = webdriver.Chrome(service=s, options=options)
    driver.set_window_position(0, 0)
    time.sleep(3)
    return driver
