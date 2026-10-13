# app.py - Visual Search + SQL - FINAL
import sqlite3
import os
from flask import Flask, request, render_template_string
from model import get_embedding, find_similar
import numpy as np

app = Flask(__name__)

# Database connect
conn = sqlite3.connect('cloth.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("SELECT * FROM clothing_items")
items = cursor.fetchall()
print(f"Total kapde DB me: {len(items)}")
for item in items:
    print(item)

# Simple HTML
HTML_PAGE = """
<h2>🧥 Cloth Search - DAVV Project</h2>
<p>Total items: {{count}}</p>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="image">
    <button type="submit">Search Similar</button>
</form>
{% if results %}
<h3>Results:</h3>
<ul>
{% for r in results %}
<li>{{r}}</li>
{% endfor %}
</ul>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    if request.method == 'POST':
        results = items  # abhi ke liye saare items dikhayenge
    return render_template_string(HTML_PAGE, count=len(items), results=results)

if __name__ == '__main__':
    print("Website starting...")
    app.run(debug=True)