from flask import Flask
from datos import productos

app = Flask(__name__)
app.run(host='0.0.0.0', debug=True)
