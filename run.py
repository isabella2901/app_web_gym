from app import create_app

from flask_cors import CORS

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
CORS(app)

#Cross-Origin Resource Sharing
#Cors accesibles desde diferentes dominios