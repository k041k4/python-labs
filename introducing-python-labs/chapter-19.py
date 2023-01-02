# logging
import logging

log_format = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='./introducing-python-labs/chapter-19.log', format=log_format) # setting up to level logging and log file
logger = logging.getLogger('Pozorovatel')

#log messages
logger.debug('debug logging')
logger.info('just an info')
logger.warning('This is a serious warning!')
logger.error('We have an error...')
logger.critical('critical problem , this not a drill!')
