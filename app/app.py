from flask import Flask
from flask_graphql import GraphQLView
from controlador.control import schema
from Conexion.db_session import db_session

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Tomorrowland@localhost:5432/Panaderia"
app.debug = True

#db = SQLAlchemy(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
    'graphql', 
    schema=schema,
    graphiql = True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()