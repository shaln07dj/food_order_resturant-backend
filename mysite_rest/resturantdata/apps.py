from django.apps import AppConfig


class ResturantdataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resturantdata'

    def ready(self):
        import resturantdata.signals
                        
