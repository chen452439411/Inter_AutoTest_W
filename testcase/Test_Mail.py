from utils.RequestsUtil import Requests
from config.Conf import ConfigYaml
import requests
def login():
    url = ConfigYaml().get_conf_url_test() + '/authorizations/'
    data = {"username":"python","password":"12345678"}
    a = Requests()
    r = a.post(url,json=data)
    print(r)



if __name__ == '__main__':
    login()