from slacker import Slacker

slack = Slacker('<your-token-number>')
# Send a message to #general channel
slack.chat.post_message('#general', 'Slacker Test')