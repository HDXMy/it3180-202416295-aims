MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)
    
    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        
        print("****************-CART-****************")
        print("Ordered Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. DVD - {item.title} - {item.category} - {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("**************************************")
   
    def calculate_discount(self, total, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Invalid discount percent")
        return total * (100 - percent) / 100

    def sort_by_title(self):
        """Sắp xếp các sản phẩm trong giỏ hàng theo tiêu đề (title) tăng dần."""
        # Giả sử mỗi item trong giỏ hàng có thuộc tính title hoặc đối tượng media có title
        self.items.sort(key=lambda item: item.title)

    def sort_by_cost(self):
        """Sắp xếp các sản phẩm trong giỏ hàng theo giá tiền (cost/price) tăng dần."""
        # Giả sử mỗi item có thuộc tính cost hoặc price
        self.items.sort(key=lambda item: item.cost)
    