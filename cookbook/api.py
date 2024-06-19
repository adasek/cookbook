from flask import Blueprint, Flask, request, jsonify, abort

app = Flask(__name__)

api_blueprint = Blueprint('api', __name__)

# In-memory storage for recipes
recipes = [
    {
        "id": 1,
        "author": "Jane Doe",
        "ingredients": [
            {
                "name": "All-purpose flour",
                "quantity": "2 cups"
            },
            {
                "name": "Granulated sugar",
                "quantity": "1 and 1/2 cups"
            },
            {
                "name": "Baking powder",
                "quantity": "1 and 1/2 teaspoons"
            },
            {
                "name": "Salt",
                "quantity": "1/2 teaspoon"
            },
            {
                "name": "Unsalted butter",
                "quantity": "1/2 cup"
            },
            {
                "name": "Eggs",
                "quantity": "2"
            },
            {
                "name": "Vanilla extract",
                "quantity": "2 teaspoons"
            },
            {
                "name": "Whole milk",
                "quantity": "1 cup"
            }
        ],
        "instructions": [
            "Preheat your oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.",
            "In a medium bowl, whisk together the flour, baking powder, and salt. Set aside.",
            "In a large bowl, beat the butter and sugar together until light and fluffy. Add the eggs one at a time, beating well after each addition. Stir in the vanilla extract.",
            "Add the flour mixture to the butter mixture alternately with the milk, beginning and ending with the flour mixture. Beat until just combined.",
            "Divide the batter evenly between the prepared cake pans and smooth the tops.",
            "Bake in the preheated oven for 25 to 30 minutes, or until a toothpick inserted into the center of the cakes comes out clean.",
            "Allow the cakes to cool in the pans for 10 minutes, then turn them out onto a wire rack to cool completely.",
            "Frost and decorate as desired."
        ]
    }
]
next_id = 1

# POST /recipe - Create a new recipe
@api_blueprint.route('/recipe', methods=['POST'])
def add_recipe():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'ingredients' not in data or 'instructions' not in data:
        return jsonify({"error": "Invalid data"}), 400

    recipe = {
        "id": next_id,
        "author": data['author'],
        "ingredients": data['ingredients'],
        "instructions": data['instructions']
    }
    recipes.append(recipe)
    next_id += 1

    return jsonify(recipe), 201


# GET /recipe - Get a list of all recipes
@api_blueprint.route('/recipe', methods=['GET'])
def get_recipes():
    return jsonify(recipes), 200


# GET /recipe/:id - Get a single recipe by ID
@api_blueprint.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({"error": "Recipe not found"}), 404

    return jsonify(recipe), 200


if __name__ == '__main__':
    app.run(debug=True)
