# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 12:31
# @Author  : chenhaibing01
# @File    : jsonFileUtils.py
# @Software: PyCharm

import os, json

class JsonFile:
    """
    读写json文件相关的工具
    """

    def __init__(self):
        """
        初始化
        """
        self.file_path = './messageFile/'


    def creat_file(self):
        """
        创建文件
        :return:
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w+') as f:
                pass

    def read(self, file_name):
        """
        读文件
        :return: Python对象
        """

        # self.file_path = self.file_path + file_name
        # if not os.path.exists(self.file_path):
        #     with open(self.file_path, 'w+') as f:
        #         return []
        try:
            with open(self.file_path + file_name, 'r', encoding='utf-8') as f:
                content = json.load(f)
            return content
        except Exception as e:
            return []

    def write(self, file_name, data):
        """
        写文件
        :return:
        """
        # self.file_path = self.file_path + file_name
        with open(self.file_path + file_name, 'w+', encoding='utf-8') as f:
            json.dump(data, f)


if __name__ == "__main__":
    JF = JsonFile()
    file_name = "openai_7.json"
    # JF.write(file_name, {"user": "sdadasdas"})
    question_record = JF.read(file_name)
    print(question_record)
