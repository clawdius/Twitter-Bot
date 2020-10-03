import tweepy

app_token = input('Insert your consumer key:')
app_token_secret = input('Insert your consumer secret key:')

auth = tweepy.OAuthHandler(app_token, app_token_secret)

redirect_url = auth.get_authorization_url()

print("Copy link below to your browser and authenticate via twitter:")
print(redirect_url)

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
    print("Save this access token for this account")
    print(auth.access_token)
    print(auth.access_token_secret)
except tweepy.TweepError:
    print('Error getting access token!')