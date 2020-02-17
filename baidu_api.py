
# 接口类
class Api:

    def __init__(self):
        self.__API_ID = '18393159'
        self.__API_KEY = 'sRqMyGTDARvho8g4661klEbd'
        self.__API_SECRET_KEY = 'nXb0pyumWK22EFzGFwpi3WQCvWllYneo'

    def getID(self):
        return self.__API_ID

    def getKEY(self):
        return self.__API_KEY

    def getSecretKEY(self):
        return self.__API_SECRET_KEY