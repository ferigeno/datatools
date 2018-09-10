import os

# Explination of the variables
#  DRIVER = User defined odbc driver (Not required is using psycopg2)
#  HOST = The server address or ip for the connection
#  PORT = What port the server is listening on
#  DATABASE = The name of the database (Postgres typically has one for the user)
#  USER = The user connecting to the database
#  PROMPT_PASSWORD = Forces the user to enter a password, even if one is provided
#  SSL_MODE = Secure Connection: options are
#    disable     = only try a non-SSL connection
#    allow       = try non SSL, if it fails try SSL
#    prefer      = try SSL, if fails try non SSL
#    require     = Only try SSL
#    verify-ca   = Only try SSL and verify cert
#    verify-full = Same as above but verify hostname with cert
#  Terminator = End command to state query is completed
#  Header = Display column names on query
#  Delimiter = Character string that splits column values
#  Clean_print = Space columns due to max value length in column
#  Isolation_level = Standard is 'Read_Commited'
#    Read_commited = Trasaction waits until rowlocks are unlocked. Holds lock on
#                    Affected rows only
#    Read_uncommited = Transactions are not isolated (Typically Read only)
#    Repeatable_read = Same as read_commited except on all rows returned
#    Serializable    = Transaction waits for rowlocks to open by other transactions
#  Auto_Commit = Commit on every query/transaction
#  Commit_Count = How often a commit is made when loading data
#  Thread_Limit = Number of threads allowed. If None all threads will be used

class default(object):
    #Database Connection Defaults
    package_use      = 'pyodbc'
    driver           = 'Postgresql'
    host             = 'localhost'
    port             = 5432
    database         = os.getlogin()
    username         = os.getlogin()
    prompt_password  = True
    ssl_mode         = 'prefer'

    #BOTH SQL_QUERY AND DATA_LOADER
    terminator       = ';'
    header           = True

    #SQL_QUERY
    delimiter        = '|'
    clean_print      = True
    isolation_level  = 'READ_COMMITTED'
    auto_commit      = False

    #DATA_LOADER
    commit_count     = 1
    thread_limit     = None
