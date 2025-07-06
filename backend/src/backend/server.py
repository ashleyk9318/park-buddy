from flask import Flask
from backend.routes import garage_bp, floor_bp, parking_spot_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(garage_bp)
app.register_blueprint(floor_bp)
app.register_blueprint(parking_spot_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)