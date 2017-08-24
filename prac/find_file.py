# coding = utf-8
import os

result_dir = 'C:\\Users\\xuzhen\\PycharmProjects\\QA2017\\prac\\report'

lists = os.listdir(result_dir)

lists.sort(key=lambda fn: os.path.getmtime(result_dir + '\\' +fn))
print((lists[-1]))
file = os.path.join(result_dir, lists[-1])
print(file)
