from .libs  import Print
from .libs  import shopifyConnect as SC
from .libs  import shopifyGraphQL as SG
from .libs  import shopifyInfo as SI


@staticmethod
def Main(Folders:dict) -> None:
    Print.h2("Hello World !")

    country = SI.CONNECTION_COUNTRY.ESP
    env = SI.CONNECTION_ENV.TEST
    
    infosConnect = SI.CONNECTION_INFO[ str(country) ][ str(env) ]

    
    Print.Environnement  (env , country)
    
    #Init Folders 
    SG.ShopifyGraphQL.DEFAULT_FOLDER_GPL    = Folders   ['query']
    SG.ShopifyGraphQL.DEFAULT_FOLDER_JSON   = Folders   ['tmp']

    # Create Shopify GraphQL engine
    shopifyConnect = SG.ShopifyGraphQL(  infosConnect['SHOPIFY_SHOP_NAME']
                      , infosConnect['SHOPIFY_ADMIN_TOKEN'])
    # Load GraphQL file
    graphQL_getProducts = shopifyConnect.loadGraphQLFile('QueryProducts.graphql' )
    
    # Load Data
    rowData = shopifyConnect.executeQueryWithPages( graphQL_getProducts.query, graphQL_getProducts.variable , graphQL_getProducts.objectName )
    
    print (rowData)