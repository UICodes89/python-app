from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! <3',
        'deployed_on': 'kubernetes',
        'message1git status':'you are doing grat!! Manoj Shukla!',
        'deployed_on':'kubernates'
    })

@app.route('/api/v1/healthz')
def health():
    # Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    # Start the server only once and after all routes are defgitined
    app.run(host="0.0.0.0", port=8080)