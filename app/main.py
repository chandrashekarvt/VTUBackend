from flask import Flask, jsonify
from app.DataRetriever import getData


app = Flask(__name__)


@app.route('/1')
def circular1():
    data = getData('https://vtu.ac.in/en/category/administration/')
    return jsonify(data)

@app.route('/2')
def circular2():
   data = getData( 'https://vtu.ac.in/category/examination/')
   return jsonify(data)
