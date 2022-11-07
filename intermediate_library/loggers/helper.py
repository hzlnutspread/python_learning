import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')
# logger.propagate = False  # will not propagate to the base layer (root)
# logger.info('hello from helper')


# # create handler
# stream_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('file.log')
#
# # level and format for each handler
# stream_handler.setLevel(logging.WARNING)
# file_handler.setLevel(logging.ERROR)
#
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)
#
# logger.warning('this is a warning')
# logger.error('this is an error')
