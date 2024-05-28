from abc import abstractmethod

class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # it's ok to have this method
        pass

    # it doesn't make sense to have this method in an old fashioned printer, either to be able to raise error
    # because users can also have chance to invoke it by API. However, it must be implemented at the
    # same time because it's an abstract method from base class, so this subclass interface segregation principle
    def fax(self, document):
        pass

    # it doesn't make sense to have this method in an old fashioned printer, either to be able to raise error
    # because users can also have chance to invoke it by API. However, it must be implemented at the
    # same time because it's an abstract method from base class, so this subclass interface segregation principle
    def scan(self, document):
        '''Not Supported'''
        raise NotImplementedError('Printer cannot scan!')
    
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)