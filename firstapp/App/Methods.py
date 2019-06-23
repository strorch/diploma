from .AbstractMethod import AbstractMethod


class Methods(AbstractMethod):

    @staticmethod
    def getMethod(name):
        array = Methods.getMathodsArray()
        try:
            method = array[name]
        except:
            method = None
        return method

    @staticmethod
    def getMathodsArray():
        return {
            'shi-tomasi': Methods.ShiTomasi,
            'harris': Methods.Harris,
        }


