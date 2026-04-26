def get_basic_info(df):
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
        "missing_values": df.isna().sum().to_dict(),
        "unique_users": int(df["user_id"].nunique()),
        "unique_tracks": int(df["track"].nunique()),
        "unique_artists": int(df["artist"].nunique()),
        "unique_genres": int(df["genre"].nunique()),
    }


def genre_stats(df):
    return df["genre"].value_counts()


def artist_stats(df, top_n=10):
    return df["artist"].value_counts().head(top_n)


def user_stats(df):
    return df["user_id"].value_counts()


def hourly_stats(df):
    return df["hour"].value_counts().sort_index()


def daily_stats(df):
    order = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    result = df["day_name"].value_counts()
    return result.reindex(order, fill_value=0)


def genre_duration_stats(df):
    return (
        df.groupby("genre")
        .agg(
            listens=("track", "count"),
            avg_duration=("duration", "mean"),
            total_duration=("duration", "sum"),
        )
        .sort_values("listens", ascending=False)
        .round(2)
    )


def build_report(df):
    genre_counts = df["genre"].value_counts()
    artist_counts = df["artist"].value_counts()
    user_counts = df["user_id"].value_counts()
    hour_counts = df["hour"].value_counts()
    day_counts = df["day_name"].value_counts()

    longest_track = df.loc[df["duration"].idxmax()]
    avg_duration = df["duration"].mean()
    total_minutes = df["duration"].sum() / 60

    return {
        "total_listens": int(len(df)),
        "top_genre": genre_counts.idxmax(),
        "top_genre_count": int(genre_counts.max()),
        "top_artist": artist_counts.idxmax(),
        "top_artist_count": int(artist_counts.max()),
        "top_user": int(user_counts.idxmax()),
        "top_user_count": int(user_counts.max()),
        "top_hour": int(hour_counts.idxmax()),
        "top_hour_count": int(hour_counts.max()),
        "top_day": day_counts.idxmax(),
        "top_day_count": int(day_counts.max()),
        "avg_duration": round(float(avg_duration), 2),
        "longest_track": str(longest_track["track"]),
        "longest_track_artist": str(longest_track["artist"]),
        "longest_track_duration": int(longest_track["duration"]),
        "total_minutes": round(float(total_minutes), 2),
    }