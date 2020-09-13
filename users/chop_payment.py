import requests


def request_order(url, params):
    # headers = {'Authorization': 'Bearer 8D5497F9347C452F81F380F5D2DD5963'}    # CHOP offpay
    headers = {'Authorization': 'Bearer 5F08A36D02754CBB84E960E896B0DA1A'}    # CHOP gmail
    # headers = {'Authorization': 'Bearer B614E02D83D344C391081AA0606E0B11'}    # API ONLINE

    response = requests.post(url, data=params, headers=headers)
    resp_dic = response.text
    return resp_dic



def pay_order():
    """支付接口"""
    url = 'https://uat.citconpay.com/chop/chop'

    params = {
        "payment_method":"ccrecurring",
        "amount":"2",
        "currency":"CNY",
        "reference":"P00000000002",
        "allow_duplicates":"yes",
    }

    return request_order(url, params)


def refund_order():
    """退款接口"""
    url = 'https://uat.citconpay.com/chop/refund'

    params = {
        "amount": '2',
        "currency": 'USD',
        "transaction_id": 'bd2669207c3dde888e4f788cd',
        "reason": '',
    }

    return request_order(url, params)


def inquire():
    """查询特定付款和/或订单的状态"""
    url = 'https://uat.citconpay.com/chop/inquire'

    params = {
        "q": 'fdc93e62ddab53f7e5f14383b',
        "inquire_method": 'real'
    }

    return request_order(url, params)


def transactions():
    """查询商家所有交易信息"""
    url = 'https://uat.citconpay.com/chop/transactions'

    params = {}

    return request_order(url, params)


if __name__ == '__main__':
    print(pay_order())
