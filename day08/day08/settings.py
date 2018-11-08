"""
Django settings for day08 project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x#_k8ffm)vt)ooh8*_or*27g+m2qydv65chw^8)_n&p*74h(te'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app08',
    'lianxi'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'day08.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'day08.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django08',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PWD'),
        'PORT': '3306',
        'HOST': '101.132.145.148',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# redis作为缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.163.com'  # 如果是 163 改成 smtp.163.com

EMAIL_PORT = 465  # smtp的端口 不能改

EMAIL_HOST_USER = "17625904460@163.com"  # 账号

EMAIL_HOST_PASSWORD = "zd010803"  # 授权码

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 默认邮件的发送人

VERIFY_CODE_MAX_AGE = 60 * 60  # H缓存时间，验证码

#设置谁发送给谁
ADMINS = (
    ('zhangding', '17625904460@163.com'),
    ('zd','1574070307@qq.com')
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER
LOGGING = {
    #版本
    'version': 1,
    #是否覆盖之前的日志
    'disable_existing_loggers': False,
    # 用于控制日志信息的最终输出格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'easy':{
          'format':'%(asctime)s|%(funcName)s|%(message)s'
        }
    },
    #过滤条件要求debug是true/false
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true':{
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },


    'handlers': {
        # 'null': {
        #     'level': 'DEBUG',
        #     'class': 'logging.NullHandler',
        # },
        #一旦线上代码报错，邮件提示
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log", 'debug.log'),  # 文件路径
            'maxBytes': 1024 * 1024 * 5, #5M的数据
            'backupCount': 5,  #允许几个备份
            'formatter': 'standard', #上面用的格式
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    #上面四个全是为loggers服务的
    'loggers': {
        'django': {
            'handlers': ['console','debug'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True, #是否继承父类的log信息
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['debug'],
            'propagate': False,
        },
    }
}