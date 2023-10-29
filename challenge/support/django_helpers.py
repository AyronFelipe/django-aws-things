import os


def eval_env_as_boolean(varname, standard_value):
    return str(os.getenv(varname, standard_value)).lower() in ("true", "1", "t", "y")
