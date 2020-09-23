import yaml, os,sys

"""
获取.yaml中的数据
"""
def Read_data(file_path):
    # 得到文件路径
    file = os.getcwd() + os.sep + "Data" + os.sep + file_path + ".yaml"
    with open(file, "rb") as f:
        return yaml.load(f)
