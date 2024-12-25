#Write your tests here
import os
import sys

# Append the parent directory
sys.path.append(os.path.abspath('..'))


from Backend import settings
ile_name = os.listdir(settings.MEDIA_ROOT)
import random
print(random.choice(ile_name))