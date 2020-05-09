"""Run nautilus."""
from nautilus import app, utils

if __name__ == "__main__":
    app.run(debug=utils.env.get('debug'), host="0.0.0.0")
