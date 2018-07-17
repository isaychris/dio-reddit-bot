# dio-reddit-bot

This is a comment bot for reddit which uses the praw api to respond to latest comments from /r/anime that contain the word dio with a picture of dio.

![Image](https://i.imgur.com/l60egHd.gif)
### Prerequisites
* Reddit App 
* Python 3
* PRAW Api

### Setup
To install the bot & its dependencies, run the following command:
```
python setup.py install
```

### Usage
Simply insert your reddit app info into config.ini and run the following command in a tmux session:
```
python3 bot.py