import threading
from selenium.webdriver.common.by import By
import requests
import whisper
import warnings
import time
import tempfile

warnings.filterwarnings("ignore")

model = whisper.load_model("base")

def transcribe(url):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=True) as temp_audio:
        temp_audio.write(response.content)
        temp_audio.flush()
        result = model.transcribe(temp_audio.name)
    return result["text"].strip()

def scan_for_captchas_on_page(driver, refresh_interval=1):
    while True:
        try:
            driver.switch_to.default_content()
            captchas = fetch_captchas(driver)
            if len(captchas) > 0:
                captcha_element = captchas[0]
                click_checkbox(driver, captcha_element)
                time.sleep(1)
                request_audio_version(driver)
                time.sleep(1)
                solve_audio_captcha(driver)

        except Exception as exp:
            pass
        time.sleep(refresh_interval)

def fetch_captchas(driver):
    captchas_on_page = []
    for captcha_element in driver.find_elements(By.XPATH, ".//iframe[@title='reCAPTCHA']"):
        driver.switch_to.frame(captcha_element)
        status = driver.find_elements(By.ID, "recaptcha-accessible-status")
        if len(status) == 0 or status[0].get_attribute('innerHTML') != 'You are verified':
            captchas_on_page.append(captcha_element)
        driver.switch_to.default_content()
    return captchas_on_page

def click_checkbox(driver, captcha_element):
    driver.switch_to.default_content()
    driver.switch_to.frame(captcha_element)
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    text = transcribe(driver.find_element(By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()
    time.sleep(5)

class CaptchaFree:
    def __init__(self, driver):
        self.driver = driver
        self.captcha_thread = threading.Thread(target=scan_for_captchas_on_page, args=(self.driver,))
        self.captcha_thread.daemon = True
        self.captcha_thread.start()

    def __getattr__(self, name):
        return getattr(self.driver, name)

if __name__ == "__main__":
    pass
