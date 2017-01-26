class Song:
    def __init__(self, x):
        self._x = x

    @property
    def artist(self):
        return "file"

    @property
    def title(self):
        return "not found"

    @property
    def timestamp(self):
        return "-1"

    @property
    def track_id(self):
        return "given_id" # should be whatever track_id was given

    @property
    def tags(self):
        return []

    @property
    def similars(self):
        return []

    def get_tags(self, limit=0):
        return []

    def get_similars(self, limit=0):
        return []

    def shared_tags(self, other_song_instance):
        return ()

    def combined_tags(self, other_song_instance):
        return ()
