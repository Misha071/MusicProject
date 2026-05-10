import pandas as pd
import pytest

from src.data_loader import load_data
from src.analysis import (
    get_basic_info,
    genre_stats,
    artist_stats,
    user_stats,
    hourly_stats,
    daily_stats,
    genre_duration_stats,
    duration_stats,
    filter_tracks,
    build_report,
)
from src.utils import row_generator, filtered_track_generator, chunk_generator


@pytest.fixture
def sample_df():
    data = {
        "user_id": [1, 1, 2, 2, 3],
        "track": ["A", "B", "C", "D", "E"],
        "artist": ["X", "Y", "X", "Z", "Y"],
        "genre": ["pop", "rock", "pop", "jazz", "rock"],
        "duration": [200, 150, 220, 300, 180],
        "timestamp": [
            "2026-01-01 10:00:00",
            "2026-01-01 11:00:00",
            "2026-01-02 10:00:00",
            "2026-01-03 15:00:00",
            "2026-01-04 15:00:00",
        ],
    }
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["day_name"] = df["timestamp"].dt.day_name()
    df["duration_min"] = df["duration"] / 60
    return df


def test_get_basic_info(sample_df):
    info = get_basic_info(sample_df)
    assert info["rows"] == 5
    assert info["unique_users"] == 3
    assert info["unique_genres"] == 3


def test_genre_stats(sample_df):
    stats = genre_stats(sample_df)
    assert stats["pop"] == 2
    assert stats["rock"] == 2
    assert stats["jazz"] == 1


def test_artist_stats(sample_df):
    stats = artist_stats(sample_df)
    assert stats["X"] == 2


def test_user_stats(sample_df):
    stats = user_stats(sample_df)
    assert stats[1] == 2
    assert stats[2] == 2
    assert stats[3] == 1


def test_hourly_stats(sample_df):
    stats = hourly_stats(sample_df)
    assert stats[10] == 2
    assert stats[11] == 1
    assert stats[15] == 2


def test_daily_stats(sample_df):
    stats = daily_stats(sample_df)
    assert stats.sum() == 5


def test_genre_duration_stats(sample_df):
    result = genre_duration_stats(sample_df)
    assert "listens" in result.columns
    assert "avg_duration" in result.columns
    assert "total_duration" in result.columns


def test_duration_stats(sample_df):
    stats = duration_stats(sample_df)
    assert stats["min"] == 150
    assert stats["max"] == 300


def test_filter_tracks(sample_df):
    result = filter_tracks(sample_df, genre="pop", min_duration=210)
    assert len(result) == 1
    assert result.iloc[0]["track"] == "C"


def test_build_report(sample_df):
    report = build_report(sample_df)
    assert report["total_listens"] == 5
    assert "top_genre" in report
    assert "top_artist" in report
    assert "top_user" in report


def test_row_generator(sample_df):
    rows = list(row_generator(sample_df))
    assert len(rows) == 5


def test_filtered_track_generator(sample_df):
    rows = list(filtered_track_generator(sample_df, genre="rock"))
    assert len(rows) == 2


def test_chunk_generator(sample_df):
    chunks = list(chunk_generator(sample_df, chunk_size=2))
    assert len(chunks) == 3
    assert len(chunks[0]) == 2


def test_load_data_missing_columns(tmp_path):
    bad_df = pd.DataFrame({"a": [1], "b": [2]})
    file_path = tmp_path / "bad.csv"
    bad_df.to_csv(file_path, index=False)

    with pytest.raises(ValueError):
        load_data(file_path)