from flask import Flask, render_template, request

app = Flask(__name__)

# This dictionary simulates the recommendations data
recommendations_data = {
    "3": ["3", "134", "138", "139", "141"],
    "134": ["3", "134", "138", "139", "141"],
    "138": ["3", "134", "138", "139", "141"],
    "139": ["3", "134", "138", "139", "141"],
    "141": ["3", "134", "138", "139", "141"]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    track_id = request.form['track_id']
    recommended_tracks = recommendations_data.get(track_id, [])
    return render_template('home.html', selected_track_id=track_id, recommended_tracks=recommended_tracks)

if __name__ == '__main__':
    app.run(debug=True)
