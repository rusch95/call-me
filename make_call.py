from twilio.rest import TwilioRestClient
import auth_codes 
from reddit_stripper import grab_headline 

def call_with_headline():
    #Codes are imported from ignored local python file.
    account_sid = auth_codes.sid
    auth_token = auth_codes.auth_token
    #Concatenates a predefined message with the url encoded headline
    #Resource url points to a speaking app that reads the POST request
    resource_url = ("http://twimlets.com/message?Message%5B0%5D=Hello+there,"
                    "My%20name%20is%20Robert%20Rusch+and+the+top+reddit+post"
                    "+right+now+is+,.+" + grab_headline() + "&")
    
    client = TwilioRestClient(account_sid, auth_token)
  
  # Make the call
    call = client.calls.create(to="+16173098954",  # Number to Call
                                     from_="+16175130992", # Calling From
                                     url= resource_url) #Using this online asset
    print call.sid

if __name__ == "__main__":
    call_with_headline()
