import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from flask.sessions import NullSession
from werkzeug.exceptions import abort
import datetime

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_competition(competition_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM competitions WHERE id = ?',
                        (competition_id,)).fetchone()
    conn.close()
    if note is None:
        abort(404)
    return note

def get_score(competition_id):
    conn = get_db_connection()
    scores = conn.execute('SELECT * FROM scores WHERE competitionid = ?',
                        (competition_id,)).fetchone()
    conn.close()
    if scores is None:
        abort(404)
    return scores

def get_shots(score_id):
    conn = get_db_connection()
    shots = conn.execute('SELECT * FROM shots WHERE scoreid = ?',
                        (score_id,)).fetchone()
    conn.close()
    if shots is None:
        shots = None
    return shots

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    conn = get_db_connection()
    competitions = conn.execute('SELECT * FROM competitions INNER JOIN scores ON competitions.id = scores.competitionid').fetchall()
    conn.close()
    return render_template('index.html', competitions=competitions)

@app.route('/competitions/<int:competition_id>')
def competition_post(competition_id):
    competition = get_competition(competition_id)
    score = get_score(competition_id)
    shots = get_shots(score['id'])
    chart_labels = ['Serie 1', 'Serie 2', 'Serie 3', 'Serie 4']
    chart_values = [score['serie1'], score['serie2'], score['serie3'], score['serie4']]
    return render_template('competitions/post.html', competition=competition, score=score, shots=shots, chart_labels=chart_labels, chart_values=chart_values)

@app.route('/competitions/<int:competition_id>/chart')
def competition_chart(competition_id):
    competition = get_competition(competition_id)
    score = get_score(competition_id)
    shots = get_shots(score['id'])
    chart_labels = ['Serie 1', 'Serie 2', 'Serie 3', 'Serie 4']
    chart_values = [score['serie1'], score['serie2'], score['serie3'], score['serie4']]
    return render_template('charts/competition.html', competition=competition, score=score, shots=shots, chart_labels=chart_labels, chart_values=chart_values)


@app.route('/competitions/create', methods=('GET', 'POST'))
def competition_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        score = request.form['score']
        serie1 = request.form['serie1']
        serie2 = request.form['serie2']
        serie3 = request.form['serie3']
        serie4 = request.form['serie4']
        sporttype = request.form['sporttype']
        shoton = request.form['shoton']

        if not title:
            title = 'no title'
        if not content:
            content = 'no content'

        if not score or not serie1 or not serie2 or not serie3 or not serie4 or not shoton:
            flash('Check the from!')
        elif float(score) != (float(serie1) + float(serie2) + float(serie3) + float(serie4)):
            flash('Check the score!' + str(float(serie1) + float(serie2) + float(serie3) + float(serie4)))
        else:
            conn = get_db_connection()

            insert_competitions = conn.execute('INSERT INTO competitions (title, content, sporttype, shoton) VALUES (?, ?, ?, ?)',
                (title, content, sporttype, shoton))

            conn.execute('INSERT INTO scores (competitionid, score, serie1, serie2, serie3, serie4) VALUES (?, ?, ?, ?, ?, ?)',
                (insert_competitions.lastrowid, score, serie1, serie2, serie3, serie4))

            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('competitions/create.html')

@app.route('/competitions/<int:id>/edit', methods=('GET', 'POST'))
def competition_edit(id):
    competition = get_competition(id)
    score = get_score(id)
    shots = get_shots(score['id'])

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        score = request.form['score']
        serie1 = request.form['serie1']
        serie2 = request.form['serie2']
        serie3 = request.form['serie3']
        serie4 = request.form['serie4']
        sporttype = request.form['sporttype']
        shoton = request.form['shoton']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE competitions SET title = ?, content = ?, updated = ?, sporttype = ?, shoton = ?'
                         ' WHERE id = ?',
                         (title, content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), sporttype, shoton, id))
            conn.execute('UPDATE scores SET score = ?, serie1 = ?, serie2 = ?, serie3 = ?, serie4 = ?'
                         ' WHERE competitionid = ?',
                         (float(score), float(serie1), float(serie2), float(serie3), float(serie4), id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('competitions/edit.html', competition=competition, score=score, shots=shots)

@app.route('/competitions/<int:id>/delete', methods=('POST',))
def competition_delete(id):
    note = get_competition(id)
    conn = get_db_connection()
    
    conn.execute('DELETE FROM competitions WHERE id = ?', (id,))
    conn.execute('DELETE FROM scores WHERE competitionid = ?', (id,))

    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(note['title']))
    return redirect(url_for('index'))
