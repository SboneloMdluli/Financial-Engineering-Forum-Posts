class Bond:
    compounding = 2

    @classmethod
    def set_compounding_frequency(cls, frequency: int) -> None:
        cls.compounding = frequency

    @staticmethod
    def present_valuation(
        par_value: float, yield_to_maturity: float, coupon_rate: float, years: int
    ) -> float:
        yield_to_maturity = yield_to_maturity / (100 * Bond.compounding)
        period = years * Bond.compounding
        price = par_value * (1 + yield_to_maturity) ** -period
        coupon = par_value * coupon_rate / (100 * Bond.compounding)
        price += (coupon / yield_to_maturity) * (1 - (1 + yield_to_maturity) ** -period)
        return price

    @staticmethod
    def duration(
        par_value: float,
        price: float,
        yield_to_maturity: float,
        coupon_rate: float,
        years: int,
    ) -> float:
        coupon = par_value * coupon_rate / (100 * Bond.compounding)
        yield_to_maturity = yield_to_maturity / (100 * Bond.compounding)
        period = years * Bond.compounding
        macaulay_duration = (
            -coupon * yield_to_maturity**-2 * (1 - (1 + yield_to_maturity) ** -period)
            + period
            * (coupon / yield_to_maturity - par_value)
            / ((1 + yield_to_maturity) ** (period + 1))
        ) / price
        return -macaulay_duration / Bond.compounding

    @staticmethod
    def convexity(
        par_value: float,
        price: float,
        yield_to_maturity: float,
        coupon_rate: float,
        years: int,
    ) -> float:
        coupon = par_value * coupon_rate / (100 * Bond.compounding)
        yield_to_maturity = yield_to_maturity / (100 * Bond.compounding)
        period = years * Bond.compounding
        convexity = (
            2
            * coupon
            * yield_to_maturity**-3
            * (1 - (1 + yield_to_maturity) ** -period)
            - 2
            * coupon
            * period
            * yield_to_maturity**-2
            * ((1 + yield_to_maturity) ** -(period + 1))
            + period
            * (period + 1)
            * (par_value - coupon / yield_to_maturity)
            * ((1 + yield_to_maturity) ** -(period + 2))
        )
        return convexity / (price * Bond.compounding**2)
