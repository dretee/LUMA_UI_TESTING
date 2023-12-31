import configparser

configs = configparser.RawConfigParser()
configs.read(".\\configurations\\config.ini")


class ReadProperties:

    @staticmethod
    def getPageURL():
        url = configs.get("common data", "HomeURL")
        return url

    @staticmethod
    def getAccountCreationURL():
        return configs.get("common data", "createAccount")

    @staticmethod
    def getCartURL():
        return configs.get("common data", "cartURL")

    @staticmethod
    def getAccountURL():
        return configs.get("common data", "accountURL")

    @staticmethod
    def getEmail():
        return configs.get("common data", "EXISTING_EMAIL")

    @staticmethod
    def getPassword():
        return configs.get("common data", "EXISTING_PASSWORD")

    @staticmethod
    def LoginURL():
        return configs.get("common data", "LogInURL")

    @staticmethod
    def forgotPasswordURL():
        return configs.get("common data", "forgotPasswordURL")

    @staticmethod
    def getMenHoodiesAndSweatshirtPageURL():
        return configs.get("men page data", "URLForHoodiesAndSweatshirtPage")

    @staticmethod
    def getMenJacketPageURL():
        return configs.get("men page data", "URLForJacketsPage")

    @staticmethod
    def getMenPantsPageURL():
        return configs.get("men page data", "URLForPantsPage")

    @staticmethod
    def getMenShortsPageURL():
        return configs.get("men page data", "URLForShortsPage")

    @staticmethod
    def getMenTanksPageURL():
        return configs.get("men page data", "URLForTanksPage")

    @staticmethod
    def getWomenJacketsPageURL():
        return configs.get("Women page data", "URLForJacketsPage")

    @staticmethod
    def getWomenPantsPageURL():
        return configs.get("Women page data", "URLForPantsPage")

    @staticmethod
    def getWomenShortsPageURL():
        return configs.get("Women page data", "URLForShortsPage")

    @staticmethod
    def getWomenTanksPageURL():
        return configs.get("Women page data", "URLForTanksPage")


