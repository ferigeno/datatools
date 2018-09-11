import sys
import os
from argparse import ArgumentParser
from collections import OrderedDict
import data_funcs as dfunc
import defaults as dflt


def var_set(var_list):
    cmd_line = __arg_parser__(dflt.ArgLists.full_list, var_list)
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
                exec("var_dict['"+var+"'] = dflt.Default."+var)
            except Exception:
                print("Unable to set variable "+var+" with any"+
                      " accepted methods.\n"+
                      "Please either:\n"+
                      "  Provide it on the command line\n"+
                      "  Set it as a system env variable\n"+
                      "  Provide it in a config file\n")
                sys.exit()
                
    return(var_dict)
    
def __arg_parser__(dictonary, parser_list):
    parser = ArgumentParser()
    
    parser.add_argument(
        "-c",
        "--config",
        help="The user defined config file for quick import"
    )
    
    for val in parser_list:
        cmd=(
            "parser.add_argument("+
            dictonary[val]+
            ")"
        )
        exec(cmd)
        
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
