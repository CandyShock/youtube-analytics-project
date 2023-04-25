import os
import json
from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.about_chanel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.title = self.about_chanel['items'][0]['snippet']['title']
        self.video_count = self.about_chanel['items'][0]['statistics']['videoCount']
        self.url = f"https://www.youtube.com/channel/{self._channel_id}"
        self.subscriberCount = self.about_chanel['items'][0]['statistics']['subscriberCount']
        self.viewCount = self.about_chanel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        raise AttributeError

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name):
        with open(file_name, 'w+', encoding='utf-8') as f:
            json.dump({'channel_id': self.channel_id}, f, ensure_ascii=False)
            json.dump({'title': self.title}, f, ensure_ascii=False)
            json.dump({'video_count': self.video_count}, f, ensure_ascii=False)
            json.dump({'url': self.url}, f, ensure_ascii=False)
            json.dump({'subscriberCount': self.subscriberCount}, f, ensure_ascii=False)
            json.dump({'viewCount': self.viewCount}, f, ensure_ascii=False)
