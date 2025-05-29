from pycomm3 import LogixDriver
from pycomm3.logger import configure_default_logger, LOG_VERBOSE

class CLP:

    def __init__(self, ip_address, log_file="rockwell.log"):
        self.plc = LogixDriver(ip_address)
        # configure_default_logger(level=LOG_VERBOSE, filename=log_file)
        
    def connect(self):
        self.plc.open()

    def read(self, tag_name):
        return self.plc.read(tag_name)




