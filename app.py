from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/closet', methods=['POST'])
def saving_outerwear():
    outerwear_image_receive = request.form['outerwear_image_give']
    outerwear_category_receive = request.form['outerwear_category_give']
    outerwear_title_receive = request.form['outerwear_title_give']

    outerwear = {
        'image': outerwear_image_receive,
        'category': outerwear_category_receive,
        'title': outerwear_title_receive
    }

    db.outerwears.insert_one(outerwear)

    return jsonify({'result': 'success'})


@app.route('/closet', methods=['GET'])
def listing_outerwear():
    result = list(db.outerwears.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'outerwears': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
