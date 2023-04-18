
import sys

class MathHelper(object):

    min_price_unit:float = 1e-10

    @staticmethod
    def adjust_price(price: float) -> float:
        if price == sys.float_info.max or abs(price) < MathHelper.min_price_unit:
            return 0
                