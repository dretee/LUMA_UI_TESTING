import configparser

configs = configparser.RawConfigParser()
configs.read(".\\configurations\\config.ini")


class ReadProperties:

    @staticmethod
    def getPageURL():
        return configs.get("common data", "HomeURL")

    @staticmethod
    def getEmail():
        return configs.get("common data", "EXISTING_EMAIL")

    @staticmethod
    def getPassword():
        return configs.get("common data", "EXISTING_PASSWORD")

    @staticmethod
    def LoginURL():
        return configs.get("common data", "LogInURL")
