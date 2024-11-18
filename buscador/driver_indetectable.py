import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Config import GOOGLE_USER, GOOGLE_PASS

def iniciar_webdriver_indetectable(headless=False, pos="maximizada"):
    option = uc.ChromeOptions()
    option.add_argument("--password-store=basic")
    option.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    # Agregar el argumento explícito si headless es True
    if headless:
        option.add_argument("--headless=new")

    driver = uc.Chrome(options=option, log_level=3)

    if not headless:
        driver.maximize_window()
        if pos != "maximizada":
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                driver.set_window_rect(x=0, y=0, width=ancho // 2, height=alto)
            if pos == "derecha":
                driver.set_window_rect(x=ancho // 2, y=0, width=ancho // 2, height=alto)
    return driver

def login_google():
    driver = iniciar_webdriver_indetectable(headless=False, pos="maximizada")
    wait = WebDriverWait(driver, 30)
    driver.get("https://accounts.google.com/")
    
    # Campo de correo
    e = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
    e.send_keys(GOOGLE_USER)
    e.send_keys(Keys.ENTER)
    
    # Campo de contraseña
    e = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    e.send_keys(GOOGLE_PASS)
    e.send_keys(Keys.ENTER)

    time.sleep(15)
    
    return driver

#login_google()
