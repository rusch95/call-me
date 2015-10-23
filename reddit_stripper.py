import praw
from urllib import quote_plus
#Uses Praw as an API request handler
def grab_headline():    
    r = praw.Reddit(user_agent='Lets Type A Random String awoijf')
    #Only grab the top post
    posts = r.get_front_page(limit=1)
    #Generate title of top post
    for post in posts:
        top_post_name =  post.title
    #Encode so that the top title is url safe
    reddit_post = quote_plus(top_post_name)
    return reddit_post

if __name__ == "__main__":
    print grab_headline()
