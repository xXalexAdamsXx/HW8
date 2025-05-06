from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def base():
    return(
        "<h1 style='text-align: center;'>WELCOME TO ALEX'S PYTHON WEBSITE!</h1>"
        "<div style='display: flex; justify-content: center; padding: 2px;'>"
            "<form action='/home'><button style='margin: 5px;'>REDIRECT TO HOME</button></form>"
            "<form action='/page1'><button style='margin: 5px;'>REDIRECT TO PAGE 1</button></form>"
            "<form action='/page2'><button style='margin: 5px;'>REDIRECT TO PAGE 2</button></form>"
        "</div>"
    )

@app.route('/home')
def home():
    return(
        "<body style='background-color: gray'>"
            f"<div style='margin: auto; display: flex; justify-content: center;'>"
                f"<h1>WELCOME TO ALEX'S HOME PAGE</h1>" 
            f"</div>"
            "<div style='display: flex; justify-content: center; padding: 2px;'>"
                "<form action='/page1'><button style='margin: 5px;'>REDIRECT TO PAGE 1</button></form>"
                "<form action='/page2'><button style='margin: 5px;'>REDIRECT TO PAGE 2</button></form>"
            "</div>"

        "</>"
    )


@app.route('/page1')
def page_one():
    return(
        "<body style='background-color: red'>"
            "<div style='text-align: center;'>"
                "<h1>Welcome to page 1!</h1> <h2>Click on the button for the page that you want to go to.</h2>"
            "</div>"
            "<div style='display: flex; justify-content: center; padding: 2px;'>"
                "<form action='/home'><button style='margin: 5px;'>REDIRECT TO HOME</button></form>"
                "<form action='/page2'><button style='margin: 5px;'>REDIRECT TO PAGE 2</button></form>"
            "</div>"
        "</body>"
    )

@app.route('/page2', methods=['GET', 'POST'])
def page_two():

    username = ''
    if request.method=='POST':
        username = request.form.get('username', 'Unknown user')


    return(
        "<body style='background-color: yellow'>"
            "<div style='text-align: center;'>"
                f"<h1>{'Hello, ' + username if username else 'Welcome to Page 2'}</h1>"
            "</div>"
            "<div style='display: flex; justify-content: center; padding: 2px;'>"
                "<form action='/home'><button style='margin: 5px;'>REDIRECT TO HOME</button></form>"
                "<form action='/page1'><button style='margin: 5px;'>REDIRECT TO PAGE 2</button></form>"
            "</div>"

            "<h2>Simple form</h2>"
            "<form method='POST' style='display: flex; flex-direction: column; justify-content: center;'>"
                "<input name='username' placeholder='Your name' style='width: 10rem; margin: 10px;' type='text'></input>"
                "<label for='username'>I haven't implimented any security on this form. Please don't do an HTML injection</label>"
                "<input style='width: 10rem; margin: 10px;' type='submit'></input>"
            "</form>"
        "</body>"
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001)