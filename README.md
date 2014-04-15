Bulkloader Connectors
=====================

This purpose of this project is to aggregate non official bulkloader connectors.

Oracle Connector
----------------

Import data from Oracle RDBMS.
For further details check this post:

[Importing data from Oracle to Google App Engine Datastore with a custom bulkloader connector](http://fabiouechi.blogspot.com/2011/12/bulk-loading-data-from-oracle-to-google.html)

Property Connector
------------------

Import Java Property Files into Datastore.
Useful for setting up Java Webapps with external configuration.
Check also the [gaemeleon](https://github.com/fabito/gaemeleon) project. It provides a set of utilities classes to ease this task.

```sh
appcfg.py upload_data --config_file=bulkloader_properties.yaml --url=http://localhost:8080/_ah/remote_api --kind=Configuration --filename=test2.properties --email=f@f.com
```