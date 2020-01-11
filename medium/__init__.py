from medium.controllers.home import home
from flask import Flask

app = Flask("mediumFlask", template_folder='medium/templates',
            static_folder='medium/static')
app.register_blueprint(home)
