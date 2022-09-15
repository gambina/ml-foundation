import logging


def setup_logger(log_level=logging.DEBUG):
    Logger = logging.getLogger(__name__)
    Logger.setLevel(log_level)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s'
        + '| %(name)s: %(module)s - %(funcName)s():'
        + '%(message)s'
    )
    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    Logger.addHandler(console_handler)
    file_handler = logging.FileHandler('../logger.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)
    Logger.addHandler(file_handler)
    return Logger

# Test if it works


def main():
    Logger = setup_logger()
    Logger.warning('This is a warning message!')


if __name__ == '__main__':
    main()
    print('End of the file execution')
