import logging
from logging.handlers import RotatingFileHandler

def get_logger(logger_name, filepath):
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    rotating_file_handler = RotatingFileHandler(
        filepath,
        backupCount=10,
        maxBytes=1e7,  # 10MB
    )
    rotating_file_handler.setFormatter(formatter)
    logger.addHandler(rotating_file_handler)
    logger.setLevel(logging.INFO)

    return logger
