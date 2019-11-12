from flask import render_template, flash, redirect, request, jsonify
from app import app, db
from app.forms import EnterRoom
from app.models import User, Question, Answers, Responses


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
	form = EnterRoom()
	return render_template('index.html', title='Enter Room Code', form=form)

@app.route('/playtime', methods=['POST', 'GET'])
def playtime():
	# development version of playing
	question = Question.query.get(1)
	questions = [{'question': question.question_prompt}]

	answers_prompts = []
	answer_ids = []

	for answer in question.answers:
		answers_prompts.append(str(answer))
		answer_ids.append(int(answer.id))

	answers = zip(answers_prompts, answer_ids)

	return render_template('playgame.html', title='Home', questions=questions, answers=answers)



@app.route('/enterroom', methods=['POST', 'GET'])
def submit():
#	if form.validate_on_submit():
#		if 'd' in form.
#				return '''
	form = EnterRoom()
	if form.validate_on_submit():
		#flash('Entering Room {}').format(form.roomcode.data)
		return redirect('/playtime')
	return redirect('/index')

@app.route('/processresponse', methods=['POST', 'GET'])
def process():
	#answer = 'STARTING OVER'
	answer = request.form['answer']
	answer_id = request.form['answer_id']
	# populate response instance
	resp = Responses()

	resp.question_id = 1
	resp.answer_id = int(request.form['answer_id'])
	resp.user_id = 1

	db.session.add(resp) 
	db.session.commit()

	return jsonify({'text': answer})

	#('', 204)

	#'Processed ' + str(answer) + str(answer_id)