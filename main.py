import requests as r
import xmltodict
import sys


def test_domain(domain):
    url = f"https://login.microsoftonline.com/getuserrealm.srf?login=x@{domain}&xml=1"
    response = r.get(url)
    data = xmltodict.parse(response.text)
    if data["RealmInfo"]["NameSpaceType"] == "Managed":
        return True
    else:
        return False

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target domain")
    raise SystemExit(2)

if test_domain(sys.argv[1]):
    print("Target uses 365 Cloud")
    print("\nSee https://attack.mitre.org/matrices/enterprise/cloud/office365/ for attacks on this domain")
else:
    print("Target doesn't use 365 Cloud")
