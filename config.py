"""MyPHP Configuration File

Generated by Web Installer.
"""

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # Application secret key. Keep this secret!
    SECRET_KEY = "GLH3dDfxN2pFu_7dlZzZ_A"

    # Database Configuration
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://myphp_py:%5DW6gxWZzZ.bVkCST@localhost:3306/myphp_py"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Leave as is.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Captcha Site Key
    XCAPTCHA_SITE_KEY = os.environ.get("SITE_KEY") or \
                        "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"

    # Captcha Secret Key
    XCAPTCHA_SECRET_KEY = os.environ.get("SECRET_KEY") or \
                          "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

    
    # This enables HCaptcha. Uncomment these 3 lines to use
    # HCaptcha.
    if os.environ.get("HCAPTCHA", "false").lower() == 'true':
        XCAPTCHA_VERIFY_URL="https://hcaptcha.com/siteverify"
        XCAPTCHA_API_URL="https://hcaptcha.com/1/api.js"
        XCAPTCHA_DIV_CLASS="h-captcha"
    
    SESSION_COOKIE_NAME = "myphp_session"
    REMEMBER_COOKIE_NAME = "myphp_remember_token"
    
    API_LINKS_SCHEME = os.environ.get('API_LINKS_SCHEME') or 'http'

    # SESSION_TYPE = "filesystem"
    # SESSION_FILE_DIR = "C:\\Users\\advai\\OneDrive\\Documents\\Programmed tools\\myphp\\.session-data\\"

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    
    TELEGRAM_BOTAPI_USE = os.environ.get("TELEGRAM_BOTAPI_USE") is not None
    TELEGRAM_BOTAPI_KEY = os.environ.get('TELEGRAM_BOTAPI_KEY')
    TELEGRAM_BOTAPI_CHANNEL = os.environ.get("TELEGRAM_BOTAPI_CHANNEL")
    
    FERNET_KEY = os.environ.get("FERNET_KEY")
    
    SECRET_QUESTIONS = "secret_questions.json"

    # Leave as is.
    MYPHP_SETUP = True if str(os.environ.get('MYPHP_SETUP')).lower() == \
        'true' else False
