class Test():
    def __init__(self):
        self.__i = 1
    
    def _set_i(self):
        self.__i += 1
        return False
    
    def _show(self):
        print(self.__i)
    
    def result(self):
        self._show()
        self._set_i()
        self._show()
        
        
if __name__ == '__main__':
    test = Test()
    test.result()
    
    
    
        
        