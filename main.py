import time, os, random, json

from baidu_api import *
from file import createFile

from aip import AipOcr

# 打开文件，读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_file_path():
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))          # 获取项目根目录
    path = os.path.join(PROJECT_ROOT, "images")               # 文件路径

    return path

if __name__ == "__main__":
    api = Api()

    path = get_file_path()
    client = AipOcr(api.getID(), api.getKEY(), api.getSecretKEY())

    num = 1
    for root, dirs, files in os.walk(path):
         for fn in files:
            f_name = os.path.join(root, fn)     # path+文件名
            image = get_file_content(f_name)
            ret = client.basicGeneral(image)
            file_name = createFile(num)
            for item in ret['words_result']:
                s = item['words']
                with open(file_name, 'ab') as f:
                    f.write(s.encode('utf-8'))
                    f.write('\n'.encode('utf-8'))
            print(num, "保存成功")
            num = num + 1
            time.sleep(random.randint(1, 2))
