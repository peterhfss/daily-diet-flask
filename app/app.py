import datetime
from flask import Flask, jsonify, request
from app.main.models.meal import Meal

meals =[]

def create_app():
    app = Flask(__name__)

    @app.route('/meals',methods=['POST'])
    def create_meal():
        # Obtendo os valores passados pela requisição
        data = request.get_json()
        new_meal = Meal(name=data.get('name'), description=data.get('description'), created_at=datetime.datetime.now(), is_on_diet=False)
        meals.append(new_meal)
        return jsonify({'message':'Nova refeição criada com sucesso'})

    @app.route('/meals', methods=['GET'])
    def get_meals():
        meals_list = [meal.to_dict() for meal in meals]

        output ={
            "meals": meals_list
        }

        return jsonify(output)

    return app