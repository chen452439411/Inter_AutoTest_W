import os
import yaml


class YamlReader(object):
    """
    封装Yaml方法
    """

    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None
        self._data_all = None


    def data(self):
        """
        读取单个配置文件的数据
        :return: 配置文件的数据 type：dict or list
        """
        if self._data == None:
            with open(self.yamlf,'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data


    def data_all(self):
        """
        读取多个配置文件的数据
        :return: 配置文件的数据 type ：list
        """
        if self.data_all == None:
            with open(self.yamlf,'rb') as f:
                self.data_all = yaml.safe_load_all(f)
        return self.data_all