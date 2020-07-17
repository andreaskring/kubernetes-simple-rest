import flask
from flask_oidc import OpenIDConnect

app = flask.Flask(__name__)
app.config.update({
    'SECRET_KEY': 'thisisasecretkey',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_CALLBACK_ROUTE': '/callback',
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'flask-demo',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token'
})
oidc = OpenIDConnect(app)


@app.route('/')
def index():
    if oidc.user_loggedin:
        return 'Welcome %s'# % oidc.user_getfield('email')
    else:
        return 'Not logged in'


@app.route('/login')
@oidc.require_login
def login():
    return 'Welcome %s'# % oidc.user_getfield('email')


@app.route('/callback')
@oidc.accept_token
def callback():
    return 'Callback'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
