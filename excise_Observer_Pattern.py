#coding=utf-8
#大V的基类
class Publisher:
    def __init__(self):
        pass
#关注
    def register(self):
        pass
#取消关注
    def unregister(self):
        pass
#发布微博
    def notifyall(self):
        pass

#这是这个大V的子类
class Sina(Publisher):
    def __init__(self):
        self.listofuser =[]   #粉丝列表
        self.postname= None  #微博内容
#关注
    def register(self,username):
        if username not in self.listofuser:
            self.listofuser.append(username)
#取关：
    def unregister(self,username):
        self.listofuser.remove(username)
#发微博
    def notifyall(self):
        for user in self.listofuser:
            user.notify(self.postname)
#写微博
    def writenewpost(self,postname):
        self.postname=postname
        self.notifyall()

#粉丝的基类
class suscriber:
    def __init__(self):
        pass
    def notify(self):
        pass

#粉丝的子类
class user(suscriber):
    def __init__(self,susbribername):
        self.susbribername = susbribername
    def notify(self,postname):
        print "%s notified of a new post %s" %(self.susbribername,postname)


if __name__=="__main__":
    jingyu = Sina()
    doudou = user("doudou")
    hehe = user("hehe")

    jingyu.register(doudou)
    jingyu.register(hehe)

    jingyu.writenewpost("love doudou &&hehe")
    jingyu.unregister(hehe)
    jingyu.writenewpost("hehe is disappear")
    
