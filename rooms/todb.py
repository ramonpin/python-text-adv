import sys
import sqlite3
import os
import os.path

def main(dbname):
    con = sqlite3.connect(dbname)

    con.execute("CREATE TABLE IF NOT EXISTS rooms(id, INTEGER PRIMARY KEY, json TEXT NOT NULL)")

    for filename in os.listdir():
        base, extension = os.path.splitext(filename)
        if extension == '.json':
            with open(filename, 'r') as f:
                json = f.read()
                print("Inserting room {0}".format(int(base)))

                con.execute("INSERT OR REPLACE INTO rooms (id, json) VALUES (?, ?)",
                            (int(base), json))
                con.commit()

if __name__ == "__main__":
    main(sys.argv[1])
