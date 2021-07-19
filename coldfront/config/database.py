import os
from coldfront.config.env import ENV

#------------------------------------------------------------------------------
# Database settings
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Custom Database settings
#------------------------------------------------------------------------------
# You can also override this manually in local_settings.py, for example:
#
# NOTE: For mysql you need to: pip install mysqlclient
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'coldfront',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     },
# }


# NOTE: For postgresql you need to: pip install psycopg2
if os.environ.get('DBUSER', default=False):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': os.environ['DBUSER'] + "@coldfront-postgres",
            'PASSWORD': os.environ['DBPASS'],
            'HOST': os.environ['DBHOST'] + ".postgres.database.azure.com",
            'PORT': '5432',
        },
    }
else:
    # Set this using the DB_URL env variable. Defaults to sqlite. 
    #
    # Examples:
    #
    # MariaDB:
    #  DB_URL=mysql://user:password@127.0.0.1:3306/database
    #
    # Postgresql:
    #  DB_URL=psql://user:password@127.0.0.1:8458/database
    #------------------------------------------------------------------------------
    DATABASES = {
        'default': ENV.db_url(
            var='DB_URL',
            default='sqlite:///'+os.path.join(os.getcwd(), 'coldfront.db')
        )
    }
