from .libs  import Print 
from .libs  import shopifyConnect as SC
from .libs  import shopifyInfo as SI

@staticmethod
def Main() -> None:
    Print.h2("Hello World !")

    country = SI.CONNECTION_COUNTRY.FRA
    env = SI.CONNECTION_ENV.TEST
    
    infosConnect = SI.CONNECTION_INFO[ str(country) ][ str(env) ]

    # Create connection
    siteConnect = SC.ShopifyConnect (
            infosConnect['SHOPIFY_SHOP_NAME']
        ,   infosConnect['SHOPIFY_ADMIN_TOKEN']
    )
    
    Print.Environnement  (env , country)