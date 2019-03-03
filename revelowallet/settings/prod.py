from os.path import join, dirname, exists
import environ

from .local import *

env = environ.Env()
env_file = join(dirname(__file__), '.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))