"""
枚举
"""

from enum import Enum, unique, auto, IntEnum

import unittest

# 定义Http 状态值, 添加unique后枚举值不能重复
@unique
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500


for status in HttpStatus:
    print("%s : %s " % (status.name, status.value))


# 枚举自动赋值
# 使用 auto() 得到的是整数自增型，如果我们需要别的方式，只需要在我们的枚举类中，重写 _generate_next_value_ 方法。
class TestEnum(unittest.TestCase):

    def test_auto_number(self):
        class Color(Enum):
            red = auto()
            blue = auto()
            green = auto()

        self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
        self.assertEqual(Color.red.value, 1)
        self.assertEqual(Color.blue.value, 2)
        self.assertEqual(Color.green.value, 3)

    def test_auto_name(self):
        class Color(Enum):
            def _generate_next_value_(self, start, count, last):
                return self

            red = auto()
            blue = auto()
            green = auto()

        self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
        self.assertEqual(Color.red.value, 'red')
        self.assertEqual(Color.blue.value, 'blue')
        self.assertEqual(Color.green.value, 'green')


# 枚举比较
# 枚举值不能直接进行比较，如果需要这样继承IntEnum
class TestEnum1(unittest.TestCase):
    class Season(IntEnum):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4
    
    def test_comparisons(self):
        season = self.Season

        self.assertEqual(season.SPRING, 1)

        class Part(Enum):
            SPRING = 1
            CLIP = 2
            BARREL = 3
        
        self.assertNotEqual(Part.SPRING, 1)
        self.assertNotEqual(Part.SPRING, season.SPRING)
    

# 枚举继承
# python 中的枚举类是可以被继承的，但是被继承的枚举类规定其不能定义任何成员，但可以定义抽象方法。举例如下：
class TestEnumExtend(unittest.TestCase):
    
    def test_extending(self):
        
        class Shade(Enum):
            
            def shade(self):
                print(self.name)
            
        class Color(Shade):
            red = 1
            green = 2
            blue = 3
        
        with self.assertRaises(TypeError):
            class MoreColor(Color):
                cyan = 4
                magenta = 5
                yellow = 6
    
    def test_extending2(self):
        class Shade(Enum):
            def shade(self):
                return self.name
        
        class Color(Shade):
            def hex(self):
                return '%s nice!' % self.value
        
        class MoreColor(Color):
            cyan = 4
            magenta = 5
            yellow = 6
        
        self.assertEqual(MoreColor.magenta.shade(), 'magenta')
        self.assertEqual(MoreColor.magenta.hex(), '5 nice!')

if __name__ == '__main__':
    TestEnum().test_auto_number()
    TestEnum1().test_comparisons()
    TestEnumExtend().test_extending()
    TestEnumExtend().test_extending2()

