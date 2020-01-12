from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/closet', methods=['POST'])
def saving():
    image_receive = request.form['image_give']
    category_receive = request.form['category_give']
    title_receive = request.form['title_give']

    item = {
        'image': image_receive,
        'category': category_receive,
        'title': title_receive
    }

    db.items.insert_one(item)

    return jsonify({'result': 'success'})


@app.route('/closet', methods=['GET'])
def listing():
    result = list(db.items.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'clothes': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
