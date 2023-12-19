

CELERY_BROKER = "redis://localhost:6379/0"
CELERY_BACKEND = "CELERY_BACKEND"
BROKER_URL = "BROKER_URL"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_RESULT_EXTENDED = "CELERY_RESULT_EXTENDED"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = ['json']
CELERY_RESULT_SERIALIZER = ['json']

CELERY_BROKER_BACKEND = "memory"
timezone = "Tehran/Iran"
CELERY_CACHE_BACKEND = True
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Other configuration:
# RESULT_EXPIRE = 3600
