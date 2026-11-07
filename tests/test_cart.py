import unittest
from aims.cart import Cart
# Import các lớp Media/Product tùy theo cấu trúc dự án của bạn

class TestCartSorting(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        # Tạo sẵn các item giả lập với title và cost khác nhau để kiểm tra
        # Ví dụ: item1, item2, item3...

    def test_sort_by_title(self):
        # Thực hiện sắp xếp
        self.cart.sort_by_title()
        # Kiểm tra thứ tự tiêu đề sau khi sắp xếp đã chuẩn tăng dần hay chưa
        titles = [item.title for item in self.cart.items]
        self.assertEqual(titles, sorted(titles))

    def test_sort_by_cost(self):
        # Thực hiện sắp xếp theo giá
        self.cart.sort_by_cost()
        # Kiểm tra thứ tự chi phí sau khi sắp xếp đã chuẩn tăng dần hay chưa
        costs = [item.cost for item in self.cart.items]
        self.assertEqual(costs, sorted(costs))

if __name__ == '__main__':
    unittest.main()