import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/social_media_analysis'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    #MAIL_SERVER = 'smtp.googlemail.com'
    #MAIL_PORT = 25
    #MAIL_USE_TLS = True
    MAIL_SERVER: 'smtp.gmail.com',
    MAIL_PORT: 465,
    MAIL_USE_TLS: False,
    MAIL_USE_SSL: True,
    MAIL_USERNAME = 'smanalysis.uom@gmail.com'
    MAIL_PASSWORD = 'Smanalysis@123'