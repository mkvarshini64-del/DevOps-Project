from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": "Hello from DevOps Project"}

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="127.1.1.6", port=5000, debug=True)