import os
import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
    
except Exception:
    
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)