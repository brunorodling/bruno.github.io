from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Modelo de dados do personagem
character = {
    "defesa": 10,
    "agilidade": 10,
    "armadura": 10,
    "constituicao": 10,
    "inteligencia": 10,
    "sabedoria": 10,
    "destreza": 10,
    "carisma": 10,
    "espada": 10
}

@app.route('/')
def index():
    return render_template('index.html', character=character)

@app.route('/update', methods=['POST'])
def update():
    for key in character.keys():
        if key in request.form:
            character[key] = int(request.form[key])
    return redirect(url_for('index'))

@app.route('/attack', methods=['POST'])
def attack():
    damage = int(request.form['damage'])
    for key in character.keys():
        character[key] = max(character[key] - damage, 0)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
