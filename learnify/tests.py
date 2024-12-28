import sys
sys.path.append('..')
import os
from Backend import settings
#from .ai.ai_gen_quiz_model import quiz_engine

from datetime import datetime
date_time = datetime.now()
time = date_time.time()
print(time.strftime('%H-%M'))
if l_ist:=len(os.listdir('{}/quiz'.format(settings.MEDIA_ROOT))) == 1:
    print(l_ist)
