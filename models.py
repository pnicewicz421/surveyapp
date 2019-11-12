from app import db

class User(db.Model):
	# user 
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), index=True, unique=False)
	isAnonymous = db.Column(db.Boolean())
	responses = db.relationship('Responses', backref='user', lazy='dynamic')

	def __repr__(self):
		if self.isAnonymous == True:
			return 'Anonymous User'
		return '<User {}>'.format(self.username)

class Question(db.Model):
	# question and question type
	id = db.Column(db.Integer, primary_key=True)
	question_prompt = db.Column(db.String(256), index=True, unique=False)
	question_type = db.Column(db.String(128), index=True, unique=False)
	answers = db.relationship("Answers", backref='answers', lazy='dynamic')

	def __repr__(self):
		return self.question + ' (' + self.question_type + ')'

class Answers(db.Model):
	# answers pre-populated for the question
	id = db.Column(db.Integer, primary_key=True)
	answer_type = db.Column(db.String(32), unique=False) # most of the time, text. But it could be picture
	answer = db.Column(db.String(128), unique=False)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	responses = db.relationship("Responses", backref='responses', lazy='dynamic')

	def __repr__(self):
		return self.answer

class Responses(db.Model):
	# individual user responses
	id = db.Column(db.Integer, primary_key=True)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
	answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return self.answer_id + ' by ' + self.user_id

