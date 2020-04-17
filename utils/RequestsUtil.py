import requests

class Requests(object):
    """
    封装requests方法
    """

    def requests_api(self,url,method,json=None,data = None,headers = None,cookies = None):
        """
        request api
        :param url: str
        :param method:
        :param json:
        :param data:
        :param headers:
        :param cookies:
        :return: {'code':'code','body':'body'} type:dict
        """
        if method =='get':
            r = requests.get(url,json=json,data = data,headers = headers,cookies = cookies)
        elif method =='post':
            r = requests.post(url,json=json, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception ('method参数错误')
        code = r.status_code
        try:
            body = r.json()
        except:
            body = r.text
        res = dict()
        res['code'] = code
        res['body'] = body
        return res

    def get(self,url,**kwargs):
        """
        get请求封装方法
        :param url: url地址 type：str
        :param kwargs:
        :return: {'code':'code','body':'body'} type:dict
        """
        return self.requests_api(url,method='get',**kwargs)


    def post(self,url,**kwargs):
        """
        Post请求封装方法
        :param url: url地址 type：str
        :param kwargs:
        :return: {'code':'code','body':'body'} type:dict
        """
        return self.requests_api(url,method='post',**kwargs)