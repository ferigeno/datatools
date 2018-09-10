from argparse import ArgumentParser
from collections import OrderedDict
import data_funcs as DFUNC
import defaults as DF
import sys
import os

def var_set(var_list):
    cmd_line = __arg_parser__(var_list)
    if cmd_line.config is not None:
        config_data = __config_load__(cmd_line.config)
    else:
        config_data = OrderedDict()

    var_dict = OrderedDict()
    for var in var_list:
        #Command Line Trumps All
        if getattr(cmd_line,var) is not None:
            var_dict[var] = getattr(cmd_line,var)
        #Next Level is any passed in config files
        elif var in config_data:
            var_dict[var] = config_data[var]
        elif var in os.environ:
            var_dict[var] = os.environ[var]
        elif var.upper() in os.environ:
            var_dict[var] = os.environ[var.upper()]
        elif var.lower() in os.environ:
            var_dict[var] = os.environ[var.lower()]
        else:
            try:
                exec("var_dict['"+var+"'] = DF.default."+var)
            except Exception:
                print("Unable to set variable "+var+" with any"+
                      " accepted methods.\n"+
                      "Please either:\n"+
                      "  Provide it on the command line\n"+
                      "  Set it as a system env variable\n"+
                      "  Provide it in a config file\n")
                sys.exit()
                
    return(var_dict)
    
def __arg_parser__(parser_shortlist):
    parser = ArgumentParser()
    
    parser.add_argument(
        "-c",
        "--config",
        help="The user defined config file for quick import")
    
    if 'package_use' in parser_shortlist:
        parser.add_argument(
            "-pu",
            "--package_use",
            help="Determines whether pyodbc or psycopg2 is used",)
        
    if 'driver' in parser_shortlist:
        parser.add_argument(
            "-dr",
            "--driver",
            help="For pyodbc, the name of the driver to use")
        
    if 'host' in parser_shortlist:
        parser.add_argument(
            "-dh",
            "--host",
            help="The hostname or ip for the database server")
        
    if 'port' in parser_shortlist:
        parser.add_argument(
            "-p",
            "--port",
            help="The port for the database server",
            type=int)
        
    if 'database' in parser_shortlist:
        parser.add_argument(
            "-d",
            "--database",
            help="The database name the user is connection to")
        
    if 'username' in parser_shortlist:
        parser.add_argument(
            "-u",
            "--username",
            help="The database username the user is connecting with")
        
    if 'prompt_password' in parser_shortlist:
        parser.add_argument(
            "-pp",
            "--prompt_password",
            help="Enables or disables prompting password, even if one is provided",
            action="store_true")
        
    if 'ssl_mode' in parser_shortlist:
        parser.add_argument(
            "-ssl",
            "--ssl_mode",
            help="Specifies which SSL mode is used when creating database connection")

    if 'terminator' in parser_shortlist:
        parser.add_argument(
            "-t",
            "--terminator",
            help="Defines a query terminator")
        
    if 'header' in parser_shortlist:
        parser.add_argument(
            "-hdr",
            "--header",
            help="Enables or disables providing a header on results",
            action="store_true")
        
    if 'delimiter' in parser_shortlist:
        parser.add_argument(
            "-dlmtr",
            "--delimiter",
            help="Specifies the delimiter used on outputted data")
        
    if 'clean_print' in parser_shortlist:
        parser.add_argument(
            "-cp",
            "--clean_print",
            help="Enables or disables cleanprint",
            action="store_true")
        
    if 'isolation_level' in parser_shortlist:
        parser.add_argument(
            "-il",
            "--isolation_level",
            help="Sets the isolation level used in the database connection")
        
    if 'auto_commit' in parser_shortlist:
        parser.add_argument(
            "-ac",
            "--auto_commit",
            help="Enables or disables automatic commiting after queries/transactions",
            action="store_true")
        
    if 'commit_count' in parser_shortlist:
        parser.add_argument(
            "-cc",
            "--commit_count",
            help="Sets the number of rows attempted to be loaded before a commit",
            type=int)
        
    if 'thread_limit' in parser_shortlist:
        parser.add_argument(
            "-tl",
            "--thread_limit",
            help="Sets the number of threads used during a dataload. Default is all",
            type=int)
        
    if 'file' in parser_shortlist:
        parser.add_argument(
            "-f",
            "--file",
            help="A query file or data file being used")
        
    if 'error_file' in parser_shortlist:
        parser.add_argument(
            "-ef",
            "--error_file",
            help="The file where errors are stored")
        
    if 'query' in parser_shortlist:
        parser.add_argument(
            "-q",
            "--query",
            help="A one time query ran")

    return(parser.parse_args())


def __config_load__(config):
    env = open(config, "r")
    variables = env.readlines()
    env.close()

    var_list = OrderedDict()
    for val in variables:
        if val[0].strip() not in ["#", ""]:
            try:
                if '='.join(val.split("=")[1:]).lower().strip() != '':
                    var_list[str(val.split("=")[0]).lower().strip()] = (
                        DFUNC.typecast(
                            '='.join(val.split("=")[1:]).strip()
                            )
                        )
            except Exception:
                print("Proivded Cofig File Issue:")
                print(
                    "Both a Parameter name and a" +
                    " value must be presented seperated by an =")
                print("ex.\n  driver = PostgreSQL\n")
                sys.exit()
    return(var_list)

if __name__ == '__main__':
    full_list = ['package_use',
                 'driver',
                 'host',
                 'port',
                 'database',
                 'username',
                 'prompt_password',
                 'ssl_mode',
                 'terminator',
                 'header',
                 'delimiter',
                 'clean_print',
                 'isolation_level',
                 'auto_commit',
                 'commit_count',
                 'thread_limit',
                 'file',
                 'error_file',
                 'query'
                 ]
    var_dict = var_set(full_list)
    for var in full_list:
        print(var, var_dict[var])
