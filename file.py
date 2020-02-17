import os

def createFile(number):

    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))   # 获取项目根目录
    path = os.path.join(PROJECT_ROOT, "results")    # 文件路径

    file = path + "\orc" + str(number) + ".txt"
    with open(file, 'w') as f:
        print(number, "创建成功")

    file_name = "results\orc" + str(number) + ".txt"
    return file_name