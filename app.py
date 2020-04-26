import os
import flask

app = flask.Flask(__name__)


@app.route('/status')
def status():
    return flask.jsonify({'HOSTNAME': os.getenv('HOSTNAME')})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
