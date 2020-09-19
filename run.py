from app import app

@app.route('/')
def index():
    return 'Flask API started'


if __name__ == '__main__':
    app.run(port=5000, debug=True)