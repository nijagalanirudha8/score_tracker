from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
batsmen = []

@app.route('/')
def index():
    return render_template('index.html', batsmen=batsmen)

@app.route('/add', methods=['POST'])
def add_batsman():
    name = request.form['name']
    runs = int(request.form['runs'])
    balls = int(request.form['balls'])
    strike_rate = (runs / balls) * 100 if balls != 0 else 0
    batsmen.append({'name': name, 'runs': runs, 'balls': balls, 'strike_rate': round(strike_rate, 2)})
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove_batsman(index):
    if 0 <= index < len(batsmen):
        batsmen.pop(index)
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    batsmen.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)