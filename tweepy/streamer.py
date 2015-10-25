#!/usr/bin/python
__author__ = 'Roelof (graphific)'

from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

class StdOutListener(StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.save_file = tweets

    def on_data(self, data):
        self.save_file.append(json.loads(tweet))
        print tweet
        save_file.write(str(tweet))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tweepy Streamer')
    parser.add_argument('-ck', '--consumer_key', help='twitter auth consumer key', required=True, type=str)
    parser.add_argument('-cs', '--consumer_secret', help='twitter auth consumer secret', required=True, type=str)
    parser.add_argument('-at', '--access_token', help='twitter auth access_token', required=True, type=str)
    parser.add_argument('-ats', '--access_token_secret', help='twitter auth access token secret', required=True, type=str)
    parser.add_argument('-k', '--keywords', help='keywords to search for', required=True, nargs="+", type=str)
    parser.add_argument('-t', '--searchtime', help='time in minutes to search twitter', required=True, type=int)
    parser.add_argument('-o', '--output', help='output filename', required=True, type=str)

    if not args.consumer_key is None and args.consumer_secret is None and not args.access_token is None and not args.access_token_secret is None and not args.keyword is None and not args.searchtime is None:

            l = StdOutListener()
            auth = OAuthHandler(args.consumer_key, args.consumer_secret)
            auth.set_access_token(args.access_token, args.access_token_secret)

            stream = Stream(auth, l)
            stream.filter(track=args.keywords)

            tweets = []
            save_file = open(args.output, 'a')
