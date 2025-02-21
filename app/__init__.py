from os import path as PA

# Grabs the folder where the script runs.
basedir = PA.abspath(PA.dirname(__file__))

from app        import main
