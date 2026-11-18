import pandas as pd

class Sessionizer:
    def __init__(self, timeout_minutes=30):
        self.timeout = pd.Timedelta(minutes=timeout_minutes)

    def create_sessions(self, df):
        """
        Create sessions using time-based heuristics.
        """
        df = df.copy()

        df["time_diff"] = df.groupby("user_id")["timestamp"].diff()
        df["new_session"] = df["time_diff"] > self.timeout

        df["session_id"] = df.groupby("user_id")["new_session"].cumsum()

        return df
