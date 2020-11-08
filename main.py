from slack_sdk import WebClient
from ssl import SSLContext

sslcert = SSLContext()

client = WebClient(
    token='<your-token-number>',
    ssl=sslcert
)
response = client.chat_postMessage(channel="#slack-test", text="Slacker test")
print(response)