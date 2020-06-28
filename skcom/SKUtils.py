
import os

class SKUtils:
    @staticmethod
    def CheckAndCreateFolder(path):
        if not os.path.exists(path):
            os.mkdir(path)