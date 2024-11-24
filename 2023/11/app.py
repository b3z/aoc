from flask import Flask, request, render_template_string
from threading import Thread

app = Flask(__name__)

# HTML Template for the homepage
HTML_TEMPLATE = '''
<!doctype html>
<html>
<head><title>Input Form</title></head>
<body>
  <h2>Enter you query:</h2>
  <form method="POST">
      <input name="text">
      <input type="submit">
  </form>
  {% if list_items %}
    <h2>Results:</h2>
    <ul>
    {% for item in list_items %}
      <li>{{ item }}</li>
    {% endfor %}
    </ul>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    res = []
    list_items = None
    if request.method == 'POST':
        input_text = request.form['text']
        res = ['1\tblah', '2\tblah']

    return render_template_string(HTML_TEMPLATE, list_items=res)

if __name__ == '__main__':
    Thread(target=app.run(debug=True, port=8080)).start()
