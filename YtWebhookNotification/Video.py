import requests
import re
from discord_webhook import DiscordWebhook

class Video:

    def __init__(self, WebhookUrl, channel_url, channel_name, message):
        self.WebhookUrl = WebhookUrl
        self.channel_url = channel_url
        self.channel_name = channel_name
        self.message = message

    def CheckForUploads(self):
        html = requests.get(self.channel_url+"/videos").text


        try:
            latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
        except:
            pass

        PrevUrl = None
        webhook = DiscordWebhook(url=self.WebhookUrl, content=self.message)
        if PrevUrl==None:
            webhook.execute()
        elif not PrevUrl == latest_video_url:
            PrevUrl = latest_video_url
            webhook.execute()