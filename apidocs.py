"""Contain interactive documentation to help one get started using the API
"""
import os

from flasgger import Swagger

from app import create_app


app = create_app('config.ProductionConfig')
swagger = Swagger(app)


# Users
@app.route('/api/v3/auth/register', methods=["POST"])
def signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
    """


if __name__ == "__main__":
    app.run()
