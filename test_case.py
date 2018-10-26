# coding=utf-8

import unittest
from base.request_method import RunMain
from utils.excel_tool import ExcelTool
from config import config

class test(unittest.TestCase):
    def setUp(self):
        self.run_method = RunMain()
        self.ET = ExcelTool(config.FILE_NAME)
        self.lines =self.ET.get_row()

    def test_01(self):
        global result
        for i in range(1,self.lines):
            is_run = self.ET.get_cell(i,config.IS_RUN)
            url = self.ET.get_cell(i, config.URL)
            is_header = self.ET.get_cell(i, config.IS_HEADER)
            header = self.ET.get_cell(i, config.HEADER)
            method = self.ET.get_cell(i, config.METHOD)
            data = self.ET.get_cell(i, config.DATA)
            expect_result = self.ET.get_cell(i, config.EXPECT_CODE)
            if is_run == 'yes':
                if method == 'Post':
                    if is_header == 'yse':
                        result = self.run_method.send_post(url,data,header)
                    else:
                        result = self.run_method.send_post(url,data)
                else:
                    if is_header == 'yse':
                        result = self.run_method.send_get(url,header)
                    else:
                        result = self.run_method.send_get(url)
            self.assertEqual(result,expect_result)

    def tearDown(self):
        print('测试完成')



