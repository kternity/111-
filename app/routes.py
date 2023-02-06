from flask import Flask       #From the flask module import the Flask class

app = Flask(__name__)         #Create an instance of the Flast class into the app variable (now an object)

@app.get("/")                 # Flask decorator that creates routes.
def index():                  # Flask calls these "view functions".
   me = {                     # Python dictionary with key/value pairs.
      "first_name": "Kenneth",
      "last_name": "Chung",
      "hobbies": "Basketball",
      "is_active": True
   }
   return me                  # When a view function returns a dictionary, flast automatically converts it to JSON.