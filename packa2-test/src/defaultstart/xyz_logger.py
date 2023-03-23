 #!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Default Python script , should be called as a first import in every other Python script

Usage
----------
import default_start : direct import as a first import inevery script

Parameters
----------
None
'''
import logging
import logging.config
from colorlog import ColoredFormatter

#Logging

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(log_color)s%(levelname)-8s%(reset)s %(asctime)s %(log_color)s%(message)s%(reset)s"
LOG_DATE_FORMAT = '%H:%M:%S'
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOG_FORMAT, LOG_DATE_FORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)
