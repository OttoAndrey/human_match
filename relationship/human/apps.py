from django.apps import AppConfig


class HumanConfig(AppConfig):
    name = 'human'

    def ready(self):
        import human.signals
