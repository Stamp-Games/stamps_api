class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/stamp_games"
    DEBUG = True
    
class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/stamp_games-test"
    DEBUG = True
    
class TravisConfig(object):
    DATABASE_URI = "postgresql://localhost:5432/stamp_games-test"
    DEBUG = False
    SECRET_KEY = "Not secret"