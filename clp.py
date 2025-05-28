from pycomm3 import LogixDriver
from pycomm3.logger import configure_default_logger, LOG_VERBOSE, LOG_DEBUG


class CLP:

    def init(self, ip_address, log_file="rockwell.log"):
        self.plc = LogixDriver(ip_address)
        configure_default_logger(level=LOG_DEBUG, filename=log_file)
        
    def connect(self):
        self.plc.open()

    def read(self, tag_name):
        return self.plc.read(tag_name)




