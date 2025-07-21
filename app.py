from flask import Flask, render_template, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load Netflix data
try:
    df = pd.read_csv('netflix_titles.csv')
except FileNotFoundError:
    df = pd.DataFrame()  # Empty dataframe if file not found

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/genre-distribution')
def genre_distribution():
    try:
        # Process genre data from CSV
        # This is sample logic - adjust based on your CSV structure
        genres = df['listed_in'].str.split(', ').explode()
        genre_counts = genres.value_counts().head(10)
        
        return jsonify({
            'genres': genre_counts.index.tolist(),
            'counts': genre_counts.values.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/year-distribution')
def year_distribution():
    try:
        # Process year data from CSV
        year_counts = df['release_year'].value_counts().sort_index()
        
        return jsonify({
            'years': year_counts.index.tolist(),
            'counts': year_counts.values.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)