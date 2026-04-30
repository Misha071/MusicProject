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
from src.utils import print_basic_info, print_duration_info, print_report


DATA_PATH = "data/music.csv"


def main():
    df = load_data(DATA_PATH)

    info = get_basic_info(df)
    print_basic_info(info)

    print("\nЖанры: ")
    print(genre_stats(df))

    print("\nИсполнители: ")
    print(artist_stats(df))

    print("\nПользователи: ")
    print(user_stats(df))

    print("\nЧасы: ")
    print(hourly_stats(df))

    print("\nДни: ")
    print(daily_stats(df))

    print("\nЖанры и длительность")
    print(genre_duration_stats(df))

    duration = duration_stats(df)
    print_duration_info(duration)

    print("\n=== ФИЛЬТР: POP И ДЛИТЕЛЬНОСТЬ >= 200 ===")
    print(filter_tracks(df, genre="pop", min_duration=200).head())

    report = build_report(df)
    print_report(report)


if __name__ == "__main__":
    main()