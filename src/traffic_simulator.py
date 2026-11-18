import random
import pandas as pd
from datetime import datetime, timedelta

class TrafficSimulator:
    def __init__(self, users=10000, pages=20, sessions_per_user=3):
        self.users = users
        self.pages = pages
        self.sessions = sessions_per_user

    def generate(self):
        data = []
        base_time = datetime.now()

        for user in range(self.users):
            for s in range(self.sessions):
                session_length = random.randint(3, 10)
                t = base_time

                for _ in range(session_length):
                    url = f"/page{random.randint(1, self.pages)}"
                    data.append([user, url, t])
                    t += timedelta(seconds=random.randint(1, 30))

        return pd.DataFrame(
            data, columns=["user_id", "url", "timestamp"]
        )
