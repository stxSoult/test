# Toggle  'production/development'
ENVIRONMENT = 'development'


if ENVIRONMENT == 'development':
    SETTINGS = 'conf.settings.development'
else:
    SETTINGS = 'conf.settings.production'

