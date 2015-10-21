from twilio.rest import TwilioRestClient
import auth_codes 
from reddit_stripper import grab_headline 

def call_with_headline():
    account_sid = auth_codes.sid
    auth_token = auth_codes.auth_token
    resource_url = "http://twimlets.com/message?Message%5B0%5D=Hello+there,My%20name%20is%20Robert%20Rusch+and+the+top+reddit+post+is+" + grab_headline() + "&"
    client = TwilioRestClient(account_sid, auth_token)
  
  # Make the call
    call = client.calls.create(to="+12282653134",  # Number to Call
                                     from_="+16175130992", # Calling from
                                     url= resource_url)
    print call.sid

if __name__ == "__main__":
    call_with_headline()
