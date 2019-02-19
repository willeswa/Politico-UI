from app import create_app
from flasgger import Swagger


app = create_app('production')
app.config['SWAGGER'] = {
    "swagger": "2.0",
    "info": {
        "title": "Politico-API",
        "contact": {
            "email": "gwiliez@ymail.com",
            "mobile": "0725175171"
        },
        "description": """
        This is the official documentation of the Politico API.
        Use these endpoints to create a voting system
        """,
        "version": "2.0",
        "license": {
            "name": "MIT license",
            "url": "https://opensource.org/licenses/MIT"
        }
    },
    'securityDefinitions': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
swagger = Swagger(app)
# introduce CORS


@app.route('/api/v2/auth/signup', methods=['POST'])
def signup():
    """ This endpoint registers a user.
    ---
    tags:
        - Users
    parameters:
      - in: body
        name: Users
        required: true
        schema:
          type: object
          properties:
            firstname:
              type: string
              example: "Wanjala"
            lastname:
              type: string
              example: "Willies"
            othername:
              type: string
              example: "Godfrey"
            email:
              type: string
              example: "gwiliez@gmail.com"
            phone_number:
              type: string
              example: "0725175171"
            passport_url:
              type: string
              example: "http://link"
            password:
              type: string
              example: "tangatanga"
    responses:
      '201':
        description: CREATED!
      '409':
        description: CONFLICT
      '400':
        description: BAD REQUEST
    """
@app.route('/api/v2/auth/signin', methods=['POST'])
def signin():
    """ This endpoint signs in the user.
    ---
    tags:
        - Users
    parameters:
      - in: body
        name: Users
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "gwiliez@gmail.com"
            password:
              type: string
              example: "tangatanga"
    responses:
      '200':
        description: SUCCESS!
      '400':
        description: BAD REQUEST
    """

if __name__ == "__main__":
    app.run()
