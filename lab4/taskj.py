import json
with open("sample.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<7}")
print("-" * 80)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    descr = item["l1PhysIf"]["attributes"]["descr"] if item["l1PhysIf"]["attributes"]["descr"] else ""  
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<7}")
