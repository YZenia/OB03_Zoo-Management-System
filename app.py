from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

def load_data():
    with open('zoo_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    animals = data['animals']
    staff = data['staff']
    return animals, staff

@app.route('/')
def home():
    animals, staff = load_data()
    return render_template('index.html', animals=animals, staff=staff)

if __name__ == '__main__':
    app.run(debug=True)
