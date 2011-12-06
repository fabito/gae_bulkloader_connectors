#!/usr/bin/env python
"""A bulkloader connector to read data from Oracle selects.
"""
from google.appengine.ext.bulkload import connector_interface
from google.appengine.ext.bulkload import bulkloader_errors
import cx_Oracle
import os.path

class OracleConnector(connector_interface.ConnectorInterface):

  @classmethod
  def create_from_options(cls, options, name):
    """Factory using an options dictionary.

    Args:
      options: Dictionary of options:
        columns: sql query to perform, each selected column becomes a column
      name: The name of this transformer, for use in error messages.

    Returns:
      OracleConnector object described by the specified options.

    Raises:
      InvalidConfiguration: If the config is invalid.
    """
    columns = options.get('columns', None)
    if not columns:
        raise bulkloader_errors.InvalidConfiguration(
            'Sql query must be specified in the columns '
            'configuration option. (In transformer name %s.)' % name)

    return cls(columns)

  def __init__(self, sql_query):
    """Initializer.

    Args:
      sql_query: (required) select query which will be sent to database. The returned columns/aliases will be used as the connectors column names
    """
    self.sql_query = unicode(sql_query)

  def generate_import_record(self, filename, bulkload_state):
    """Generator, yields dicts for nodes found as described in the options.

    Args:
      filename: py script containing oracle database connection properties: host, port, uid, pwd and service.
      bulkload_state: Passed bulkload_state.

    Yields:
      Neutral dict, one per row returned by the sql query
    """
    dbprops = __import__(os.path.splitext(filename)[0])
    dsn_tns = cx_Oracle.makedsn(dbprops.host, dbprops.port, dbprops.service)
    connection = cx_Oracle.connect(dbprops.uid, dbprops.pwd, dsn_tns)
    cursor = connection.cursor()
    cursor.arraysize = dbprops.cursor_arraysize
    cursor.execute(self.sql_query)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    for row in cursor.fetchall():
       decoded_dict = {}
       for i in range(num_fields):
         decoded_dict[field_names[i]] = row[i]
       yield decoded_dict    
    cursor.close()
    connection.close()
