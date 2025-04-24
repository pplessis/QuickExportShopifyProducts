from dataclasses import dataclass
from typing import List

@dataclass
class Metafield:
    __slots__ = 'namespace', 'key', 'id', 'value'
    namespace   : str
    key         : str
    id          : str
    value       : str

@dataclass
class Variant:
    __slots__ = 'id', 'sku', 'displayName', 'price', 'compareAtPrice', 'metafields'
    id          : str
    sku         : str
    displayName : str
    price       : str
    compareAtPrice  : str
    metafields  : List[Metafield]

@dataclass
class Product :
    __slots__ = 'id', 'createdAt', 'updatedAt', 'title', 'tags', 'vendor', 'handle', 'status', 'variants', 'metafields'
    id          : str
    createdAt   : str
    updatedAt   : str
    title       : str
    tags        : List[str]
    vendor      : str
    handle      : str
    status      : str
    variants    : List[Variant]
    metafields  : List[Metafield]

    def __str__(self) -> str:

        return 'id: {0} | title: {1}| handle: {2}'.format(self.id, self.title, self.handle )
        pass

