import os
from utils.YamlUtil import YamlReader

current = os.path.abspath(__file__)
BASE_FIR = os.path.dirname(os.path.dirname(current))
_conf_path = BASE_FIR + os.sep + 'config'
_conf_file = _conf_path + os.sep + 'conf.yml'



def get_config_path():
    """
    获取config文件夹path
    :return: config文件夹path  type: str
    """
    return _conf_path


def get_conf_file():
    """
    获取yml配置文件path
    :return: 配置文件path  type: str
    """
    return _conf_file

class ConfigYaml(object):

    def __init__(self):
        self.config = self.get_data()

    def get_data(self):
        """
        获取数据 data or data_all
        :return: 数据结果 type: list or dict
        """
        try:
            data = YamlReader(get_conf_file()).data()
        except:
            data = YamlReader(get_conf_file()).data_all()
        return data

    def get_conf_url_test(self):
        """
        读取配置文件中test的url
        :return: str
        """
        return self.config['BASE']['test']['url']

if __name__ == '__main__':
    pass