from aip import AipOcr
import os


"""你的百度AppID, API Key, Secret Key"""
APP_ID = '18393159'
API_KEY = 'qbK2kKKtrXTo0rE1rg4M6Tl6'
SECRET_KEY = 'nXb0pyumWK22EFzGFwpi3WQCvWllYneo'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

"""打开文件，读取图片"""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))          # 获取项目根目录
path = os.path.join(PROJECT_ROOT, "images")         # 文件路径

for r, ds, fs in os.walk(path):
     for fn in fs:
        fname = os.path.join(r, fn)
        image = get_file_content(fname)
        ret = client.basicGeneral(image)
        print(ret)
        # for item in ret['words_result']:
        #     print(item['words'])
