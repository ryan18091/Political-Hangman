from app import db

class Sessions(db.Model):
    # __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer,unique=False, nullable=True)
    politician = db.Column(db.String,unique=False, nullable=True)
    # politician_id = db.Column(db.Integer,unique=False, nullable=True)
    datestamp = db.Column(db.String,unique=False, nullable=True)
    guess_phrase = db.Column(db.String,unique=False, nullable=True)
    phrase = db.Column(db.String,unique=False, nullable=True)
    word_guess = db.Column(db.String,unique=False, nullable=True)
    turns = db.Column(db.Integer,unique=False, nullable=True)
    alpl = db.Column(db.String,unique=False, nullable=True)


    def __init__(self, session_id, politician, datestamp, guess_phrase, phrase, word_guess, turns, alpl):
        self.session_id = session_id
        self.politician = politician
        # self.politician_id = politician_id
        self.datestamp = datestamp
        self.guess_phrase = guess_phrase
        self.phrase = phrase
        self.word_guess = word_guess
        self.turns = turns
        self.alpl = alpl

    def __repr__(self):
        return '<session_id {}'.format(self.session_id)

class tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    politician = db.Column(db.String,unique=True, nullable=True)
    screen_name = db.Column(db.String,unique=True, nullable=True)
    datestamp = db.Column(db.String,unique=False, nullable=True)
    tweet = db.Column(db.String,unique=False, nullable=True)
    # background_url = db.Column(db.String,unique=False, nullable=True)
    # profile_url = db.Column(db.String,unique=False, nullable=True)

    def __init__(self, politician,  datestamp, tweet, screen_name):
        self.politician = politician
        self.screen_name = screen_name
        self.datestamp = datestamp
        self.tweet = tweet
        # self.background_url = background_url
        # self.profile_url = profile_url

    def __repr__(self):
        return '<User %r>' % self.username

