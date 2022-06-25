from abc import ABC, abstractmethod


class servicable(ABC):
    @abstractmethod
    def needs_service(self) -> bool: raise NotImplementedError
