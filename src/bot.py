import tweepy
import time

#authentication
auth = tweepy.OAuthHandler("fKvZSEFPJ2gGDq5FhOpEh1izV", "woP6uEaMF9nS8tcr8O9PimF7uEPP6ZX89vy1DnOQMwtac7OGRe")
auth.set_access_token("1576851334569299969-qxQ9Bg1CdMm1uys2LTrCDCAsOyh72Q", "v4mcBa6vnC7QdztkwACYSU3ACm4Y64RhNklnsbtgGYCe1")
 
time_running = 3600 #an hour for looping time
time_running_saver = time_running

while time_running != 0:
    time.sleep(1)
    time_running -= 1
    
    if time_running == 0:
        time_running = time_running_saver
        
        #using tweepy to tweet
        api = tweepy.API(auth)
        api.update_status("another test")

