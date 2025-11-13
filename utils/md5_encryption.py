import hashlib

class md5_encrytion:
    def __init__(self,str_d):
        hl = hashlib.md5()
        # print("需要加密的内容：" + str_d)
        # 1. 将字符串编码为 UTF-8 字节
        encoded_string = str_d.encode("utf-8")
        # 2. 更新 MD5 对象
        hl.update(encoded_string)
        # 3. 获取十六进制摘要
        md5_result = hl.hexdigest()
        self.md5_result = md5_result

    def get_md5(self):
        return self.md5_result


if __name__ == '__main__':
    md5 = md5_encrytion("自动化按键").get_md5()
    print(md5)