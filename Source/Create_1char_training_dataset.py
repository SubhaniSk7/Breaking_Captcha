from captcha_master.captcha.image import ImageCaptcha
import string
import random

image = ImageCaptcha(width=128, height=128, fonts=None, font_sizes=(90, 90, 90), noise_point=40)
alphabets = list(string.ascii_uppercase)
for i in range(25000):
    char = alphabets[random.randint(0,25)]
    data = image.generate(char)
    image.write(char, 'Dataset/' + char + str(i) + '.png')

