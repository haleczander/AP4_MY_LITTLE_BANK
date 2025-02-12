from connect_db import connect

class Repository:
    def __init__( self ):
        self.connection = connect()