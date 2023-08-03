from flask import Flask, render_template, request, jsonify
import main

app = Flask(__name__)
cat_window = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle_cat', methods=['POST'])
def toggle_cat():
    global cat_window
    display_cat = request.json['display_cat']
    if display_cat:
        cat_window = main.run_buddy()
    else:
        if cat_window:
            cat_window.destroy()
            cat_window = None
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
