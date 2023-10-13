import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

deep_ecg_model_path = '/home/ubuntu/aimodel/dirichlet_model/model-26000.meta'

def load_model_and_predict(data):
    saver = tf.train.import_meta_graph(deep_ecg_model_path)

    with tf.Session() as sess:
        saver.restore(sess, "model-26000")

        graph = tf.get_default_graph()

        for op in graph.get_operations():
          print(op.name)

        # # 需要根据模型替换为实际的 tensor 名字
        # input_tensor = graph.get_tensor_by_name('input_node_name:0')
        # output_tensor = graph.get_tensor_by_name('output_node_name:0')

        # predictions = sess.run(output_tensor, feed_dict={input_tensor: data})

        # return predictions

def main():
    # 传入要进行预测的数据
    data = None  # 方法通过这里传递预测数据
    predictions = load_model_and_predict(data)

    # 打印或者返回预测结果
    print(predictions)


if __name__ == "__main__":
    main()
