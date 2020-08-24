import pika

#建立连接
userx = pika.PlainCredentials("chongqing_youxian_jufang","8xQjF73Dk2qB")
conn = pika.BlockingConnection(pika.ConnectionParameters("125.62.27.92", 5672, '/cms_host', credentials=userx))

#开辟管道
channelx = conn.channel()

#声明队列，参数为队列名
channelx.queue_declare(queue="chongqing_youxian_jufang_assetInfo")

#消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
def dongcallbackfun(v1, v2, v3, bodyx):
    print("得到的数据为:", bodyx)

#接收准备
channelx.basic_consume(dongcallbackfun, #收到消息的回调函数
                       queue="chongqing_youxian_jufang_assetInfo", #队列名
                       no_ack=True #是否发送消息确认
                       )
print("-------- 开始接收数据 -----------")

#开始接收消息
channelx.start_consuming()