import logging
import os

class Logger:
    def __init__(self):
        self.create_log()
    def create_log(self):
        self.ensure_log_folder_exists()
        log = logging.getLogger("debug_astris_telemetry_decoder")

        if not self.logger_exists(log):
            handler = logging.FileHandler(self.create_log_filename())
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            handler.setFormatter(formatter)
            log.addHandler(handler)
            log.setLevel(logging.DEBUG)
        return log
    @staticmethod
    def logger_exists(log):
        if len(log.handlers) > 0:
            return True
        else:
            return False
    @staticmethod
    def ensure_log_folder_exists():
        if not os.path.exists(os.path.join(os.path.expanduser("~"), "ASTRIS-II-ground-station", "log")):
            os.makedirs(os.path.join(os.path.expanduser("~"), "ASTRIS-II-ground-station", "log"))

    @staticmethod
    def create_log_filename():
        return os.path.join(os.path.expanduser("~"), "ASTRIS-II-ground-station", "log", "minxss_beacon_decoder_debug.log")
