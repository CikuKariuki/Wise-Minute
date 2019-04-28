from app import create_app,db
from app.models import User,Occupation
from flask_script import Manager,Server
# from app import app

#Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

def test():
    '''
    run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Occupation = Occupation)

if __name__ == '__main__':
    manager.run()