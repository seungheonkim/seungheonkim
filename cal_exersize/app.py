from flask import Flask, render_template, Response, blueprints
import cv2
import mediapipe as mp
from cal_exersize.exercise.service import Exersize_service
from routes.exec_route import bp as exec_bp


app = Flask(__name__)
app.register_blueprint(exec_bp)

@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
