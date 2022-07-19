from engines.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        """
        Returns true if -> warning light is on
        """
        return self.warning_light_on
