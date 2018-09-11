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

class Default:
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
    
class ArgLists:
    full_list = {
        "password":'"-pwd", "--password", help="Supplies password. PASSWORD IS NOT PROTECTED THIS WAY. It is better to set an env_variable or have and external config file"',
        "package_use":'"-pu", "--package_use", help="Determines whether pyodbc or psycopg2 is used"',
        "driver":'"-dr", "--driver", help="For pyodbc, the name of the driver to use"',
        "host":'"-dh","--host", help="The hostname or ip for the database server"',
        "port":'"-p", "--port", help="The port for the database server"',
        "database":'"-d", "--database", help="The database name the user is connection to"',
        "username":'"-u", "--username", help="The database username the user is connecting with"',
        "prompt_password":'"-pp", "--prompt_password", help="Enables or disables prompting password, even if one is provided", action="store_true"',
        "ssl_mode":'"-ssl", "--ssl_mode", help="Specifies which SSL mode is used when creating database connection"',
        "terminator":'"-t", "--terminator", help="Defines a query terminator"',
        "header":'"-hdr", "--header", help="Enables or disables providing a header on results", action="store_true"',
        "delimiter":'"-dl", "--delimiter", help="Specifies the delimiter used on outputted data"',
        "clean_print":'"-cp", "--clean_print", help="Enables or disables cleanprint", action="store_true"',
        "isolation_level":'"-il", "--isolation_level", help="Sets the isolation level used in the database connection"',
        "auto_commit":'"-ac", "--auto_commit", help="Enables or disables automatic commiting after queries/transactions", action="store_true"',
        "commit_count":'"-cc", "--commit_count", help="Sets the number of rows attempted to be loaded before a commit", type=int',
        "thread_limit":'"-tl", "--thread_limit", help="Sets the number of threads used during a dataload. Default is all", type=int',
        "file":'"-f", "--file", help="A query file or data file being used"',
        "error_file":'"-ef", "--error_file", help="The file where errors are stored"',
        "query":'"-q", "--query", help="A one time query ran"'
    }
    
