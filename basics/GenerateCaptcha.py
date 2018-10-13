from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

#audio = AudioCaptcha(voicedir='/path/to/voices')
audio = AudioCaptcha()

#image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])
image = ImageCaptcha()

data = audio.generate('1234')
# audio.write('1234', 'out.wav')

data = image.generate('subhani')
image.write('Subhani', './../outputFiles/generatedCaptchas/out1.png')
image.write('Subhani', './../outputFiles/generatedCaptchas/out2.png')
image.write('Dhruv Kaushik', './../outputFiles/generatedCaptchas/out3.png')
image.write('Gurpreet Singh', './../outputFiles/generatedCaptchas/out4.png')