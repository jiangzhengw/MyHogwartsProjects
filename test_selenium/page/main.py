# Time: 2020/7/7 11:22
# Author: jiangzhw
# FileName: main.py
from test_selenium.page.contact import Contact


class Main:
    """登陆后首页PO"""
    def download(self):
        """立即下载"""
        pass

    def import_user(self):
        """发起邀请"""
        pass

    def goto_apps(self):
        """探索企业应用"""
        pass

    def goto_company(self):
        """验证公司主体信息"""
        pass

    def get_massage(self):
        """了解详情"""
        return "aaa"

    def add_member(self):
        """添加成员"""
        # return Contact()
        # 返回当前页面po
        return self

    def add_member_error(self):
        """添加成员失败"""
        # 不同的情况返回的页面不同
        # return AddMemberPage()
        pass
