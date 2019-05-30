# -*- coding: utf-8 -*-
import unittest


class IntegerArithmeticTestCase(unittest.TestCase):  # 继承unittest里面的TestCase这个类
    '''第一个案例'''
    #   setUp(self) tearDown(self) setUpClass(cls) tearDownClass(cls)四个可以随意搭配使用
    #  但是setUpClass(cls) tearDownClass(cls)使用前要先添加注解@classmethod，他们四个的优先级
    #  setUpClass(cls)的优先级最高其次是setUp(self)，测试用例

    def setUp(self):
        # setUp(self)在每个用例之前先调用一次
        print("先打开浏览器")

    def tearDown(self):
        # tearDown(self)在每个用例执行完调用一次

        print("关闭浏览器")

    @classmethod
    def setUpClass(cls):  # 必须要加 @classmethod注解
        print("用例前只执行一次")

    @classmethod
    def tearDownClass(cls):  # 必须要加 @classmethod注解
        print("用例后只执行一次")


    # 测试用例的执行顺序是按照ASCII码来执行的，即0-9 A-Z a-z
    def test_1(self):
        '''1111'''
        print("test-1")
        a='admin'
        b='admin'
        self.assertTrue(a==b)#判断两个字符串是否相等
        '''
        self.assertTrue(a!=b)#判断两个字符串是否不相等
        self.assertTrue(a in b)#判断a是否包含b
        self.assertTrue(a not in b)#判断a是否不包含b
        self.assertEquals(a,b)#传参数判断相等
        self.assertNotEquals(a,b)#传参数判断不相等
        self.assertIn(a,b)  #判断a在b里面
        self.assertNotIn(a,b) #判断a不在b里面
        self.assertIsNone(x)  #判断返回值为空
        self.assertIsNotNone(x)    #判断返回值不为空
        '''
    def testAdd(self):  # 测试用例方法名称以“test*”开头 test后面随便定义 但是要以test开头
        '''add'''
        self.assertEqual((1 + 2), 3)
        print('((1 + 2), 3)')
        self.assertEqual(0 + 1, 1)
        print('(0 + 1, 1)')

    def testMultiply(self):
        '''multiply'''
        self.assertEqual((0 * 10), 0)
        print('((0 * 10), 0)')
        self.assertEqual((5 * 8), 40)
        print('((5 * 8), 40)')


if __name__ == '__main__':
    '''
   如果在导入后不调用__name__他是不会执行if一下的代码
   print(__name__)打印出来是__main__
    '''
    unittest.main()
