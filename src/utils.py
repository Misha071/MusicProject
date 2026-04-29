import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] {func.__name__} выполнилась за {end_time - start_time:.6f} сек.")
        return result
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Вызов функции: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def print_basic_info(info):
    print("Базовая информация")
    print(f"Количество строк: {info['rows']}")
    print(f"Количество колонок: {info['columns']}")
    print(f"Названия колонок: {info['column_names']}")
    print(f"Пропуски: {info['missing_values']}")
    print(f"Уникальных пользователей: {info['unique_users']}")
    print(f"Уникальных треков: {info['unique_tracks']}")
    print(f"Уникальных исполнителей: {info['unique_artists']}")
    print(f"Уникальных жанров: {info['unique_genres']}")


def print_report(report):
    print("\nОтчет")
    print(f"Всего прослушиваний: {report['total_listens']}")
    print(f"Самый популярный жанр: {report['top_genre']} ({report['top_genre_count']})")
    print(f"Самый популярный исполнитель: {report['top_artist']} ({report['top_artist_count']})")
    print(f"Самый активный пользователь: {report['top_user']} ({report['top_user_count']})")
    print(f"Самый активный час: {report['top_hour']}:00 ({report['top_hour_count']})")
    print(f"Самый активный день: {report['top_day']} ({report['top_day_count']})")
    print(f"Средняя длительность трека: {report['avg_duration']} сек.")
    print(
        f"Самый длинный трек: {report['longest_track']} — "
        f"{report['longest_track_artist']} ({report['longest_track_duration']} сек.)"
    )
    print(f"Общее время прослушивания: {report['total_minutes']} мин.")