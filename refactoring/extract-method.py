class PrintVersion:
    def __init__(self, name):
        self.name = name
    
    def printBanner(self):
        print('Imprimiendo banner')

    def getOutstanding(self):
        return 'Get Outstanding'

    def printOwing(self):
        self.printBanner()

        # print details
        print("name:", self.name)
        print("amount:", self.getOutstanding())
        return True


    def printOwingN(self):
        self.printBanner()
        self.printDetails(self.getOutstanding())
        return True

    def printDetails(self, outstanding):
        print("name:", self.name)
        print("amount:", outstanding)

newprint = PrintVersion('raul')
print(newprint.printOwingN())