# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 11:06
# @Author  : chenhaibing01
# @File    : mulconversation.py
# @Software: PyCharm


import openai
from utils.jsonFileUtils import JsonFile
JF = JsonFile()

openai.api_key = "XXXXXX"

class ChatGPT:
    """
    可进行多轮对话
    """
    def __init__(self):
        """初始化对话列表，可以加入一个key为system的字典，有助于形成更加个性化的回答"""
        self.conversation_list = []
        self.question_name = "openai_"

    def show_conversation(self, msg_list):
        """
        打印对话
        :param msg_list:
        :return:
        """
        for msg in msg_list:
            if msg['role'] == 'user':
                print(f"\U0001f600: {msg['content']}\n")  #\U0001f600 微笑的表情
            else:
                print(f"\U0001f4BB: {msg['content']}\n")

    def ask(self, question_id = 0, prompt = ""):
        """

        :param isNewQuestion: 是否是新问题
        :param question_id: 问题id
        :param prompt: 提示词
        :return:
        """
        file_name = self.question_name + str(question_id) + ".json"

        question_record = JF.read(file_name)

        if question_record:
            self.conversation_list = question_record

        self.conversation_list.append({"role": "user", "content": prompt})

        answer = self.get_answer()
        print(f"当前问题的答案：{answer}")

        self.conversation_list.append({"role": "assistant", "content": answer})

        # self.show_conversation(self.conversation_list)#展示对话列表


        JF.write(file_name, self.conversation_list)
        return self.conversation_list



    def get_answer(self):
        """获取答案"""

        response = openai.ChatCompletion.create(model = "gpt-3.5-turbo-0301", messages = self.conversation_list)
        answer = response.choices[0].message["content"]

        return answer



if __name__ == "__main__":
    c2 = ChatGPT()
    c2.ask(3, "我想买个加湿器")   #（问题id, 问题）如果是连续的问题，就用相同的问题id
    # c2.ask(3,"它和谷歌有什么区别")
    # c2.ask(3, "你觉得谁更好")

