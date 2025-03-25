from dataclasses import dataclass
from typing import List

@dataclass
class MetaObjectField:
    key         :str
    value       :str
    type        :str

@dataclass
class MetaObjectDealer:
    id          :str
    handle      :str
    type        :str
    updatedAt   :str

    md5                         : MetaObjectField
    sth_id                      : MetaObjectField
    account_name                : MetaObjectField
    activity_status             : MetaObjectField
    ecommerce_role              : MetaObjectField
    tech_external_id            : MetaObjectField
    mailing_zip_postal_code     : MetaObjectField
    mobile_phone                : MetaObjectField
    email                       : MetaObjectField


###################### GRAPH QL

@dataclass
class QueryStatus:
    restoreRate                 :int
    currentlyAvailable          :int
    maximumAvailable            :int

@dataclass
class QueryCost:
    requestedQueryCost          :int
    actualQueryCost             :int
    throttleStatus              :QueryStatus

@dataclass
class Extensions:
    cost                        :QueryCost

@dataclass
class QueryPageInfo:
    hasNextPage                 :bool
    endCursor                   :str

@dataclass
class QueryNodes:
    nodes                       : List[MetaObjectDealer]
    pageInfo                    : QueryPageInfo

@dataclass
class MetaObject:
    metaobjects                 : QueryNodes

@dataclass
class QueryData:
    data                        : MetaObject
    extensions                  : Extensions

