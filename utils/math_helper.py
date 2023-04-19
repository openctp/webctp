import sys

class MathHelper(object):

    @staticmethod
    def adjust_price(price: float) -> float:
        if price == sys.float_info.max:
            price = 0
        return price
                