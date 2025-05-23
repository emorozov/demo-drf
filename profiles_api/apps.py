from django.apps import AppConfig


class ProfilesApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles_api"

    def ready(self):
        import profiles_api.signals.handlers
