import abc

class CSVParserInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse(self) -> list:
        pass