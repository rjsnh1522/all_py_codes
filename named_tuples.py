from collections import namedtuple

ProductAvailability = namedtuple(
    "ProductAvailability",
    (
        "available",
        "on_sale",
        "price_range",
        "price_range_undiscounted",
        "discount",
        "price_range_local_currency",
        "discount_local_currency",
    ),
)


vv = ProductAvailability(
    available="true",
    on_sale=True,
    price_range="0-200",
    price_range_undiscounted="20",
    discount="5",
    price_range_local_currency="0-200",
    discount_local_currency="rs",
)


def one_method() -> ProductAvailability:

    return vv


print(one_method())
