# import bson
import os
import motor
from tornado import web, gen, ioloop
from tornado.options import define, options
from handlers import *

define('port', default=8888, help='run on the given port', type=int) 
define('db_uri', default='localhost', help='mongodb uri') 
define('db_name', default='poker', help='name of database') 
define('debug', default=True, help='debug mode', type=bool)
define('cookie_secret', default='THIS_IS_FOR_DEBUG_ONLY', help='random cookie secret value')

options.parse_command_line()

db = motor.MotorClient(options.db_uri)[options.db_name] 
gridfs = motor.MotorGridFS(db)

settings = {
    'debug': options.debug,
    'db': db,
    'login_url': '/login',
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': options.cookie_secret,
    'xsrf_cookies': True,
}

app = web.Application([
    web.url(r'/', MainHandler),
    web.url(r'/login', LoginHandler),
    web.url(r'/register', RegisterHandler),
    web.url(r'/matches', MatchHandler),
], **settings)

if __name__ == '__main__':
    app.listen(options.port)
    ioloop.IOLoop.instance().start()
