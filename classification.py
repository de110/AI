import tensorflow as tf
import numpy as np

x_data = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
y_data = np.array([[0,0,0,1],[0,0,1,0],[0,0,0,1],[0,1,0,0],[0,0,0,1],[0,0,0,1],[1,0,0,0],[1,0,0,0]])

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([3,10],-1.0,1.0))
W2 = tf.Variable(tf.random_uniform([10,4],-1.0,1.0))

b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([4]))

Z1=tf.add(tf.matmul(X,W1),b1)
L1=tf.nn.relu(Z1)

model = tf.add(tf.matmul(L1,W2),b2)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y,logits=model))

optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)

init =tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(5000):
  sess.run(train_op, feed_dict ={X:x_data, Y:y_data})
 
  if(step+1)%10==0:
    print(step+1,sess.run(cost,feed_dict={X:x_data,Y:y_data}))
   
prediction =tf.argmax(model,axis=1)
target=tf.argmax(Y,axis=1)
print('Predict Value: ',sess.run(prediction,feed_dict={X:x_data}))
print('Real Value: ',sess.run(target,feed_dict={Y:y_data}))

is_correct = tf.equal(prediction,target)
accuracy =tf.reduce_mean(tf.cast(is_correct,tf.float32))
print('Accuracy: %.2f'%sess.run(accuracy*100,feed_dict={X:x_data,Y:y_data})) 
