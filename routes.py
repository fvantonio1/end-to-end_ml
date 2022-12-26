from flask import Blueprint, request, json, jsonify
from utils import load_model, make_response

urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/predict', methods=['GET'])
def predict():
    days = request.args.get('days', default = 1, type = int)
    model = load_model()
    
    response = make_response(model, days)
    return response, 200