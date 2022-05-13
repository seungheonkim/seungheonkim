from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
from cal_exersize.exercise.service import Excersize_service

exec = Excersize_service()

cap = cv2.VideoCapture('/Users/gimseungheon/Desktop/김승헌/sessac_python/cal_excersize/videos/Chair Dips.mp4')
app = Flask(__name__)


def gen_frames():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    calories = 0
    stage = None
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, frame = cap.read()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                # Get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                # Calculate angle
                angle = exec.calculate_angle(shoulder, hip, knee)

                # Curl counter logic
                if angle > 100:
                    stage = "down"
                if angle < 60 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

                # Calorie calc logic
                calories = 1 * counter

            except:
                pass

            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0, 0), (280, 130), (51, 153, 255), -1)

            # Rep data
            cv2.putText(image, 'Reps: ' + str(counter),
                        (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 51, 51), 5, cv2.LINE_AA)

            # Calorie Burnt data
            cv2.putText(image, 'Kcal: ' + str(calories),
                        (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 51, 51), 5, cv2.LINE_AA)
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )
            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
