from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for initial tracks and recommended tracks
initial_tracks = [
    {"track_id": 3, "title": "Track 3", "link": "link_to_track_3.mp3"},
    {"track_id": 134, "title": "Track 134", "link": "link_to_track_134.mp3"},
    {"track_id": 138, "title": "Track 138", "link": "link_to_track_138.mp3"},
    {"track_id": 139, "title": "Track 139", "link": "link_to_track_139.mp3"},
    {"track_id": 141, "title": "Track 141", "link": "link_to_track_141.mp3"}
]

# Function to get recommended tracks for a given track ID
def get_recommended_tracks(track_id):
    # Assuming the recommended tracks are static for demonstration
    # In real-world scenarios, you would query a database or use some recommendation algorithm
    return [3, 134, 138, 139, 141]

@app.route('/')
def home():
    return render_template('home.html', initial_tracks=initial_tracks)

@app.route('/play', methods=['POST'])
def play():
    track_id = int(request.form['track_id'])
    selected_track = None
    for track in initial_tracks:
        if track['track_id'] == track_id:
            selected_track = track
            break
    if selected_track:
        recommended_tracks = get_recommended_tracks(track_id)
        return render_template('player.html', selected_track=selected_track, recommended_tracks=recommended_tracks)
    else:
        return "Track not found."

if __name__ == '__main__':
    app.run(debug=True)
