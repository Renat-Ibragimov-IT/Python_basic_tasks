# 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
#   Input:
#   coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
#   code = ('BTC', 'ETH', 'XRP', 'LTC')
#   Output:
#   {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def merging_into_dict(some_tuple: tuple, some_tuple_2: tuple) -> dict:
    return dict(zip(some_tuple, some_tuple_2))


print(merging_into_dict(coin, code))
