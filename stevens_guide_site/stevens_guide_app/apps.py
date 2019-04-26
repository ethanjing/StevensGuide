from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StevensGuideAppConfig(AppConfig):
    name = 'stevens_guide_app'


class UserProfilesConfig(AppConfig):
    name = 'cmdbox.userprofiles'
    verbose_name = _('userprofiles')

    def ready(self):
        import cmdbox.userprofiles.signals
