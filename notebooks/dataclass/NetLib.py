class IpBaseClass():
    def __init__(self, prefix="", family="", status="", size="",
                 description="", tenant="", site="", vlan="", vrf="",
                 role=""):
        self._dict = {"prefix": prefix,
                     "family": family,
                     "size": size,
                     "description": description,
                     "status": status,
                     "tenant": tenant,
                     "site": site,
                     "vlan": vlan,
                     "vrf": vrf,
                     "role": role,
                     }
    @property
    def dict(self):
        return self._dict

    @dict.setter
    def dict(self, newdict):
        self._dict = dict()
        self._dict = newdict

    def __repr__(self):
        return f"{self.dict['prefix']}"

    def __str__(self):
        return f"{self.dict['prefix']}"

    def __eq__(self, other):
        return f"{self.dict['prefix']}/{self.dict['size']}" == f"{other['prefix']}/{other['size']}"

    def __lt__(self, other):
        return f"{self.dict['prefix']}/{self.dict['size']}" < f"{other['prefix']}/{other['size']}"

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def update(self, item):
        if self.dict.keys() == item.keys():
            self.dict.update(item)
        else:
            raise DictionariesNotSameSize(item)


# Possibly add more methods to "IpBaseClass" for checking and validation of ip/subnet
class IP(IpBaseClass):
    def is_ip(self, func):
        """ Check ip family for ip addresses and networks
        Args:
            item (ip or subnet): ip or subnet
            func (_type_):  ex: ipaddress.IPv4Address or IPv4Address
                            ex: ipaddress.IPv6Address or IPv6Address
                            or an other function from any other appropriate library
        Returns:
            boolean: True if OK
            string: Error description if NOK
        """
        try:
            func(self.dict['prefix'])
            return True
        except Exception as e:
            return e.args
        
    def is_network(self, func):
        """ Check ip family for ip addresses and networks
        Args:
            item (ip or subnet): ip or subnet
            func (_type_):  ex: ipaddress.IPv4Network or IPv4Network
                            ex: ipaddress.IPv4Network or IPv4Network
                            
                            or an other function from any other appropriate library
        Returns:
            boolean: True if OK
            string: Error description if NOK
        """
        try:
            func(f"{self.dict['prefix']}/{self.dict['size']}")
            return True
        except Exception as e:
            return e.args
            

class Prefix(IP):
    def __init__(self, prefix="", family="", status="", size="",
                 description="", tenant="", site="", vlan="", vrf="",
                 role="", children="", available_prefixes=""):
        self._dict = {"prefix": prefix,
                     "family": family,
                     "status": status,
                     "size": size,
                     "description": description,
                     "tenant": tenant,
                     "site": site,
                     "vlan": vlan,
                     "vrf": vrf,
                     "role": role,
                     "children": children,
                     "available_prefixes": available_prefixes                     }


class PrefixToReserve(Prefix):
    """PrefixToReserve Child of Prefix Class with additional attributes
    done : indicates if the prefix is reserved in Netbox
    errors: list of encountered errors along the way
    leaf: for interco vlans

    Args:
        Prefix (_type_): _description_
    """
    def __init__(self, prefix="", family="", status="", size="",
                description="", tenant="", site="", vlan="", vrf="",
                 role="", children="", parent_prefix = "", container="", available_prefixes="", done="", errors=list(), key="",leaf="", tags=list()):
        super().__init__(prefix="", family="", status="", size="",
                 description="", tenant="", site="", vlan="", vrf="",
                 role="", children="", available_prefixes="")
        self._dict = {"prefix": prefix,
                    "family": family,
                    "status": status,
                    "size": size,
                    "description": description,
                    "tenant": tenant,
                    "site": site,
                    "vlan": vlan,
                    "vrf": vrf,
                    "role": role,
                    "children": children,
                    "container": container,                    
                    "parent_prefix": parent_prefix,
                    "available_prefixes": available_prefixes,
                    "done": done,
                    "leaf": leaf,
                    "errors": errors,
                    "key": key,
                    "tags": tags,
                    }