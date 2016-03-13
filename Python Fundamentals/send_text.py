from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC98ca69848d5e26962e0355f46e3ff2af" 
AUTH_TOKEN = "fcbf8f57311df3075f3b3aec2f645bb6" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+15202482177", 
    from_="+15207779789", 
    body="This is my first message", 
    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
)
