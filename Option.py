from abc import ABC, abstractmethod


class Option(ABC):

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    @abstractmethod
    def execute(self):
        ...


