import os
import sqlite3 as sql
from flask import Flask, render_template, request, g, url_for, redirect
from gerrymander_app.db import get_db
from wtforms import form


import pdb

app = Flask(__name__)

def district_info():
	db = get_db()
	"""query to get random district id"""
	random_district_id = db.execute("SELECT district_id FROM gerrymander_images ORDER BY RANDOM() LIMIT 1").fetchone()[0] 

	"""queries to get relevant score/image based on id"""
	gerrymander_score_query = f"SELECT state, district_number, gerrymander_score FROM gerrymander_score WHERE district_id = '{random_district_id}'"
	gerrymander_image = f"SELECT district_image FROM gerrymander_images WHERE district_id = '{random_district_id}'"

	district_image = db.execute(gerrymander_image).fetchone()[0] 
	state, district_number, gerrymander_score = tuple(db.execute(gerrymander_score_query).fetchone())

	district_info = {'random_district_id': random_district_id, 'district_image': district_image, 'state': state, 'district_number': district_number, 'gerrymander_score': gerrymander_score}
	return district_info



@app.route('/question', methods=['GET', 'POST'])
def user_input(district_info):
	#if district_info['gerrymander_score'] > 50:
		#gerrymandered = "yes"
	#else:
		#gerrymandered = "no"
	print(district_info['state'])


	if request.form:
		user_answer=list(request.form.keys())[0]
		print(user_answer)
		return redirect(url_for('results', gerrymandered = gerrymandered, user_answer=user_answer))
	else:
		return render_template("question.html", district_image = district_info['district_image'], state = district_info['state'], district_number = district_info['district_number'], form=form)



@app.route('/answer', methods=['GET', 'POST'])
def results():
	
	data = request.args
	user_answer = data['user_answer']
	gerrymandered = data['gerrymandered']                   
	print(user_answer)
	print(gerrymandered)

	if user_answer == gerrymandered:
		results_title = "It's a match!"
		return render_template("answer.html", results_title=results_title, form=form)

	elif user_answer != gerrymandered:
		results_title = "Not a match!"
		return render_template("answer.html", results_title=results_title, form=form)
	
