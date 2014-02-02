import sqlite3

_conn = sqlite3.connect('db.db', check_same_thread=False)
_conn.row_factory = sqlite3.Row
_cursor = _conn.cursor()

class PartyModel:
    def __init__(self):
        pass

    @classmethod
    def add_item(cls, item):
        _cursor.execute('INSERT INTO party(text) VALUES(?)', (item, ))
        _conn.commit()

    @classmethod
    def retrieve_category(cls):
        rows = _cursor.execute(
            'SELECT text FROM party ORDER BY id DESC LIMIT ?', (n, )
        )
        return [r['text'] for r in rows]
