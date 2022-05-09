tweet = str(input("Enter a tweet: "))
sizeTweet = len(tweet)
if sizeTweet < 140:
    print(f"That {sizeTweet} char tweet will work...")
    print(f"{tweet}")
else:
    print(f"Your {sizeTweet} char tweet is {sizeTweet - 140} chars too long")
    print("Rewrite your tweet...")
    