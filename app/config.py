# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    SEGMENT_ANALYTICS_WRITEKEY = os.getenv('SEGMENT_ANALYTICS_WRITEKEY', None)

    # App Config - the minimal footprint
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')

    STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY'     , None )
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None )
    SERVER_ADDRESS         = os.getenv('SERVER_ADDRESS', 'https://questshout-on-render.onrender.com/')

    STRIPE_IS_ACTIVE       = False
    if STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY:
        STRIPE_IS_ACTIVE = True
