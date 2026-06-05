from dotenv import load_dotenv
import os


load_dotenv()


class ConfigReader:

    @staticmethod
    def get_base_url():
        return os.getenv("BASE_URL")