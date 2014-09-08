from tornado import auth, gen, web
import motor
from Match import Match

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('index.html', title='Home')

    @gen.coroutine
    def post(self, data):
        self.write('home-post, ' + data)


class LoginHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('login.html', title='Login')


class RegisterHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write("Request to register\n")


class MatchHandler(web.RequestHandler):
    @web.authenticated
    @gen.coroutine
    def get(self):
        db = self.settings['db']
        all_matches = db.matches.find()
        matches_count = yield all_matches.count()
        yielded_matches = yield all_matches.to_list(100)
        # yielded_matches.append(Match([]))
        self.render('matches.html', matches=yielded_matches)
