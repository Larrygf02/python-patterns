import abc

class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor = successor
    
    @abc.abstractmethod
    def handle_request(self):
        print('handle_request')

class ConcreteHandler1(Handler):
    def handle_request(self):
        if True:
            pass
        elif self._successor is not None:
            self._successor.handle_request()

class ConcreteHandler2(Handler):
    def handle_request(self):
        if False:
            pass
        elif self._successor is not None:
            print(self._successor)
            self._successor.handle_request()

def main():
    concrete_handler_1 = ConcreteHandler1()
    concrete_handler_2 = ConcreteHandler2(concrete_handler_1)
    concrete_handler_2.handle_request()

if __name__ == "__main__":
    main()