from flask import Blueprint, jsonify

def create_user_controller():
    user_controller = Blueprint('user_module', __name__, template_folder='templates')
    
    @user_controller.route('/')
    def info():
        return jsonify({
            'module': 'user'
        })

    return user_controller
