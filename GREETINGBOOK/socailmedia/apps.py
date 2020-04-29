from django.apps import AppConfig


class SocailmediaConfig(AppConfig):
    name = 'socailmedia'

    def ready(self):
        import socailmedia.mysignal
