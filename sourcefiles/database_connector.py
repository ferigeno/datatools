import sys
import getpass

package_error = '''
Package listed is not supported.
Supported Packages are:
  pyodbc
  psycopg2
'''

def db_connector(conn_dict):
    package = conn_dict['package_use']
    if package.lower() == 'pyodbc':
        return(__pyodbc_connection__(conn_dict))
    elif package.lower() == 'psycopg2':
        return(__psycopg2_connection__(conn_dict))
    else:
        print(package_error)
        sys.exit()

def __pyodbc_connection__(conn_dict):
    cmd = ("DRIVER={"+
           str(conn_dict['driver'])+
           "};")
    if 'host' in conn_dict:
        cmd = (cmd+
               "SERVER="+
               str(conn_dict['host'])+
               ";")
    if 'port' in conn_dict:
        cmd = (cmd+
               "PORT="+
               str(conn_dict['port'])+
               ";")
    if 'database' in conn_dict:
        cmd = (cmd+
               "DATABASE="+
               str(conn_dict['database'])+
               ";")
    if 'username' in conn_dict:
        cmd = (cmd+
               "UID="+
               str(conn_dict['username'])+
               ";")
    if 'prompt_password' in conn_dict:
        if conn_dict['prompt_password'] == True:
            conn_dict['password'] = getpass.getpass(prompt='Database Password: ')
    if 'password' in conn_dict:
        cmd = (cmd+
               "PWD="+
               str(conn_dict['password'])+
               ";")
    if 'ssl_mode' in conn_dict:
        cmd = (cmd+
               "SSLMODE="+
               str(conn_dict['ssl_mode'])+
               ";")

    if 'auto_commit' in conn_dict:
        conn = pyodbc.connect(cmd, autocommit=conn_dict['auto_commit'])
    else:
        conn = pyodbc.connect(cmd)

#    if 'isolation_level' in conn_dict:
#        cmd = (cmd+
#               "SERVER="+
#               conn_dict['isolation_level']+
#               ";")
    return(conn)

def __psycopg2_connection__(conn_dict):
    print('psycopg2')

if __name__ == '__main__':
    db_connector(None)
