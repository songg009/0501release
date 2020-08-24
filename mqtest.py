# coding:gb2312
import pika
import time
import os
import sys
import time
from stat import S_ISREG, ST_CTIME, ST_MODE

try:
    import cPickle as pickle
except ImportError:
    import pickle

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)

rabbitmq_username = 'chongqing_youxian_jufang'
rabbitmq_password = '8xQjF73Dk2qB'
rabbitmq_host = '125.62.27.92'
rabbitmq_port = 5675
rabbitmq_exchange_name = ''
rabbitmq_exchange_routing_key = ''


class mq_tool:
    def __int__(self):
        self._connection = None
        self._channel_1 = None
        self._channel_2 = None
    
    def connect(self):
        try:
            credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
            parameters = pika.ConnectionParameters(rabbitmq_host, 5675, '/cms_host', credentials)
            connection = pika.BlockingConnection(parameters)
            self._connection = connection
            self._channel_1 = self._connection.channel()
            self._channel_2 = self._connection.channel()
            self._channel_1.queue_declare(queue="chongqing_youxian_jufang_assetInfo")
            return True
        except:
            raise
        return False
    
    def publish(self, txt):
        try:
            # channel = self._connection.channel()
            self._channel_1.basic_publish(exchange=rabbitmq_exchange_name,
                                          routing_key=rabbitmq_exchange_routing_key,
                                          body=txt)
            return True
        except:
            raise
        return False
    
    def close(self):
        self._connection.close()
        self._connection = None


def sync_file(file_path, from_line):
    mq = mq_tool()
    if not mq.connect():
        return 0
    print('sync file [%s] from line(%d) start..' % (file_path, from_line))
    f = open(file_path, 'r')
    line_num = 0
    done_num = 0
    time_s = int(time.time())
    for line in f:
        line_num += 1
        if line_num < from_line:
            continue
        if line.find('>: LogText:') <= 0:
            done_num += 1
            continue
        try:
            
            line = line[47:-1]
            ret = True
            
            ret = mq.publish(line[47:-1])
        except:
            ret = False
            raise
        if not ret:
            break
        time_e = int(time.time())
        if time_e > time_s:
            print
            done_num
            time_s = time_e
        done_num += 1
    print('sync file [%s] done line(%d)s.' % (file_path, from_line + done_num))
    # mq.close()
    return done_num


sync_file('2017_12_16_00_00_03.log', 0)