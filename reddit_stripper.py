import praw
from urllib import quote_plus
def grab_headline():    
    r = praw.Reddit(user_agent='Grabbing the top')
    posts = r.get_front_page(limit=1)
    #change to single generator
    for post in posts:
        top_post_name =  post.title
    reddit_post = quote_plus(top_post_name)
    return reddit_post
