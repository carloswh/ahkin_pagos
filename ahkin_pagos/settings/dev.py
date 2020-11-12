from __future__ import absolute_import
from .base import BaseSettings

from datetime import timedelta


class DevSettings(BaseSettings):

    @property
    def MIDDLEWARE(self):
        middlewares = list(BaseSettings.MIDDLEWARE)
        middlewares.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
        return middlewares


DevSettings.load_settings(__name__)
