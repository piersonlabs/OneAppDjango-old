import dj_database_url
import os
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

##################### DJANGO #####################
GRAPPELLI_ADMIN_TITLE = "One App Content Administration"
#GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
DEBUG = True
LOCAL = False
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = '&amp;vfd6x75sqm$!dm$df)x3%m*f#lm^rjo(rz$sdfads3)62=&amp;$-'
ADMINS = (('Dane Hesseldahl', 'dane.hesseldahl@gmal.com'),)
MANAGERS = ADMINS
ROOT_URLCONF = 'oneapp.urls'
WSGI_APPLICATION = 'oneapp.wsgi.application'
TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'))

##################### DATABASE #####################
if LOCAL:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': 'oneapp',
			'USER': 'root',
			'PASSWORD': '',
			'HOST': '',
			'PORT': '',
		}
	}
else:
	DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

##################### APP SETTINGS #####################

ANONYMOUS_USER_ID = 1
AWS_ACCESS_KEY_ID = 'AKIAIHOPPUYH7VQHG3BA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'one-app'
AWS_BUCKET_NAME = 'one-app'

FACEBOOK_APPLICATION_ID = 115387878589734
FACEBOOK_APPLICATION_SECRET_KEY = '9ec37b21b6d33495c28a6ca448fec021'
FACEBOOK_APPLICATION_NAMESPACE = 'oneapp'

SENDGRID_USERNAME = 'app2921662@heroku.com'
SENDGRID_PASSWORD = '09qlymjz'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'app2921662@heroku.com'
EMAIL_HOST_PASSWORD = '09qlymjz'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ACCOUNT_ACTIVATION_DAYS = 7

LOGIN_URL		   = '/account/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGIN_ERROR_URL	   = '/account/login/'

TWITTER_CONSUMER_KEY		 = ''
TWITTER_CONSUMER_SECRET		 = ''
FACEBOOK_APP_ID				 = ''
FACEBOOK_API_SECRET			 = ''
LINKEDIN_CONSUMER_KEY		 = ''
LINKEDIN_CONSUMER_SECRET	 = ''
ORKUT_CONSUMER_KEY			 = ''
ORKUT_CONSUMER_SECRET		 = ''
GOOGLE_CONSUMER_KEY			 = ''
GOOGLE_CONSUMER_SECRET		 = ''
GOOGLE_OAUTH2_CLIENT_ID		 = ''
GOOGLE_OAUTH2_CLIENT_SECRET	 = ''
FOURSQUARE_CONSUMER_KEY		 = ''
FOURSQUARE_CONSUMER_SECRET	 = ''
GITHUB_APP_ID				 = ''
GITHUB_API_SECRET			 = ''
DROPBOX_APP_ID				 = ''
DROPBOX_API_SECRET			 = ''
FLICKR_APP_ID				 = ''
FLICKR_API_SECRET			 = ''
INSTAGRAM_CLIENT_ID			 = ''
INSTAGRAM_CLIENT_SECRET		 = ''

SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

##################### LOCALIZATION #####################

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

##################### MEDIA SETTING #####################
if LOCAL:
	MEDIA_ROOT = ''
	MEDIA_URL = ''
	STATIC_ROOT = ''
	STATIC_URL = '/assets/'
	UPLOADS_URL = '/assets/'
	ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
	
	STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'assets'),)

else:
	MEDIA_ROOT = ''
	MEDIA_URL = ''
	STATIC_ROOT = ''
	STATIC_URL = 'http://one-app.s3-website-us-west-2.amazonaws.com/'
	UPLOADS_URL = 'http://one-app.s3-website-us-west-2.amazonaws.com/'
	ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

	STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'assets'),)
	TINYMCE_JS_URL = STATIC_URL + "tiny_mce/tiny_mce.js"
	TINYMCE_JS_ROOT = os.path.join(SITE_ROOT, "assets/tiny_mce")

TINYMCE_DEFAULT_CONFIG = {
	'plugins': "table,spellchecker,paste,searchreplace",
	'theme': "advanced",
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

##################### LOADER & MIDDLE SETTING #####################
STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#	 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

if not LOCAL:
	STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
	DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	  'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS = (
#	'social_auth.backends.facebook.FacebookBackend',
#	'userena.UserenaAuthenticationBackend',
#	'guardian.backends.ObjectPermissionBackend',
	'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
#	'social_auth.context_processors.social_auth_by_name_backends',
#	'social_auth.context_processors.social_auth_backends',
#	'social_auth.context_processors.social_auth_by_type_backends',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.static',
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.i18n',
	#'nerd8_site.context_processors.location',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'fandjango.middleware.FacebookMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
#	'grappelli.dashboard',
	'grappelli',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'storages',
	'imagekit',
	'fandjango',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}
