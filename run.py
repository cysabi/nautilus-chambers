"""Run nautilus."""
from nautilus import app, env

if __name__ == "__main__":
    app.run(debug=env.get('debug'))
