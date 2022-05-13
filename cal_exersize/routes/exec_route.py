from flask import Flask, Blueprint, Response, render_template, request, session
from cal_exersize.exercise.service import Exersize_service

exec = Exersize_service()


bp = Blueprint('exec', __name__, url_prefix='/exec')

@bp.route('/select_exec')
def select_exec():
    return render_template('select_exec.html')


# @bp.route('/run_exec/<string:exec_name>')
# def run_exec(exercise_index):
#     exec_name = exec.getExecName(exercise_name)
#     return render_template('run_exec.html', exec_name=exec_name)


@bp.route('/exec_result')
def exec_result():
    counter = exec.counter
    calories = exec.calories
    return render_template('exec_result.html', counter=counter, calories=calories)


@bp.route('/video_feed_arm_curl')
def video_feed_arm_curl():
    return Response(exec.arm_curl(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_chair_dips')
def video_feed_chair_dips():
    return Response(exec.chair_dips(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_crunch')
def video_feed_crunch():
    return Response(exec.crunch(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_leg_raise')
def video_feed_leg_raise():
    return Response(exec.leg_raise(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_lunge')
def video_feed_lunge():
    return Response(exec.lunge(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_pull_up')
def video_feed_pull_up():
    return Response(exec.pull_up(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_push_up')
def video_feed_push_up():
    return Response(exec.push_up(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_side_lateral_raise')
def video_feed_side_lateral_raise():
    return Response(exec.side_lateral_raise(), mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/video_feed_squat')
def video_feed_squat():
    return Response(exec.squat(), mimetype='multipart/x-mixed-replace; boundary=frame')

