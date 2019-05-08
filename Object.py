class Parent:
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        self.parentAttr = attr

    def setParentAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
         print("子类属性:%d" % self.parentAttr)

    def getParentAttr(self):
         print("父类属性:%d" % Parent.parentAttr)

    def myMethod(self):
        print("调用父类我的方法")


class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

    def myMethod(self):
        print("调用子类我的方法")


child = Child()
child.childMethod()
child.parentMethod()
child.setAttr(200)
child.setParentAttr(300)
child.getAttr()
child.getParentAttr()
child.myMethod()
