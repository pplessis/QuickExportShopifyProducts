import json
import urllib3
from enum import Enum
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
urllib3.disable_warnings (urllib3.exceptions.InsecureRequestWarning)

#from .shopifyDB import ShopifyInfoId, ShopifyID
from .shopifyConnect import ShopifyConnect as SC
from .utils import Io, Print, Tools

class SH_GRAPHQL_URL (str, Enum):
   default         =  'https://{0}.myshopify.com/admin/api/{1}/graphql.json'

###
class GraphQlQuery:
    """ The code defines a class `GraphQlQuery` that represents a GraphQL query and contains the following attributes:
        - `query`: the actual GraphQL query itself.
        - `variable`: the variables used in the GraphQL query.
        - `graphQlName`: the name of the GraphQL operation (e.g., "mutation" or "query").
        - `objectName`: the name of the object concerned by the GraphQL query.
    """
    def __init__(self) -> None:
        self.query = ''
        self.variable = ''
        self.graphQlName = ''
        self.objectName = ''
        pass

    def variableApplyTemplate (self, keysValue:dict) -> bool:
        """The method variableApplyTemplate(keysValue:dict) -> bool allows applying values to keys specified in a dictionary (keysValue) to the variable of the GraphQL query.
        Args:
            keysValue (dict): _description_
        Returns:
            bool: _description_
        """
        returnValue = False

        # Example "keysValue"
        # { "%LIST%"  : VALUE  }

        self.variable = Tools.replaceValueInHTMLTemplate(self.variable , keysValue)

        return returnValue


# #######################

class ShopifyGraphQL (SC) :
    DEFAULT_FOLDER_GPL = 'graphQL'
    DEFAULT_FOLDER_JSON = 'data/out/json'

    def __init__(self, ShopName:str, AdminToken:str) -> None:
        super().__init__(ShopName, AdminToken)

        self.filesFolder = self.DEFAULT_FOLDER_GPL

# #######################

    def __loadGraphQLFile (self, GraphQLFilename:str) -> GraphQlQuery:
        returnValue = GraphQlQuery()

        currentVars     = None
        queryTmp        = ''
        variablesTmp    = ''
        objectName      = ''

        # Open GraphQL File
        queryLines = Io.openTxtFile (self.filesFolder
                                     , GraphQLFilename)

        # Split GraphQL File
        for line in queryLines:
            if ( "\"\"\" QUERY " in line ):
                currentVars = 'query'
                continue
            if ("\"\"\" VARIABLES" in line):
                currentVars = 'variables'
                continue
            if ( "\"\"\" SHOPIFY-OBJECT" in line ):
                currentVars = 'object-name'
                continue

            if ("\"\"\" #" in line):
                continue
            if ("\"\"\"#" in line):
                continue

            if (len (line) == 0):
                continue

            if (currentVars == 'query'):
                queryTmp += line + Io.NEWLINE

            if (currentVars == 'variables'):
                variablesTmp += line

            if (currentVars == 'object-name'):
                objectName = line.strip()

        #print(queryTmp)
        #print(variablesTmp)

        returnValue.query       = queryTmp
        returnValue.variable    = variablesTmp
        returnValue.objectName  = objectName


        return returnValue

# #######################
    @property
    def getUrlGraphQL(self):
        return  SH_GRAPHQL_URL.default.format (self.shopName, self.apiVersion)

