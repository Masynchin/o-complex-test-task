import datetime as dt
from collections import Counter

from app.exceptions import EmptyHistory

class History:
    def __init__(self):
        self.hits = []

    def add(self, user_id, city: str):
        self.hits.append((user_id, city, dt.datetime.now()))

    def latest(self, user_id) -> str:
        user_cities = [(city, ts) for (id, city, ts) in self.hits if id == user_id]
        try:
            latest = max(user_cities, key=lambda p: p[1])
            return latest[0]
        except ValueError:
            raise EmptyHistory()

    def stats(self, user_id) -> Counter:
        return Counter(city for (_, city, _) in self.hits)
