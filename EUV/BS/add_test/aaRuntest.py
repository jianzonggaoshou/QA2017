# -*- coding: utf-8 -*-
import unittest
import addTest

# 构造测试集
suite = unittest.TestSuite()

suite.addTest(addTest.AddTest("test_userBuild"))
suite.addTest(addTest.AddTest("test_userBuild"))
suite.addTest(addTest.AddTest("test_userBuild"))
suite.addTest(addTest.AddTest("test_userBuild"))
suite.addTest(addTest.AddTest("test_userBuild"))
suite.addTest(addTest.AddTest("test_userBuild"))


if __name__ == '__main__':
	# 执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
