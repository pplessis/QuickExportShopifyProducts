from dataclasses import dataclass

@dataclass
class ShopifyCustomer:
    """Class represent a Shopify Customer (POC: @dataclass)
    """
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    pass