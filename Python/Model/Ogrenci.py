
class Ogrenci:
    def __init__(self,
                 id : int = None,
                 name : str = None,
                 surname : str = None,
                 age : int = None,
                 tc_kimlik_no : int = None
                 ) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__age=age
        self.__tc_kimlik_no = tc_kimlik_no
    
    def __str__(self) -> str:
        return f"(id={self.__id},name={self.__name},surname={self.__surname},age={self.__age},tc_kimlik_no={self.__tc_kimlik_no})"
    
    def getID(self) -> int:
        return self.__id
    def getName(self) -> str:
        return self.__name
    def getSurname(self) -> str:
        return self.__surname
    def getAge(self) -> int:
        return self.__age
    def getTcKimlikNo(self) -> int:
        return self.__tc_kimlik_no
    
    
    def setID(self,id : int) -> None:
        self.__id = id
    def setName(self,name : str) -> None:
        self.__name = name
    def setSurname(self,surname : str) -> None:
        self.__surname = surname
    def setAge(self,age : int) -> None:
        self.__age = age
    def setTcKimlikNo(self,tc_kimlik_no : int) -> None:
        self.__tc_kimlik_no = tc_kimlik_no

    def __iter__(self):
        for key in self.__dict__:
            keyClear = key.replace("_Ogrenci__","")
            yield keyClear, getattr(self, key)