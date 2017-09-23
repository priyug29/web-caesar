from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = 'POST'>
            <lebel>Rotated by:
                <input type = "text" name = "rot" value = "0"/>
            </lebel>
            <lebel>
                <textarea name = text>{0}</textarea>
            </lebel>
            <input type = "Submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])
def encrypt():
    
    rotate_by = int(request.form['rot'])
    input_text = request.form['text']

    encrypted_string = rotate_string(input_text, rotate_by)

    return form.format(encrypted_string) 


app.run()
