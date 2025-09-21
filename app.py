from flask import Flask, render_template
app = Flask(__name__)


@app.route("/") #들어갔을 때 바로 보여지는 페이지
def home():
    return render_template("/index.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("/register.html")


if __name__ == '__main__':
    app.run()