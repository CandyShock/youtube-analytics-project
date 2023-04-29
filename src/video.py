from helper.youtube_api_manual import youtube


class Video:

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.about_chanel = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=video_id
                                                  ).execute()
        self.title = self.about_chanel['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.viewCount = self.about_chanel['items'][0]['statistics']['viewCount']
        self.like_count = self.about_chanel['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"{self.title}"


class PLVideo:

    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.about_palaylist = youtube.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        self.about_chanel = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=video_id
                                                  ).execute()
        self.title = self.about_chanel['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.viewCount = self.about_chanel['items'][0]['statistics']['viewCount']
        self.like_count = self.about_chanel['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"{self.title}"
