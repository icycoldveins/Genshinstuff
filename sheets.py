import praw
import pandas as pd
import datetime
import json

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent',
                     username='your_username',
                     password='your_password')
# now get top 10 post today of subreddit Genshin
subreddit = reddit.subreddit('Genshin_Impact')

top_subreddit = subreddit.top(time_filter='day', limit=10)

topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
# convert timestamp to date
_timestamp = topics_data["created"].apply(datetime.datetime.fromtimestamp)
topics_data = topics_data.assign(timestamp=_timestamp)
# write to csv file
topics_data.to_csv('Genshin.csv', index=False)
# write to json file
topics_data.to_json('Genshin.json', orient="records")

# what can i do with reddit api for personal use?
