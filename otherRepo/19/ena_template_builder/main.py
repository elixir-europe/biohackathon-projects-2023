
"""Flask API entrypoint."""

from app.app import app

app.config['SECRET_KEY'] = 'mysecretkey'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
