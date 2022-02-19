import os
import uuid
import logging
import logging.handlers
from datetime import datetime


class WhetstoneLogger(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when = 'midnight', interval=1, backupCount = 0, encoding=None, delay=False, utc = False, postfix = '.log'):

        self.filename = filename
        self.when = when
        self.interval = interval
        self.backupCount = backupCount
        self.utc = utc
        self.postfix = postfix
        self.uuid = str(uuid.uuid4()).split('-')[0]

    def doRollover(self):
        pass



class WhetstoneBatchLogger(logging.handlers.FileHandler):
    def __init__(self, f):
        pass

    def doRollover(self):
        pass