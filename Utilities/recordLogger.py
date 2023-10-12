import logging


class recordLogger:
    ## This method is a static method and will help in the configuration
    # of the logger

    @staticmethod
    def log_generator_info():
        logging.basicConfig(filename="C:\\Users\\BAB AL SAFA\\PycharmProjects\\Lumaproject\\Logs\\Records.log",
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

        # create an object
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

