"""
    def __call__(cls, *args, **kwargs):
        if not (cls is cls.__instance):
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
"""

# 1
# staticmethod
class Singleton1:
    __instance = None
    @staticmethod
    def getInstance():
        if Singleton1.__instance == None:
            Singleton1()
        return Singleton1.__instance

    def __init__(self):
        if Singleton1.__instance != None:
            raise Exception("Only one instance!")
        else:
            Singleton1.__instance = self

# 2
# classmethod
class Singleton2:
    __instance = None
    def __init__(self):
        if not Singleton2.__instance:
            print("call __init__ method")
        else:
            print("Instance already created: ", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance


# 3
class Singleton3:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        pass


"""
    class Example:
        __instance = None

        def __new__(cls, x, y):
            if Example.__instance is None:
                Example.__instance = super().__new__(cls)
                Example.__instance.x = x
                Example.__instance.y = y
        
        def __init__(self, x, y):
            self.x = self.__instance.x
            self.y = self.__instance.y
"""