import demo_pb2

if __name__ == '__main__':
    sr = demo_pb2.SearchRequest()
    sr.query = 'baidu.com'
    sr.page_no = 1
    sr.nums = 2

    data = sr.SerializeToString()
    print(data)
    tar = demo_pb2.SearchRequest()
    tar.ParseFromString(data)
    print(tar)
    