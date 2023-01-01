# redis on local machine
import redis

conn = redis.Redis('localhost', 6379)

conn.set('dog', 'nufy')
conn.set('secret', 'ni!')
conn.set('fever', '101.5')


print(conn.keys('*'))
print('secret =', conn.get('secret'))

conn.incrbyfloat('fever', 2)
print('fever = ', conn.get('fever'))

#test expiration of key
import time

conn.expire('fever',3)
time.sleep(5)
print(conn.keys('*'))
