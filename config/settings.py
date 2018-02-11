from datetime import timedelta

DEBUG = True
LOG_LEVEL = 'DEBUG'

PAY_STACK_TEST_SECRET  = 'sk_test_f9153e963f26d104495a082c0b1b53f207dffefe'
PAY_STACK_TEST_PUBLIC  = 'pk_test_8a48853663ac6b2c68f1e5cf9c346229c278d32d'

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
db_uri = 'postgresql://quest:devpassword@postgres:5432/quest'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
