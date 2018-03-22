#coding=utf-8
'''
练习：
写一个密码生成器的类：
要求有个类变量，统计一下一共生成过多少个密码。
要求有4个方法，1：构造函数 2 实例方法  3 类方法  4 静态方法

生成指定长度的随机数字密码
生成指定长度的随机字母密码
生成指定长度的随机数字和字母的混合
'''
import random

class PassWordGen:
    count = 0
    def __init__(self):
        print "password gen is starting now!"

    def gen_num_password(self,length):
        if isinstance(length,int):
            a=range(length)
            random.shuffle(a)
            PassWordGen.count+=1
            return "".join(map(str,a))[0:length]
        else:
            print "wrong length"
            
    @classmethod
    def gen_letter_password(cls,length):
        if isinstance(length,int) and length <=26:
            a=map(chr,range(97,122))
            random.shuffle(a)
            PassWordGen.count+=1
            return "".join(a)[:length]
        else:
            print "wrong length"

    @staticmethod
    def gen_mixed_password(length):
        if isinstance(length,int) and length >=2:
            num_password_length = length/2
            letter_password_length=length - num_password_length
            a=range(num_password_length)
            random.shuffle(a)
            num_part= "".join(map(str,a))[0:num_password_length]
            b=map(chr,range(97,122))*letter_password_length
            random.shuffle(b)
            text_part = "".join(b)[:letter_password_length]
            PassWordGen.count+=1
            return num_part+text_part
        else:
            print "wrong length"

    @staticmethod
    def get_gen_password_times():
        return PassWordGen.count

if __name__ == "__main__":
    print PassWordGen.gen_mixed_password(10)
    print PassWordGen.gen_letter_password(10)
    p=PassWordGen()
    print p.gen_num_password(10)
    print PassWordGen.get_gen_password_times()
