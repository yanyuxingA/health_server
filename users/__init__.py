import xmltodict
#json转xml函数
def jsontoxml(jsonstr):
    #xmltodict库的unparse()json转xml
    xmlstr = xmltodict.unparse(jsonstr)
    print(xmlstr)
if __name__ == "__main__":
    # json = {'student': {'course': {'name': 'math', 'score': '90'},
    #                     'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    json = {'beans': {'hawbs': [{'hawbno': '分单号', 'mail_no': '运单号'}, {'hawbno': '分单号', 'mail_no': '运单号'}], 'req_type': 'query_order'}}

    jsontoxml(json)