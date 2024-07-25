from flask import jsonify,abort
import praw
from praw.models import MoreComments
from random import choice
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import CLIENT_KEY, SECRET_KEY, APP_NAME

reddit = praw.Reddit(client_id=CLIENT_KEY,
                     client_secret=SECRET_KEY, user_agent=APP_NAME)


Meme_subs = ["dankmemes", "memes", "HistoryMemes", "AdviceAnimals", "me_irl", "ComedyCemetery", "terriblefacebookmemes",
             "HindiMemes", "dankinindia", "IndianDankMemes", "indiameme", "ProgrammerHumor", "depression_memes", "YouSeeComrade","funny","comedymemes","wholesomememes","programmingmemes"]


def extract_meme_info(subred, subs):
    if hasattr(subred, 'preview'):
        preview = [i["url"] for i in subred.preview.get("images")[0].get("resolutions")]
    else:
        preview = []
    return {
        "post_link": subred.shortlink,
        "subreddit": subs,
        "top_comments": [comment.body for index, comment in enumerate(subred.comments) if not isinstance(comment, MoreComments) and index < 5],
        "title": subred.title,
        "url": subred.url,
        "nsfw": subred.over_18,
        "ups": subred.ups,
        "author": subred.author.name,
        "author_img": subred.author.icon_img,
        "image_previews": preview
    }

def fetch_meme(subs):
    try:
        subreddit = reddit.subreddit(subs)
        subred = subreddit.random()
        if subred is None:
            raise ValueError(f"No posts found in subreddit: {subs}")
        return extract_meme_info(subred, subs)
    except Exception as e:
        return None

def fetch_memes(num):
    memes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_meme, choice(Meme_subs)) for _ in range(num)]
        for future in as_completed(futures):
            meme = future.result()
            if meme:
                memes.append(meme)
                if len(memes) == num:
                    break
    return memes


def getDefault():
    try:
        subs = choice(Meme_subs)
        subreddit = reddit.subreddit(subs).random()
        memes = [extract_meme_info(subreddit, subs)]
        return jsonify({"count": len(memes), "memes": memes})
    except Exception as e:
        logging.error(e)
        abort(404, description=f"Error fetching subreddit {str(e)}")


def getNumRandom(num):
    if num < 1:
        message = "Enter a positive number greater than 0"
        return jsonify({"code": 400, "message": message}), 400
    if num > 25:
        message = "Enter a positive less 26"
        return jsonify({"code": 400, "message": message}), 400
    memes = fetch_memes(num)
    if(len(memes) == 0):
        abort(404, description="Error fetching")    
    return jsonify({"count": len(memes), "memes": memes})

def getSubredRandom(topic):
    try:
        subred = reddit.subreddit(topic)
        ran = subred.random()
        memes = [extract_meme_info(ran, topic)]
        return jsonify({"count": len(memes), "memes": memes})
    except Exception as e:
        logging.error(f"Error fetching subreddit {topic}: {e}")
        abort(404, description= f"Error fetching subreddit {e}")



def getSubredNumRandom(topic, num):
    if num < 1:
        message = "Enter a positive number greater than 0"
        return jsonify({"code": 400, "message": message}), 400
    if num > 25:
        message = "Enter a positive less 26"
        return jsonify({"code": 400, "message": message}), 400
    
    result = {
        "count": 0,
        "memes": []
    }
    try:
        for subred in reddit.subreddit(topic).random_rising(limit=num):
            try:
                meme = extract_meme_info(subred, topic)
                result["memes"].append(meme)
                result["count"] += 1
            except Exception as e:
                logging.error(f"Error fetching meme: {str(e)}")

        if result["count"] == 0:
            abort(404, description="No memes found for the given subreddit")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error fetching subreddit: {str(e)}")
        if result["count"] == 0:
            return jsonify({"code": 404, "message": "Invalid Subreddit"}), 404
        else:
            result["error message"] = str(e)
            return jsonify(result), 200
        

def getWithAuthKeys(client_key: str, secret_key: str, app_name: str, topic: str, num: int):
    if num < 1:
        message = "Enter a positive number greater than 0"
        return jsonify({"code": 400, "message": message}), 400
    if num > 25:
        message = "Enter a positive less 26"
        return jsonify({"code": 400, "message": message}), 400
    result = {
        "count": 0,
        "memes": []
    }

    redt = praw.Reddit(client_id=client_key,
                       client_secret=secret_key, user_agent=app_name)
    try:
        for subred in redt.subreddit(topic).random_rising(limit=num):
            try:
                meme = extract_meme_info(subred, topic)
                result["memes"].append(meme)
                result["count"] += 1
            except Exception as e:
                logging.error(f"Error fetching meme: {str(e)}")

        if result["count"] == 0:
            return jsonify({"code": 404, "message": "Invalid Subreddit"}), 404
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error fetching subreddit: {str(e)}")
        if result["count"] == 0:
            return jsonify({"code": 404, "message": "Invalid Subreddit"}), 404
        else:
            result["error message"] = str(e)
            return jsonify(result), 200