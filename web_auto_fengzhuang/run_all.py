# -*- coding: utf-8 -*-
import unittest
from web_auto_fengzhuang.common import HTMLTestRunner_cn

# 获取存放用例路径
casePath = 'D:\pyCodeDesign\web_auto_fengzhuang\case'
# 匹配py文件规则
ruler = 'test*.py'
# 去寻找这些文件
discover = unittest.defaultTestLoader.discover(start_dir=casePath,
                                               pattern=ruler)
print(discover)

# 获取存放报告的路径，加一个html文件
reportPath = "D:\\pyCodeDesign\\web_auto_fengzhuang\\report\\" + "report.html"
# 使用open函数去读取reportPath
fp = open(reportPath, "wb")
# 执行
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="报告的tiele",
                                          description="描述你的报告干什么用的",
                                          retry=1)  # retry=1 失败重跑一次

# 运行
runner.run(discover)
fp.close()
