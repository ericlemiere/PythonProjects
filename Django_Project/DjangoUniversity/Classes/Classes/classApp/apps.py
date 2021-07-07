from django.apps import AppConfig


class ClassappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Classes.classApp'
    # Had to add Classes. to path
