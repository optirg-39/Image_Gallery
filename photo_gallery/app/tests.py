from django.test import TestCase
from PIL import Image as PilImage
# Create your tests here.


plimg = PilImage.open('Swamiji_kYqSK6t.jpg')
image = plimg.rotate(90)
image.show()
