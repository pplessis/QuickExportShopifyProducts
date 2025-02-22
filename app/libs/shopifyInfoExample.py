from enum import Enum, StrEnum

class CONNECTION_COUNTRY (StrEnum):
    ESP = 'ESP'

class CONNECTION_ENV (StrEnum):
    TEST = 'TEST'
    PROD = 'PROD'

# Centralized API version
SHOPIFY_API_VERSION = '2025-01'

# ###########################
CONNECTION_INFO = {
    #SPAIN
        "ESP"  : {
    "TEST": {
                "SHOPIFY_SHOP_NAME"   :  'xxxxxxxxx'
                ,"SHOPIFY_ADMIN_TOKEN" :  'shpat_xxxxxxxxxx'
            }
    ,
    "PROD": {
                "SHOPIFY_SHOP_NAME"   :  'wwwwwww'
                ,"SHOPIFY_ADMIN_TOKEN" :  'shpat_wwwwwwww'
            }
    }

   }
# ################################
