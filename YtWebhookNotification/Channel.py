import requests
import re
from discord_webhook import DiscordWebhook

class Channel():
    def CheckForNewUploads(WebhookUrl:str, channel_url:str, message:str):
        html = requests.get(channel_url+"/videos").text

        try:
            latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
        except:
            pass

        PrevUrl = None
        webhook = DiscordWebhook(url=WebhookUrl, content=message)
        if PrevUrl==None:
            PrevUrl = latest_video_url
            webhook.execute()
        elif not PrevUrl == latest_video_url:
            PrevUrl = latest_video_url
            webhook.execute()