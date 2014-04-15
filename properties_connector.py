#!/usr/bin/env python
"""A bulkloader connector to read data from Java Property Files.
"""
from google.appengine.ext.bulkload import connector_interface
from google.appengine.ext.bulkload import bulkloader_errors
import os.path
import properties

class PropertyConnector(connector_interface.ConnectorInterface):

  @classmethod
  def create_from_options(cls, options, name):
    """Factory using an options dictionary.

    Args:
      options: Dictionary of options:
        columns: sql query to perform, each selected column becomes a column
      name: The name of this transformer, for use in error messages.

    Returns:
      PropertyConnector object described by the specified options.

    Raises:
      InvalidConfiguration: If the config is invalid.
    """
    return cls()

  def __init__(self):
    """Initializer.
    """

  def generate_import_record(self, filename, bulkload_state):
    """Generator, yields dicts for nodes found as described in the options.

    Args:
      filename: valid and well formed property file
      bulkload_state: Passed bulkload_state.

    Yields:
      Neutral dict, one per row returned by the sql query
    """

    self.bulkload_state = bulkload_state
    p = properties.Properties()
    p.load(open(filename))
    for k, v in p.iteritems():
      yield {'property_name':k, 'property_value':v}