# #######################
    def loadGraphQLFile (self, GraphQLFilename:str) -> GraphQlQuery:
        currentGraphQL = self.__loadGraphQLFile(GraphQLFilename)
        return currentGraphQL

    def queryFromFileAndExecute (self, GraphQLFilename:str, IntegrateCursors:bool=False) -> list:
        currentGraphQL = self.__loadGraphQLFile(GraphQLFilename)
        return self.executeQuery(currentGraphQL.query, currentGraphQL.variable, ObjectName=currentGraphQL.objectName)

    def executeQuery (self, Query:str, Variables:str, ObjectName:str='') -> list:
        returnValue = list()
        timeoutAllow =  SC.HTTP_TIMEOUT

        try :
            #Create GraphQL object
            query = gql (Query)

            variables = None
            if (len(Variables)>0):
                variables = json.loads(Variables)

            # Create connection
            transport = RequestsHTTPTransport( url= self.getUrlGraphQL
                                              ,headers= self.getRequestHeader
                                              ,verify= self.requestCertificate)

            client = Client(  transport=transport
                            , fetch_schema_from_transport=True
                            , execute_timeout=timeoutAllow)

            # Execute FirstQuery
            response = client.execute( query, variable_values = variables )

            if (len(ObjectName) > 0 ):
                returnValue.append( response [ObjectName] )
            else:
                returnValue.append( response )

        except gql.transport.exceptions.TransportQueryError as eGql:
            Print.error ( "Error: " + eGql.errors + ' - ' + str(eGql) )

        except urllib3.exceptions.ProtocolError as eUrl:
            Print.error ( "Error: " + str(eUrl) )

        except Exception as e:
            Print.error ( "Error: " + str(e) )

        return returnValue

    def executeQueryWithPages (self, Query:str, Variables:str, ObjectName:str, PageLimit:int=100) -> list:
        """Function to Retrieve a large data volume based in "cursor" variable in query.

        Args:
            Query (str): _description_
            Variables (str): _description_
            ObjectName (str, optional): _description_. Defaults to ''.

        Returns:
            list: _description_
        """
        returnValue = list()
        existNextPage = False
        nextPageToken = None
        limit_pages = PageLimit

        #Quality control
        ## Check "cursor" exist in variable
        if ( not("cursor" in Variables) ):
            raise ValueError('Variable need to contain a "cursor" to manage Pages' )
        if (not ("pageInfo" in Query)):
            raise ValueError('Query need to contain a "pageInfo" to manage Pages' )

        ## Execute a first execution
        ValuesExecution = { "%CURSOR%" : "null" }
        VariablesFistEx =  Tools.replaceValueInHTMLTemplate(Variables, ValuesExecution)

        firstResult = self.executeQuery(Query, VariablesFistEx, ObjectName)
        if (len(firstResult) == 1):
            ## Save Data
            for item in firstResult[0]['nodes']:
                    returnValue.append(item)
            ## Get Next page
            existNextPage = firstResult[0]['pageInfo']['hasNextPage']
            nextPageToken = firstResult[0]['pageInfo']['endCursor']

        ## create a loop until nextPage exist
        index = 1
        print ( '[', end='', flush=True )
        while ( existNextPage ) :
            print ( '#', end='' , flush=True )
            ValuesExecution = { "%CURSOR%" : '"{0}"'.format(nextPageToken) }
            VariablesFistEx =  Tools.replaceValueInHTMLTemplate(Variables, ValuesExecution)
            dataJson = self.executeQuery(Query, VariablesFistEx, ObjectName)

            if ( len(dataJson) == 1 ):
                ## Save Data
                for item in dataJson[0]['nodes']:
                    returnValue.append(item)
                ## Get Next page
                existNextPage = dataJson[0]['pageInfo']['hasNextPage']
                nextPageToken = dataJson[0]['pageInfo']['endCursor']
            else:
                existNextPage = False

            index += 1
            if (index > limit_pages ):
                Print.error( f'Page limit ({limit_pages})' )
                existNextPage = False

        print ( ']', flush=True, end="\n")
        return returnValue

    # #######################

    @staticmethod
    def backupResult(ArrayData, ObjectName) -> str:
        jsonText  =  ShopifyGraphQL.getJson(ArrayData)
        jsonFolder = ShopifyGraphQL.DEFAULT_FOLDER_JSON
        now = datetime.now()
        nowStr = now.strftime('%Y%m%d%H%M%S')
        result = ''

        filename = '{0}_{1}.json'.format( nowStr , ObjectName )
        result = Io.saveTxtFile(jsonFolder , filename, jsonText)

        return result
    
    @staticmethod
    def getJson(ArrayData) -> str:
        jsonText  = json.dumps(ArrayData, default = lambda o: o.__dict__, sort_keys=False)
        return jsonText

