import requests
import base64
from urllib3.exceptions import InsecureRequestWarning

def bas64encode(st):
  st_bytes = st.encode('ascii')
  base64_bytes = base64.b64encode(st_bytes)
  base64_st = base64_bytes.decode('ascii')
  return(base64_st)

def token_required(f):
    def wrapper(self, *args, **kwargs):
        self.token = self.access_token()
        return f(self, *args, **kwargs)
    return wrapper

class vsd_api_service:
    def __init__(self, url, username, password, enterprise):
        self.url = url
        self.username = username
        self.password = password
        self.enterprise = enterprise


    def access_token(self):
        auth_url = f"{self.url}/nuage/api/v5_0/me"
        headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(self.username+":"+self.password))}
        res = requests.get(auth_url, headers=headers,  verify=False)
        token=res.json()[0]["APIKey"]
        return(token)


    @token_required
    def list_enterprises(self):
        headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(self.username+":"+self.token))}
        res=requests.get(self.url+"/nuage/api/v5_0/enterprises", headers=headers,  verify=False)
        enterprises=[]
        for item in res.json():
          enterprises.append(item['name'])
        return enterprises

