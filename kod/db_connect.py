import oracledb

def connect():
    matt = {"user": "MATT", "pw": "matt"}
    kamilla = {"user": "system", "pw": "oracle"}
    currentU = kamilla
    # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
    dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
    db = oracledb.connect(user=currentU["user"], password=currentU["pw"], dsn=dsn)

    return db