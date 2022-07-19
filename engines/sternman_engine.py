from engines import Engine


class SternmanEngine(engine):
    def __init__(self, warning_light_on):
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
