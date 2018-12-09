"""
adaptor database backend for Django.

"""

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.base.creation import BaseDatabaseCreation
from django.db.backends.base.introspection import BaseDatabaseIntrospection
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.backends.adaptor.features import AdaptorDatabaseFeatures
from unittest.mock import MagicMock
import logging
import pprint
import sqlparse

logger = logging.getLogger(__name__)

def complain(*args, **kwargs):
    logger.error("complain",*args, **kwargs)
    return MagicMock(*args, **kwargs)
    

from django.db.utils import (DataError,
                             OperationalError,
                             IntegrityError,
                             InternalError,                                                  ProgrammingError,
                             NotSupportedError,
                             DatabaseError,
                             InterfaceError,
                             Error)

def ignore(*args, **kwargs):
    logger.error("Ignore",*args, **kwargs)


class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        return name
    def bulk_insert_sql(self, fields, placeholder_rows):
        logger.error("BULK_insert_sql", fields, placeholder_rows)
        #return "values ({})".format(pprint.pformat([fields,b]))
        placeholder_rows_sql = (", ".join(row) for row in placeholder_rows)
        values_sql = ", ".join("(%s)" % sql for sql in placeholder_rows_sql)
        return "VALUES " + values_sql


class DatabaseClient(BaseDatabaseClient):
    runshell = MagicMock


class DatabaseCreation(BaseDatabaseCreation):
    create_test_db = ignore
    destroy_test_db = ignore

class SomeTable:
    @property
    def type(self):
        return 't'

class DatabaseIntrospection(BaseDatabaseIntrospection):
    table_list = []
    
    def get_table_list(self, cursor):
        return self.table_list
    
    get_table_description = MagicMock
    get_relations = MagicMock
    get_indexes = MagicMock
    get_key_columns = MagicMock

class Connection:
    alias = "default"
    def close(self):
        pass
    def commit(self):
        pass
    def rollback(self):
        pass
class Cursor :
    
    def close(self):
        pass
    def execute(self, sql, params):
        self.wrapper.execute(sql + "\n")
        logger.warning("Cursor.execute", sql, params)
        statement = sqlparse.parse(sql)
        logger.warning("sql_parse", statement)
        logger.warning("sql_parse", pprint.pformat(statement))
        for x in statement:
            logger.warning("sql_parse", pprint.pformat(x))
            #logger.warning("sql_parse tree", pprint.pformat(x._pprint_tree()))
            logger.warning("sql_parse flatten", pprint.pformat([y for y in x.flatten()]))
            #'_pprint_tree', '_token_matching', 'flatten', 'get_alias', 'get_name', 'get_parent_name', 'get_real_name', 'get_sublists', 'get_token_at_offset', 'get_type', 'group_tokens', 'has_alias', 'has_ancestor', 'insert_after', 'insert_before', 'is_child_of', 'is_group', 'is_keyword', 'is_whitespace', 'match', 'normalized', 'parent', 'token_first', 'token_index', 'token_matching', 'token_next', 'token_next_by', 'token_not_matching', 'token_prev', 'tokens', 'ttype', 'value', 'within']]
        #import pdb
        #pdb.set_trace()
    
    @property 
    def lastrowid(self):
        return 1
    
    def fetchmany(self, *args, **kwargs):
        logger.warning("fetchmany",*args, **kwargs)
        raise StopIteration
    
    
class DatabaseWrapper(BaseDatabaseWrapper):
    def __init__(self, db, alias):
        super().__init__(db, alias)
        self.f = open("sql.txt","w")
        self.seen = {}
    def execute(self, sql):
        if sql not in self.seen:
            self.seen[sql]=sql
            self.f.write(sql)
    def create_cursor(self, args):
        if (args):
            logger.warning("create_cursor",*args)
        c = Cursor()
        c.wrapper = self
        return c
    
    def _set_autocommit(self, b):
        pass
    
    def init_connection_state(self):
        pass
    
    def get_connection_params(self):
        pass
    def get_new_connection(self, c):
        return Connection()
    
    exact= 'exact %s'
    
    operators = {
        'exact': exact
    }
    # Override the base class implementations with null
    # implementations. Anything that tries to actually
    # do something raises complain; anything that tries
    # to rollback or undo something raises ignore.
    # _cursor = MagicMock
    # ensure_connection = MagicMock
    # _commit = MagicMock
    # _rollback = ignore
    # _close = ignore
    # _savepoint = ignore
    # _savepoint_commit = MagicMock
    # _savepoint_rollback = ignore
    # _set_autocommit = MagicMock
    # Classes instantiated in __init__().
    class Database:

        from django.db.utils import (DataError,
                                     OperationalError,
                                     IntegrityError,
                                     InternalError,                                     ProgrammingError,NotSupportedError,DatabaseError,InterfaceError,Error)
        
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = AdaptorDatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    class SchemaEditorClass :
        def __init__(self, parent, *args, **kwargs):
            self.parent = parent
            self.connection = Connection()
        def __enter__(self):
            return self
        
        def __exit__(self, a, b, c):
            pass
        def create_model(self, migration):
            logger.warning("create_model",migration)
                
        def atomic_migration(self):
            return False
        def alter_unique_together(self, b,c,d):
            logger.warning("alter_unique_together",b,c,d)
                        
        def alter_field(self, from_model, from_field, to_field):
            logger.warning("alter_field",from_model, from_field, to_field)
                        
        def remove_field(self, from_model, from_field):
            logger.warning("remove_field",from_model, from_field)
                        
    def is_usable(self):
        return True
