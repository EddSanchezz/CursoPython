import os
import sys
import pickle
import tempfile
import time
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from apps.Colores import *
from apps.Cursor_arriba import cursor_arriba
from buscador.Config_user import OPENAI_USER, OPENAI_PASS
from buscador.driver_indetectable import iniciar_webdriver_indetectable


class ChatGpt:
    def __init__(self, user, password):
        self.OPENAI_USER = user
        self.OPENAI_PASS = password
        self.COOKIES_FILE = os.path.join(tempfile.gettempdir(), "openai_cookies.enc")
        self.SECRET_KEY = self.generate_or_load_key()
        print(f"{azul}Iniciando webdriver{gris}")
        self.driver = iniciar_webdriver_indetectable(headless=False, pos="izquierda")
        self.wait = WebDriverWait(self.driver, 30)
        login = self.login_openai()
        if not login:
            print(f"{rojo}No se pudo iniciar sesión. Cerrando.{gris}")
            sys.exit(1)

    def generate_or_load_key(self):
        """Genera o carga una clave secreta para cifrar cookies."""
        key_file = os.path.join(tempfile.gettempdir(), "secret.key")
        if os.path.isfile(key_file):
            with open(key_file, "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as file:
                file.write(key)
            return key

    def save_encrypted_cookies(self, cookies):
        """Guarda cookies cifradas en un archivo."""
        fernet = Fernet(self.SECRET_KEY)
        with open(self.COOKIES_FILE, "wb") as file:
            file.write(fernet.encrypt(pickle.dumps(cookies)))

    def load_encrypted_cookies(self):
        """Carga cookies cifradas de un archivo."""
        if os.path.isfile(self.COOKIES_FILE):
            fernet = Fernet(self.SECRET_KEY)
            with open(self.COOKIES_FILE, "rb") as file:
                return pickle.loads(fernet.decrypt(file.read()))
        return None

    def login_openai(self):
        cookies = self.load_encrypted_cookies()
        if cookies:
            print(f"{azul}Iniciando sesión con cookies{gris}")
            self.driver.get("https://chat.openai.com/")
            for cookie in cookies:
                try:
                    self.driver.add_cookie(cookie)
                except Exception as e:
                    print(f"{amarillo}Error cargando cookie: {e}{gris}")
            self.driver.refresh()
            if self.comprobar_login():
                print(f"{verde}Inicio de sesión exitoso con cookies.{gris}")
                return True
            else:
                print(f"{rojo}Falló el inicio de sesión con cookies.{gris}")

        print(f"{azul}Iniciando sesión desde cero.{gris}")
        self.driver.get("https://chat.openai.com/")

        if not self.click_element((By.XPATH, "//div[text()='Iniciar sesión']")):
            return False

        if not self.input_text((By.XPATH, "/html/body/div/main/section/div[2]/div[1]/input"), self.OPENAI_USER):
            return False

        if not self.click_element((By.XPATH, "//button[text()='Continuar']")):
            return False

        if not self.input_text((By.XPATH, "/html/body/div/div[2]/main/section/div/div/div/form/div[1]/div/div[2]/div/input"), self.OPENAI_PASS):
            return False

        if not self.click_element((By.XPATH, "//button[text()='Continuar']")):
            return False

        if self.comprobar_login():
            print(f"{verde}Inicio de sesión exitoso desde cero.{gris}")
            self.save_encrypted_cookies(self.driver.get_cookies())
            return True

        print(f"{rojo}Inicio de sesión fallido.{gris}")
        return False

    def comprobar_login(self, tiempo=30):
        for _ in range(tiempo):
            try:
                if self.driver.find_element(By.CSS_SELECTOR, "textarea[tabindex='0']"):
                    return True
            except:
                pass
            print(f"{gris}Comprobando inicio de sesión...{gris}")
            time.sleep(1)
        return False

    def click_element(self, locator):
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.click()
            return True
        except Exception as e:
            print(f"{rojo}Error haciendo clic: {e}{gris}")
            return False

    def input_text(self, locator, text):
        try:
            element = self.wait.until(ec.presence_of_element_located(locator))
            element.send_keys(text)
            return True
        except Exception as e:
            print(f"{rojo}Error ingresando texto: {e}{gris}")
            return False


if __name__ == "__main__":
    chatgpt = ChatGpt(OPENAI_USER, OPENAI_PASS)
    input("Pausa...")
