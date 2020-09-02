import pika

#建立连接
userx = pika.PlainCredentials("guest", "guest")
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", 5672, 'cms_host', credentials=userx))

#开辟管道
channelx = conn.channel()

#声明队列，参数为队列名
channelx.queue_declare(queue="test1")

#消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
def callbackfun(ch, method, properties, body):
    #print(ch)
    #print(method)
    #print(properties)
    
    print("得到的数据为:", body.decode())
    #ch.basic_ack(delivery_tag=method.delivery_tag)


#接收准备 #no_ack=True #是否发送消息确认
channelx.basic_consume(on_message_callback = callbackfun, queue='queuecqccn', auto_ack=True)
print("-------- 开始接收数据 -----------")

#开始接收消息
channelx.start_consuming()