from os        import path as PA
from app       import app

def title() -> str:
    title ="""
███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗███████╗    ███████╗██╗  ██╗ ██████╗ ██████╗ ██╗███████╗██╗   ██╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██║  ██║██╔═══██╗██╔══██╗██║██╔════╝╚██╗ ██╔╝
█████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ███████╗    ███████╗███████║██║   ██║██████╔╝██║█████╗   ╚████╔╝ 
██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ╚════██║    ╚════██║██╔══██║██║   ██║██╔═══╝ ██║██╔══╝    ╚██╔╝  
███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ███████║    ███████║██║  ██║╚██████╔╝██║     ██║██║        ██║   
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   
    """

    return title

# Grabs the folder where the script runs.
BASEDIR             = PA.abspath(PA.dirname(__file__))
GRAPH_QL_FOLDER     = BASEDIR + '/graphQL'
LOGS_FOLDER         = BASEDIR + '/logs'
TMP_FOLDER          = BASEDIR + '/tmp'

APP_FOLDERS = {       'base': BASEDIR
                    , 'query': GRAPH_QL_FOLDER
                    , 'logs': LOGS_FOLDER
                    , 'tmp': TMP_FOLDER
          }

# Grabs Launcher application


# Launch Main Program
#app = main.Main(APP_FOLDERS)
print ( title() )
app = app.ExtractMetaObject(APP_FOLDERS)