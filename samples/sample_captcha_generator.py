from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

#audio = AudioCaptcha(voicedir='/path/to/voices')
audio = AudioCaptcha()

#image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])
image = ImageCaptcha()

#s='s'
#data = audio.generate(s)
#audio.write(s, 'out.wav')

data = image.generate('s')
image.write('  s', 'out1.png')
image.write(' s', 'out2.png')
image.write('   s', 'out3.png')
image.write('s', 'out4.png')
image.write('s', 'out5.png')
image.write('s', 'out6.png')
