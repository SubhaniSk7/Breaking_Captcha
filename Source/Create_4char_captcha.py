from captcha_master.captcha.image import ImageCaptcha
import string
import random

image = ImageCaptcha(width=365, height=128, fonts=None, font_sizes=(90, 90, 90), noise_point=120)
alphabets = list(string.ascii_uppercase)
for i in range(1000):
    chars = ''
    for j in range(4):
        chars += alphabets[random.randint(0,25)]
    data = image.generate(chars)
    image.write(chars, 'Test4char/' + chars + '.png')

