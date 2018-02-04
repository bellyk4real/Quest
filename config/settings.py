from datetime import timedelta

DEBUG = True

# SERVER_NAME = 'localhost:5000'
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'bellyk4real@gmail.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'bellyk4real@gmail.com'
MAIL_PASSWORD = 'londoneye1'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy.
# db_uri = 'postgresql://quest:devpassword@postgres:5432/quest'
db_uri = 'postgres://whoeuuohhmtirt:64b4737e6536f80f29d1d26273419cacf7a2a2869a70d8c4e43914330efbf92b@ec2-50-16-231-2.compute-1.amazonaws.com:5432/din812vclohoc'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
