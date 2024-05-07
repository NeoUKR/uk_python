import argparse
from пітон.ядро.фіксовані_значення import *
from пітон.ядро.типи_данних import *

class РозбірАргументів(argparse.ArgumentParser):
    """Object for parsing command line strings into Python objects.

    Аргументи ключслова:
        - прог -- The name of the program (default:
            ``os.path.basename(sys.argv[0])``)
        - використання -- A usage message (default: auto-generated from arguments)
        - опис -- A description of what the program does
        - епілог -- Text following the argument descriptions
        - батьки -- Parsers whose arguments should be copied into this one
        - клас_форматувальника -- HelpFormatter class for printing help messages
        - prefix_chars -- Characters that prefix optional arguments
        - fromfile_prefix_chars -- Characters that prefix files containing
            additional arguments
        - argument_default -- The default value for all arguments
        - conflict_handler -- String indicating how to handle conflicts
        - add_help -- Add a -h/-help option
        - allow_abbrev -- Allow long options to be abbreviated unambiguously
        - exit_on_error -- Determines whether or not ArgumentParser exits with
            error info when an error occurs
    """

    def __init__(свій,
                 прог=Жоден,
                 використання=Жоден,
                 опис=Жоден,
                 епілог=Жоден,
                 батьки=[],
                 клас_форматувальника=argparse.HelpFormatter,
                 prefix_chars='-',
                 fromfile_prefix_chars=Жоден,
                 argument_default=Жоден,
                 conflict_handler='error',
                 add_help=Хиба,
                 allow_abbrev=Хиба,
                 exit_on_error=Істина):
        super().__init__(prog=прог,
                        usage=використання,
                        description=опис,
                        epilog=епілог,
                        parents=батьки,
                        formatter_class=клас_форматувальника,
                        prefix_chars=prefix_chars,
                        fromfile_prefix_chars=fromfile_prefix_chars,
                        argument_default=argument_default,
                        conflict_handler=conflict_handler,
                        add_help=add_help,
                        allow_abbrev=allow_abbrev,
                        exit_on_error=exit_on_error)

    # =======================
    # Дія додавання аргументу
    # =======================
    def додати_аргумент(свій, *арг, **ксарг):
        if "замовчання" in ксарг:
            ксарг["default"] = ксарг["замовчання"]
            del ксарг["замовчання"]
        if "тип" in ксарг:
            ксарг["type"] = ксарг["тип"]
            del ксарг["тип"]

        свій.add_argument(*арг, **ксарг)

    def розібрати_аргументи(свій, аргументи=Жоден, простір_імен=Жоден):
        return свій.parse_args(args=аргументи, namespace=простір_імен)
