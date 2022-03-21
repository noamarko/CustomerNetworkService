from flask import Flask


app = Flask()




if __name__ == "__main__":
    app.run("--host=0.0.0.0")