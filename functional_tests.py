from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """docstring for NewVisitorTest"""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 小明听说了一个很不错了To-Do应用网站
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页的标题和头部都包含“ To-Do ”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')
        # 他在一个文本框中输入了“ Buy peacock feathers (购买孔雀羽毛)“
        # 伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')
        # 他按回车键后,页面更新了
        # 待办事项表格中显示了“ 1: Buy peacock feathers ”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框,可以输入其他的待办事项
        # 他输入了“ Use peacock feathers to make a fly (使用孔雀羽毛做假蝇)”
        # 小明做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 页面再次更新,他的清单中显示了这两个待办事项
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # 小明想知道这个网站是否会记住他的清单

        # 他看到网站为他生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能
        # 他访问那个URL,发现他的待办事项列表还在

        # 他很满意,去睡觉了
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
