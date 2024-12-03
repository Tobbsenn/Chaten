from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

# Initialiserer Flask og SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Rute for å servere chatrommet
@app.route('/')
def index():
    return render_template('index.html')

# Lytter etter meldinger fra klienter
@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    # Sender meldingen til alle tilkoblede klienter
    socketio.send(message, broadcast=True)

# Starter Flask-serveren
if __name__ == '__main__':
    print("Server is running. Access it locally on http://127.0.0.1:5000 or with ngrok.")
    socketio.run(app, host='0.0.0.0', port=5000)
