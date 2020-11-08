import logging

class logger:
    def get_logger():
        _logger = logging.getLogger(__name__)
        _logger.setLevel(logging.DEBUG)
        logger = logging.getLogger('root')
        FORMAT = "[%(filename)s:%(lineno)s - %(asctime)s - %(funcName)5s() - %(levelname)s] %(message)s"
        logging.basicConfig(format=FORMAT)
        return _logger


