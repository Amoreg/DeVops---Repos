
from flask import Flask, render_template, session, redirect, url_for, request, flash
import sqlite3
import fake_events

app = Flask(__name__)
app.secret_key = "bettingsecret123"

# DATABASE = "betting.db"

# Helper: get database connection
def get_db():
    db = app.config.get("DATABASE", "betting.db")
    return sqlite3.connect(db, check_same_thread=False)

@app.route('/')
def home():
    if 'user' in session:
        return render_template("home.html", user=session['user'])
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with get_db() as conn:
            c = conn.cursor()
            c.execute('SELECT id, balance FROM user WHERE username = ? AND password = ?', (username, password))
            user = c.fetchone()
            if user:
                session['user'] = username
                session['user_id'] = user[0]
                session['balance'] = user[1]
                c.close()
                return redirect(url_for('home'))
            c.close()
            flash("Incorrect credentials", "error")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if len(username) > 50:
            flash("Username is too long.", "error")
            return render_template('register.html')

        with get_db() as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM user WHERE username = ?', (username,))
            if c.fetchone():
                c.close()
                flash("Username already exists.", "error")
                return render_template('register.html')

            c.execute('INSERT INTO user (username, email, password, balance) VALUES (?, ?, ?, ?)', (username, email, password, 1000.0))
            conn.commit()
            c.close()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/betting', methods=['GET', 'POST'])
def betting():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        event_id = request.form['event_id']
        bet_type = request.form['bet_type']
        amount = float(request.form['amount'])

        if amount > session['balance']:
            flash("Insufficient balance.", "error")
            return redirect(url_for('betting'))

        # Get odds
        events = fake_events.get_all_events()
        event = next((e for e in events if e['id'] == int(event_id)), None)
        if not event:
            flash("Event not found.", "error")
            return redirect(url_for('betting'))

        if bet_type == 'home':
            odds = event['odds_home']
        elif bet_type == 'away':
            odds = event['odds_away']
        elif bet_type == 'draw':
            odds = event['odds_draw']
        else:
            flash("Invalid bet type.", "error")
            return redirect(url_for('betting'))

        # Place bet
        with get_db() as conn:
            c = conn.cursor()
            c.execute('INSERT INTO bet (user_id, event_id, bet_type, amount, odds) VALUES (?, ?, ?, ?, ?)',
                      (session['user_id'], event_id, bet_type, amount, odds))
            c.execute('UPDATE user SET balance = balance - ? WHERE id = ?', (amount, session['user_id']))
            conn.commit()
            session['balance'] -= amount
            c.close()

        flash("Bet placed successfully!", "success")
        return redirect(url_for('betting'))

    events = fake_events.get_all_events()
    return render_template('betting.html', events=events, balance=session['balance'])

@app.route('/mybets')
def mybets():
    if 'user' not in session:
        return redirect(url_for('login'))

    with get_db() as conn:
        c = conn.cursor()
        c.execute('''
            SELECT b.id, e.sport, e.teams, e.date, b.bet_type, b.amount, b.odds, b.placed_at
            FROM bet b
            JOIN event e ON b.event_id = e.id
            WHERE b.user_id = ?
            ORDER BY b.placed_at DESC
        ''', (session['user_id'],))
        bets = c.fetchall()
        c.close()

    return render_template('mybets.html', bets=bets)

#-----------------------------------------------------------------------------

def create_tables():
    conn = get_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT,
    password TEXT,
    balance REAL DEFAULT 1000.0
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS event(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport TEXT,
    teams TEXT,
    date TEXT,
    odds_home REAL,
    odds_away REAL,
    odds_draw REAL
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS bet(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    event_id INTEGER,
    bet_type TEXT,
    amount REAL,
    odds REAL,
    placed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (event_id) REFERENCES event(id)
    )''')

    # Insert fake events
    events = fake_events.get_all_events()
    for event in events:
        c.execute('INSERT OR IGNORE INTO event (id, sport, teams, date, odds_home, odds_away, odds_draw) VALUES (?, ?, ?, ?, ?, ?, ?)',
                  (event['id'], event['sport'], event['teams'], event['date'], event['odds_home'], event['odds_away'], event['odds_draw']))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)