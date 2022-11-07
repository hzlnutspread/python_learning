import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('time_test.log', when='s', interval=5,
                                   backupCount=5)  # when=m means when should it roll over. m = minute, s = second h = hours d = day
logger.addHandler(handler)

for _ in range(6):
    logger.info('hello, world')
    time.sleep(5)