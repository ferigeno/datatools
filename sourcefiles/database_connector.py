import sys
import getpass
import pyodbc

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
    
    if 'prompt_password' in conn_dict:
        if conn_dict['prompt_password'] == True:
            conn_dict['password'] = getpass.getpass(prompt='Database Password: ')
    
    for val in [['host','SERVER'],
                ['port','PORT'],
                ['database','DATABASE'],
                ['username','UID'],
                ['password','PWD'],
                ['ssl_mode','SSLMODE']]:
        if val[0] in conn_dict:
            cmd = (cmd+
                   val[1]+
                   "="+
                   str(conn_dict[val[0]])+
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
