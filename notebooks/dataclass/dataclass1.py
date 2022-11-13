from dataclasses import dataclass


@dataclass
class DataPrefix:
    prefix: str = ""
    family: str = ""
    size: str = ""
    description: str = ""
    status: str = ""
    tenant: str = ""
    site: str = ""
    vlan: str = ""
    vrf: str = ""
    role: str = ""

    def __str__(self):
        return f'{self.prefix}/{self.size}'    

pfx1 = DataPrefix(prefix="1.1.1.1",
    family="ipv4",
    size="26",
    description="prod VPC",
    status="container",
    tenant="ERDC",
    site="Chartre 1",
    vlan="ha3503nd1-01",
    vrf="PRD-STD-SMU01-003",
    role="intercos"
)

print(f"pfx1 = {pfx1}")
print(f"pfx1.prefix = {pfx1.prefix}")

