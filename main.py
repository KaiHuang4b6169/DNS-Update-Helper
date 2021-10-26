import requests, json

# You'r ip Address
IP_ADDRESS = ""
# You'r domain name
DOMAIN_NAME = ""
# You'r DNS Record Name
HOST_NAME = ""
# You'r Godaddy api key
API_KEY = ""

GODADDY_API_FOMAT = "https://api.godaddy.com/v1/domains/{domain}/records/A/{host}"
GODADDY_HEAD = {"Authorization": "sso-key {apiKey}", 
                "Content-Type": "application/json"}
GODADDY_DATA = {"data": ""}

def getRequestApi(domainName: str, hostName: str):
    return GODADDY_API_FOMAT.format(domain = domainName, host = hostName)

def getRequestHead(apiKey: str):
    GODADDY_HEAD["Authorization"] = GODADDY_HEAD["Authorization"].format(apiKey = apiKey)
    return GODADDY_HEAD

def getRequestData(ipAddress: str):
    GODADDY_DATA["data"] = IP_ADDRESS
    return json.dumps([GODADDY_DATA])


def updateDNSRecord(domainName: str, hostName: str, apiKey: str, ipAddress: str):
    requestApi = getRequestApi(domainName = domainName, hostName = hostName)
    requestHeader = getRequestHead(apiKey)
    requestData = getRequestData(ipAddress)
    try:
        response = requests.put(requestApi, headers = requestHeader, data = requestData)
    except Exception as e:
        print(e)

    return response

if __name__ == '__main__':
    response = updateDNSRecord(domainName = DOMAIN_NAME, hostName = HOST_NAME, apiKey = API_KEY, ipAddress = IP_ADDRESS)
    print(response)