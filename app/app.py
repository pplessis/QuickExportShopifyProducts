import json
from .libs  import Print
from .libs  import shopifyConnect as SC
from .libs  import shopifyGraphQL as SG
from .libs  import shopifyInfo as SI

from .libs  import dataClasses_shopifyProduct   as DSP
from .libs  import dataClasses_shopifyDealer    as DSMO

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
    jsonFile = shopifyConnect.backupResult( rowData, 'PRODUCTS')
    
    # Convert rowData to object instances
    products:list[DSP.Product] = [DSP.Product(**p) for p in rowData]

    for item in products:
        print (item.createdAt)


@staticmethod
def ExtractMetaObject(Folders:dict) -> None:
    country = SI.CONNECTION_COUNTRY.FRA
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
    graphQL_getProducts = shopifyConnect.loadGraphQLFile('QueryMetaObjectDealerAll.graphql' )

    # Load Data
    rowData = shopifyConnect.executeQueryWithPages(
                                                    graphQL_getProducts.query, graphQL_getProducts.variable
                                                    , graphQL_getProducts.objectName
                                                    , PageLimit=3 )

    dealers:list[ DSMO.MetaObjectDealer ] = [DSMO.MetaObjectDealer(**p) for p in rowData]


    return None