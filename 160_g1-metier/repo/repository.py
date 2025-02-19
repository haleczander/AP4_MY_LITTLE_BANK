from connect_db import connect


class Repository:
    def __init__(self, mapper):
        self.connection = connect()
        self.mapper = mapper
        
    def map_to_dto( self, fetched ):
        return self.mapper.map_to_dto( fetched )
    
    def begin( self, cursor ):
        cursor.execute("BEGIN")
        
    def commit( self, cursor ):
        cursor.execute("COMMIT")
        
    def rollback( self, cursor ):
        cursor.execute("ROLLBACK")
