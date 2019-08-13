# 编写Page Object 设计模式
class Page(object):
    """
    页面基础类，用于所有页面的继承
    """

    bbs_url = 'http://bbs.meizu.cn'

    # 初始化参数：浏览器驱动、URL地址、超时时长
    """
    想理解此处的selenium_driver,首先要弄清Page&login、MyTest&loginTest他们的继承关系、调用关系；
    此行代码意思是：Page类初始化时，第二个参数要传入一个driver实例，因为unittest框架的setUp函数，用例执行前都会调用，所以浏览器对象在setUp()调用时已经实例化。
    后续说明，见login_sta.py 21行
    """
    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.bbs_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    # 带_ 的是私有函数，文件外部想通过导入模块调用，是不行的
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    # 定位单个元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)  # 调用的系统的函数

    # 定位多个元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 打开地址
    def open(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)
