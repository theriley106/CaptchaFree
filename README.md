# CaptchaFree

CaptchaFree is a Selenium WebDriver wrapper that automatically solves reCAPTCHA using a local version of OpenAI's Whisper model. This tool seamlessly integrates with any Selenium WebDriver instance, enabling you to automate web interactions without the hassle of reCAPTCHA interruptions.

## How are we solving captcha?

ChromeFree uses OpenAI's Whisper model to solve reCAPTCHA by converting audio CAPTCHA challenges into text. The audio CAPTCHA is downloaded and transcribed locally using the Whisper model, which then provides the text input to bypass the CAPTCHA. This process runs continuously in the background, ensuring automated CAPTCHA solving for any site visited. For a visual demonstration, check out [this video](https://www.youtube.com/watch?v=P7u81RLiPQA).

## Installation

To install CaptchaFree, use pip:

```bash
pip install captcha_free
```

## Usage

Here is an example of how to use CaptchaFree with a Selenium WebDriver:

```python
from captcha_free import CaptchaFree
from selenium import webdriver

# Wrap any selenium webdriver in the CaptchaFree class
driver = CaptchaFree(webdriver.Chrome())

# Go to a website that uses reCAPTCHA
driver.get("https://patrickhlauke.github.io/recaptcha/")

# All existing Selenium Webdriver class methods work as expected
driver.close()
```

## Contributing

Feel free to submit issues and pull requests for new features, bug fixes, or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.