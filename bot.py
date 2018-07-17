import praw
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')
cache = "replied_comments.txt"

def bot_login():
    print("Logging into Reddit ... ")
    bot = praw.Reddit(
        user_agent="DIO_BOT",
        username=config['AUTH']['USERNAME'],
        password=config['AUTH']['PASSWORD'],
        client_id=config['AUTH']['CLIENT_ID'],
        client_secret=config['AUTH']['CLIENT_SECRET'])
    return bot

def run_bot(bot, replied_comments):
    latest_comments = bot.subreddit('anime').stream.comments()

    for comment in latest_comments:
        if " dio " in comment.body.lower() and comment.id not in replied_comments and comment.author != bot.user.me():
            comment.reply('https://i.imgur.com/l60egHd.gif')

            replied_comments.append(comment.id)
            with open(cache, "a") as f:
                f.write(comment.id + "\n")

            print('BOT replied to comment {}'.format(str(comment.id)))

    time.sleep(30)

def load_replied_comments():
    with open(cache, "a+") as f:
        comments = f.read().split("\n")

    return comments

def main():
    bot = bot_login()
    cache = load_replied_comments()

    while True:
        run_bot(bot, cache)

main()