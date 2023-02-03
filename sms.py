from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
                              messaging_service_sid='',
                              body='Sent from my computer!!!',
                              to=''
                          )

print(message.sid)
