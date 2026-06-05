import logging
from pathlib import Path


class Logger:

    LOG_FOLDER = Path(__file__).parent.parent / "logs"

    @staticmethod
    def get_logger():

        Logger.LOG_FOLDER.mkdir(exist_ok=True)

        log_file = Logger.LOG_FOLDER / "test.log"

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            force=True
        )

        return logging.getLogger()