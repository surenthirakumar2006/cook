from flask import Flask, request, render_template_string, make_response
import random

app = Flask(__name__)
FLAG = "expX{c00k13s_4r3_m4g1c_33}"

# Inline SVG for oven image
OVEN_SVG = '''
<svg width="200" height="200" viewBox="0 0 100 100" style="margin:20px auto;display:block">
    <rect x="10" y="20" width="80" height="60" fill="#8B4513" />
    <rect x="15" y="25" width="70" height="50" fill="#A0522D" />
    <rect x="40" y="5" width="20" height="15" fill="#696969" />
    <path d="M30 85 L70 85 L65 95 L35 95 Z" fill="#808080" />
</svg>
'''

HTML = f'''
<!DOCTYPE html>
<html>
<head>
    <title>The Cookie Bakery</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #FFF3E0;
            text-align: center;
        }}
        .message {{
            color: #6D4C41;
            font-size: 1.2em;
            margin: 20px;
        }}
    </style>
    <link rel="icon" href="data:,">
</head>
<body>
    <h1>🍪 The Magic Cookie Oven 🍪</h1>
    {OVEN_SVG}
    {{% if flag %}}
        <div class="message">
            <h2>Perfect Bake! 🎉</h2>
            <p>Flag: <strong>{{{{ flag }}}}</strong></p>
        </div>
    {{% else %}}
        <div class="message">
            <h2>{{{{ message_title }}}}</h2>
            <p>{{{{ message_text }}}}</p>
        </div>
    {{% endif %}}
</body>
</html>
'''

MESSAGES = [
    {"title": "Burnt Cookies! 🔥", "text": "Too hot! Try a cooler temperature."},
    {"title": "Raw Dough! 🥶", "text": "Not enough heat! Needs more warmth."},
    {"title": "Cookie Monster Sad! 😢", "text": "want perfect cookies!"},
     {"title": "Soggy Cookies! 💦", "text": "Too much liquid! Try less milk or butter."},
    {"title": "Rock-Hard Treats! 🪨", "text": "Overbaked! Reduce time for a softer bite."},
    {"title": "Vanishing Cookies! 🏴‍☠️", "text": "Did you eat them already? Or forget the tray?"},
    {"title": "Oops, Salty! 🧂", "text": "Sugar and salt had a mix-up! Double-check next time."},
    {"title": "Flat as a Pancake! 🥞", "text": "Not enough baking powder! Add a little more."},
    {"title": "Choco-Meltdown! 🍫🔥", "text": "Chocolate chips turned into lava! Lower the heat."},
    {"title": "Crumbly Chaos! 🍪💔", "text": "Too dry! Try more butter or an extra egg."},
    {"title": "Burnt Bottom! 🔥⬇️", "text": "Baking sheet too close to the heat! Adjust the rack."},
    {"title": "Sugar Rush! 🍬", "text": "Maybe a little *less* sugar next time?"},
    {"title": "Mystery Flavor! 🕵️‍♂️", "text": "Wait… what did you put in here?!"}
]

@app.route('/')
def index():
    cookie_value = request.cookies.get("cookie")
    if cookie_value and cookie_value.strip() == "61":
        return render_template_string(HTML,
            flag=FLAG,
            message_title="",
            message_text=""
        )
    elif cookie_value:
        msg = random.choice(MESSAGES)
        return render_template_string(HTML,
            flag=None,
            message_title=msg['title'],
            message_text=msg['text']
        )
    else:
        # Set a default cookie value of "0"
        response = make_response(render_template_string(HTML,
            flag=None,
            message_title="Oven Ready! 🌡️",
            message_text="Set cookie for perfect cookies and same as the temp of ip!"
        ))
        response.set_cookie('cookie', '0')
        return response

@app.route('/favicon.ico')
def favicon():
    return app.response_class(status=204)  # No content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5225, debug=False)
