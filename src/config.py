import os

"""Expose any configuration from env vars as variables here."""

# Variables for env var names. naming convention: ENV_VAR_<YOUR ENV VAR NAME>
ENV_VAR_SOME_ENVVAR1 = "SOME_ENVVAR1"
ENV_VAR_DB_CONN = "DB_CONN"

SOME_ENVVAR1 = os.getenv(key=ENV_VAR_SOME_ENVVAR1, default='bla default')
DB_CONN = os.getenv(key=ENV_VAR_DB_CONN, default=None)