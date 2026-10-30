"""Music catalog and playlist manager."""
import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE songs "
    "(id INTEGER PRIMARY KEY, title TEXT, artist TEXT, plays INTEGER)"
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the db and return the playlist."""
    if playlist is None:
        playlist = []
    # using ? placeholders instead of % so the values can't break the query
    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays)
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Pick a random song id."""
    ids = [r[0] for r in conn.execute("SELECT id FROM songs")]
    return secrets.choice(ids)


def popularity(title):
    """Return popular, niche or unknown based on the play count."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


# json instead of pickle, playlist is just a list of strings
def save_playlist(playlist):
    """Convert the playlist to a json string."""
    return json.dumps(playlist)


def load_playlist(blob):
    """Load a playlist back from a json string."""
    return json.loads(blob)


def total_plays():
    """Total plays of all songs."""
    try:
        total = conn.execute("SELECT SUM(plays) FROM songs").fetchone()[0]
    except sqlite3.Error:
        return 0
    return total or 0


def main():
    """Main function."""
    pl = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, pl)
    blob = save_playlist(pl)
    songs = load_playlist(blob)
    if len(songs) > 1:
        print("multi-song playlist")
    print(popularity("Aurora"), popularity("Monsoon"),
          shuffle_pick(), total_plays())


if __name__ == "__main__":
    main()
