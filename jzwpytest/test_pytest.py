# 切换test runner到pytest
# 清理之前的configuration

# pytest会从当前目录开始，搜索test_*和*_test结尾的文件
# Test开头的类中的test开头的方法（类中不能用init初始化方法）


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def setup_module():
    print("setup_module")


def setup_function():
    print("setup_function")


class TestDemo:
    # test fixture 用例执行顺序

    def setup(self):
        print("setup")

    # 类方法的装饰器，注解，为了区分识别实例和类方法
    @classmethod
    def setup_class(self):
        print("setup_class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        hasattr()
        # 函数用于判断对象是否包含对应的属性。
        assert hasattr(x, "check")

    def test_x(self):
        demo = TestDemo()
        demo.test_one()
