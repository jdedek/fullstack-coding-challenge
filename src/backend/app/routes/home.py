from flask import current_app as app
from flask import render_template

@app.route('/api')
def test(name=None):
    return render_template('index.html')