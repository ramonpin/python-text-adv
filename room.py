import json
import sqlite3

def get_room(id, db):
    ret = None
    con = sqlite3.connect(db)
    for row in con.execute("SELECT json FROM rooms WHERE id = ?", (id,)):
        d = json.loads(row[0])
        ret = Room(id, **d)
        break
    con.close()
    return ret

class Room():
    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbor('n')

    def south(self):
        return self._neighbor('s')

    def east(self):
        return self._neighbor('e')

    def west(self):
        return self._neighbor('w')
