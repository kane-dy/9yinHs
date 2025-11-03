import os

#获取项目地址
def path():
    path =os.path.abspath(os.path.join(os.getcwd()))
    return path


def p_d_path():
    path =os.path.join(os.getcwd(), "../..")
    return path
