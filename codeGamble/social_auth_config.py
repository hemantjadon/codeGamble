import os

SOCIAL_AUTH_USER_MODEL='users.AuthUser'

SOCIAL_AUTH_LOGIN_URL= '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL='/'
SOCIAL_AUTH_LOGIN_ERROR_URL='/accounts/login-error/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/register/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/accounts/register/'

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']