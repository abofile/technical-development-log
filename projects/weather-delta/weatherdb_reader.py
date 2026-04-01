import sqlite3

with sqlite3.connect("weather_log.db") as conn:
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM weather_log_api").fetchall()

    for row in rows:
        print(f"{row['recorded_at']} | {row['temp']}° | {row['humidity']}% humidity")
