from waitress import serve
from main import app

if __name__ == '__main__':
    serve(app, port='8000')
