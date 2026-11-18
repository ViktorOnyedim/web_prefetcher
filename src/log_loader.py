import pandas as pd

class LogLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_logs(self):
        """
        Load web access logs.
        Expected columns:
        user_id, url, timestamp
        """
        df = pd.read_csv(
            self.file_path,
            parse_dates=["timestamp"]
        )

        # Sort for proper session creation
        df.sort_values(by=["user_id", "timestamp"], inplace=True)

        return df
