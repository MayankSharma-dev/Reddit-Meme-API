from flask import Flask, send_from_directory, render_template,abort
import os
from memescraper import getDefault, getNumRandom, getSubredRandom, getSubredNumRandom, getWithAuthKeys


app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def api():
    return getDefault()
    

@app.route('/<int:num>')
def api_num(num: int):
    return getNumRandom(num)


@app.route('/<string:topic>')
def api_topic(topic: str):
    return getSubredRandom(topic)


@app.route('/<string:topic>/<int:num>')
def meme_api_topic_and_no(topic: str, num: int):
    return getSubredNumRandom(topic, num)


@app.route('/<string:client_key>/<string:secret_key>/<string:app_name>/<string:topic>/<int:num>')
def api_custom_with_auth(client_key: str, secret_key: str, app_name: str, topic: str, num: int):
    return getWithAuthKeys(client_key, secret_key, app_name, topic, num)


@app.route('/about/usage')
def info_about():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(threaded=True)
