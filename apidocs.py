from app import create_app
from flasgger import Swagger


app = create_app('production')
app.config['SWAGGER'] = {
    "swagger": "2.0",
    "API version": "v2",
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
    """ User signup endpoint.
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
              example: "ericcartman@gmail.com"
            phone_number:
              type: string
              example: "0725175171"
            passport_url:
              type: string
              example: "http://link"
            password:
              type: string
              example: "mrcartman"
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
    """ User signin endpoint.
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
              example: "ericcartman@gmail.com"
            password:
              type: string
              example: "mrcartman"
    responses:
      '200':
        description: SUCCESS!
      '400':
        description: BAD REQUEST
    """
@app.route('/api/v2/offices', methods=['POST'])
def create_office():
    """ Create an office endpoint .
    ---
    tags:
        - Offices
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: body
        name: Offices
        required: true
        schema:
          type: object
          properties:
            office_name:
              type: string
              description: "A three named phrase that ends with party"
              example: "Tangatanga Movement Party"
            office_type:
              type: string
              example: "Legislative"
    responses:
      '200':
        description: SUCCESS!
      '400':
        description: BAD REQUEST
      '401':
        description: UNAUTHORIZED
    """
@app.route('/api/v2/offices', methods=['GET'])
def get_all_offices():
    """ Get all offices endpoint.
    ---
    tags:
        - Offices
    responses:
      '200':
        description: SUCCESS!
    """
@app.route('/api/v2/offices/<int:office_id>', methods=['GET'])
def get_specific_office(office_id):
    """ Get specific office endpoint.
    ---
    tags:
        - Offices
    parameters:
      - in: path
        name: office_id
        required: true
        type: integer
    responses:
      '200':
        description: SUCCESS!
      '404':
        description: NOT FOUND
    """

@app.route('/api/v2/parties', methods=['POST'])
def create_parties():
    """ Create party endpoint.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: body
        name: Parties
        required: true
        schema:
          type: object
          properties:
            party_name:
              type: string
              example: "TangaTanga Catwalking Party"
            hq_address:
              type: string
              example: "Center of Kenya"
            logo_url:
              type: string
              example: "http://twk"
    responses:
      '201':
        description: CREATED
      '409':
        description: CONFLICT
      '422':
        description: UNPROCESSABLE
      '400':
        description: BAD REQUEST
    """


@app.route('/api/v2/parties', methods=['GET'])
def get_all_parties():
    """ Get all parties endpoint.
    ---
    tags:
        - Parties
    responses:
      '200':
        description: SUCCESS
    """


@app.route('/api/v2/parties/<int:party_id>', methods=['GET'])
def get_specific_party(party_id):
    """ Get specific party endpoint.
    ---
    tags:
        - Parties
    parameters:
      - in: path
        name: party_id
        required: true
        type: integer
    responses:
      '200':
        description: SUCCESS!
      '404':
        description: NOT FOUND
    """


@app.route('/api/v2/parties/<int:party_id>', methods=['DELETE'])
def delete_specific_party(office_id):
    """ Delete specific party endpoint.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: path
        name: party_id
        required: true
        type: integer
    responses:
      '200':
        description: SUCCESS
      '404':
        description: NOT FOUND
      '401':
        description: UNAUTHORIZED
    """


@app.route('/api/v2/parties/<int:party_id>/name', methods=['PUT'])
def patch_single_party(party_id):
    """ Update party name endpoint.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: path
        name: party_id
        required: true
        type: integer
      - in: body
        name: Party Name
        required: true
        schema:
          type: object
          properties:
            party_name:
              type: string
              example: Temema Political Party
    responses:
      '200':
        description: SUCCESS
      '404':
        description: NOT FOUND
      '401':
        description: UNAUTHORIZED
    """

@app.route('/api/v2/api/v2/office/<int:office_id>/register', methods=['POST'])
def register_candidate():
    """ Register candidate endpoint.
    ---
    tags:
        - Candidates
    parameters:
      - in: body
        name: Candidate
        required: true
        schema:
          type: object
          properties:
            candidate_id:
              type: int
              example: 1
            party_id:
              type: int
              example: 1
    responses:
      '201':
        description: CREATED!
      '409':
        description: CONFLICT
      '400':
        description: BAD REQUEST
      '404':
        description: NOT FOUND
    """


if __name__ == "__main__":
    app.run()
