class myString:
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
    
    
x = myString()
x.getString()
x.printString()