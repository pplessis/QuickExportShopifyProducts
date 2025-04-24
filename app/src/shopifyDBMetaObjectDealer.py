from libs.shopifyDB import ShopifyID, SH_ENTITY
from hashlib import md5

class ShopifyDBMetaObjectDealer (ShopifyID):
    def __init__(self) -> None:
        super().__init__()
        self.firstName              = ''
        self.lastName               = ''
        self.email                  = ''
        self.techExternalId         = ''
        self.mobilePhone            = ''
        self.optInNewsletter_1      = ''
        self.ecommerceRole          = ''
        self.mailingStreet          = ''
        self.mailingCity            = ''
        self.mailingStateProvince   = ''
        self.mailingCountry         = ''
        self.mailingZipPostalCode =''
        self.salutation             =''
        self.withMyStanAccess       =''
        self.activityStatus         = ''
        self.geoLng                 = '0.00'
        self.geoLat                 = '0.00'
        self.digitalRank            =''
        self.salesSegment           =''
        self.dealerSellingArea      =''
        self.accountId              =''

    # ####################### ##
    @classmethod
    def from_entity(cls, Entity:SH_ENTITY):
        objReturn = cls()
        objReturn.entity          = Entity

        return objReturn

    # ####################### ##
    @property
    def md5(self)->str:
            returnValue = f'{self.firstName}+{self.lastName}+{self.sthId}+{self.email}+{self.techExternalId}+{self.mobilePhone}+{self.optInNewsletter_1}+{self.ecommerceRole}+{self.mailingStreet}+{self.mailingCity}+{self.mailingStateProvince}+{self.mailingCountry}+{self.mailingZipPostalCode }+{self.salutation}+{self.withMyStanAccess}+{self.activityStatus}+{self.geoLng}+{self.geoLat}+{self.digitalRank}+{self.salesSegment}+{self.dealerSellingArea}+{self.accountId}'
            returnValue =  md5( returnValue.encode() ).hexdigest()

            return  returnValue