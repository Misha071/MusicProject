import pandas as pd
from src.utils import logger, timer


REQUIRED_COLUMNS = ["user_id", "track", "artist", "genre", "duration", "timestamp"]


@logger
@timer
def load_data(path):
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"В файле отсутствуют колонки: {missing}")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["day_name"] = df["timestamp"].dt.day_name()
    df["duration_min"] = df["duration"] / 60

    return df