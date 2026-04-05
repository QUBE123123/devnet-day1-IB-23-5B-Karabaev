from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello DevNet! TOKEN_HASH8=f0c3a881\n"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
