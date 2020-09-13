import requests


def request_order(url, params):
    # headers = {'Authorization': 'Bearer 8D5497F9347C452F81F380F5D2DD5963'}    # CHOP offpay
    # headers = {'Authorization': 'Bearer 5F08A36D02754CBB84E960E896B0DA1A'}    # CHOP gmail
    headers = {'Authorization': 'Bearer B614E02D83D344C391081AA0606E0B11'}    # API ONLINE

    response = requests.post(url, data=params, headers=headers)
    resp_dic = response.text
    return resp_dic



def QR_pay_order():
    """二维码支付接口"""
    url = 'https://uat.citconpay.com/payment/pay_qr'

    params = {
        "vendor": 'wechatpay',
        "amount":"1",
        "currency":"USD",
        "reference":"jkh25jh13481231312367",
        "allow_duplicates":"yes",
    }

    return request_order(url, params)


def H5_pay_order():
    """H5端支付接口"""
    url = 'https://uat.citconpay.com/payment/pay'

    params = {
        "amount": '1',
        "currency": 'USD',
        "vendor": 'wechatpay',
        "reference": "jkh25jh13481231312367",
        "allow_duplicates": "yes",
    }

    return request_order(url, params)


def refund_order():
    """退款接口"""
    url = 'https://uat.citconpay.com/payment/refund'

    params = {
        "amount": '1',
        "currency": 'USD',
        "transaction_id": 'U0000031948-074875bfdc673fcfb868',
        "reason": '',
    }

    return request_order(url, params)


def inquire():
    """查询特定付款和/或订单的状态"""
    url = 'https://uat.citconpay.com/payment/inquire'

    params = {
        # "transaction_id": '',
        "reference": 'jkh25jh13481231312367',
        "inquire_method": 'real',
    }

    return request_order(url, params)


def transactions():
    """查询商家所有交易信息"""
    url = 'https://uat.citconpay.com/payment/transactions'

    params = {}

    return request_order(url, params)


if __name__ == '__main__':
    print(H5_pay_order())
