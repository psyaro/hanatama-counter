from datetime import datetime
from time import time
import settings
import requests

def counter(s=settings.s, mode='datetime'):
    if mode == 'timestamp':
        elapsed_unix = int(round(time())) - s
        return elapsed_unix
    delta = datetime.now() - datetime.fromtimestamp(s)
    return f'今日は{delta.days}日目です。良いですね！', delta

def send_to_discord(i=0):
    head = 'https://discord.com/api/webhooks/'
    url = settings.discord_webhooks[i]
    if not head in url:
        url = head + url
    requests.post(url, data=dict(
        content=counter()[0]
    ))
    return 'Done'

def main():
    print(counter())
    send_to_discord()

if __name__ == '__main__':
    main()


