from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
import jwt
from flask import request, jsonify

from nautilus import app, schema
from nautilus.utils import env


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """On GET request serve GraphQL Playground."""
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    """GraphQL queries are always sent as POST"""
    data = request.get_json()
    auth_header = request.headers.get('Authorization')
    auth_token = auth_header.split()[1] if auth_header else ''

    try:
        jwt_token = jwt.decode(auth_token, key=env.get('jwt_secret'))
    except jwt.exceptions.InvalidTokenError:
        return jsonify({"success": False, "message": "Invalid authentication token"}), 401

    print(jwt_token)

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema, data, context_value=request, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
