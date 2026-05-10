import argparse

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
    parser = argparse.ArgumentParser(description="Анализ музыкальных прослушиваний")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("info")
    subparsers.add_parser("genres")
    subparsers.add_parser("artists")
    subparsers.add_parser("users")
    subparsers.add_parser("duration")
    subparsers.add_parser("hours")
    subparsers.add_parser("days")
    subparsers.add_parser("genre-duration")
    subparsers.add_parser("report")

    filter_parser = subparsers.add_parser("filter")
    filter_parser.add_argument("--genre", type=str, default=None)
    filter_parser.add_argument("--min_duration", type=int, default=None)

    args = parser.parse_args()

    df = load_data(DATA_PATH)

    if args.command == "info":
        print_basic_info(get_basic_info(df))

    elif args.command == "genres":
        print(genre_stats(df))

    elif args.command == "artists":
        print(artist_stats(df))

    elif args.command == "users":
        print(user_stats(df))

    elif args.command == "duration":
        print_duration_info(duration_stats(df))

    elif args.command == "hours":
        print(hourly_stats(df))

    elif args.command == "days":
        print(daily_stats(df))

    elif args.command == "genre-duration":
        print(genre_duration_stats(df))

    elif args.command == "report":
        print_report(build_report(df))

    elif args.command == "filter":
        result = filter_tracks(df, genre=args.genre, min_duration=args.min_duration)
        print(result)

if __name__ == "__main__":
    main()