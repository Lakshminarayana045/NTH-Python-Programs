import os
from twilio.rest import Client


# Download the helper library from https://www.twilio.com/docs/python/install
# Set environment variables for your credentials
# Read more at http://twilio/secure

# this id's came in twilio website after Signup 
account_sid = "AC174508b8c6fd105e73241655f5e72538"
auth_token = "b9772965baaf18a28eb01e7747928cbb"
verify_sid = "VAbb9bca3f9932066d7ca3b09cfc5f0e7f"

# send number
sending_number = "+918179565761"
# receiver number 
receiver_number = " +919373375729"

# login server
client = Client(account_sid, auth_token)


verification = client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=receiver_number,channel="sms")












# print(verification.status)
'''
otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
    .verification_checks \
    .create(to=verified_number, code=otp_code)
print(verification_check.status)
'''
