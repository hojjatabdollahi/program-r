import tensorflow as tf
import numpy as np
import tflearn
import cv2
import argparse
import time
from collections import deque
import collections
from threading import Thread
import time
from threading import Lock
import inference_usbCam_face

mutex = Lock()
# Basic model parameters as external flags.
FLAGS = None
n = 9
BUFFER_CAPACITY=15
PATH_TO_CKPT = './model/frozen_inference_graph_face.pb'



class TensoflowFaceDector(object):
    def __init__(self, PATH_TO_CKPT):
        """Tensorflow detector
        """

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')


        with self.detection_graph.as_default():
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(graph=self.detection_graph, config=config)
            self.windowNotSet = True


    def run(self, image):
        """image: bgr image
        return (boxes, scores, classes, num_detections)
        """

        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        # Actual detection.
        start_time = time.time()
        (boxes, scores, classes, num_detections) = self.sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})
        elapsed_time = time.time() - start_time
        print('inference time cost: {}'.format(elapsed_time))

        return (boxes, scores, classes, num_detections)



class DeepFER():
    def softmax(self, x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def switch(self, argument):
        switcher = {
            -1: " No Face",
            0: "Negative",
            1: "Neutral",
            2: "Positive",
            3: "Surprise",
            4: " Disgust"
        }
        return switcher.get(argument, "Invalid emotion")

    def load_image(self, addr, size):
        # read an image and resize to (224, 224)
        # cv2 load images as BGR, convert it to RGB
        img = cv2.imread(addr)
        img = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = img.astype(np.float32)
        return img

    def resnet(self, _X):
        global n
        net = tflearn.conv_2d(_X, 16, 3, regularizer='L2', weight_decay=0.0001)
        net = tflearn.residual_block(net, n, 16)
        net = tflearn.residual_block(net, 1, 32, downsample=True)
        net = tflearn.residual_block(net, n - 1, 32)
        net = tflearn.residual_block(net, 1, 64, downsample=True)
        net = tflearn.residual_block(net, n - 1, 64)
        net = tflearn.batch_normalization(net)
        net = tflearn.activation(net, 'relu')
        net = tflearn.global_avg_pool(net)
        # Regression
        logits = tflearn.fully_connected(net, 3, activation='linear')
        return logits

    def zscore_normalize(self, image, label):
        norm_image = tf.image.per_image_standardization(image)
        return norm_image, label


    ####Main function
    def run_validation(self):
        """Train MNIST for a number of steps."""

        tDetector = TensoflowFaceDector(PATH_TO_CKPT)

        # Very important: this line is needed so the code doesn't crash when used in a Python Thread
        # It was a miracle that I found this hack on the internet
        tflearn.config.init_training_mode()

        # These lines are important so the code works in a class
        global learning_rate
        global BUFFER_CAPACITY

    
        # Creating input placeholders
        image_batch_placeholder = tf.placeholder(tf.float32, shape=(None, 64, 64, 3), name="image_batch_placeholder")
        label_tensor_placeholder = tf.placeholder(tf.int32, shape=(None, 3), name="label_tensor_placeholder")

        # ResNet ligits
        pred = self.resnet(image_batch_placeholder)

        saver = tf.train.Saver()

        # The op for initializing the variables.
        init_op = tf.group(tf.global_variables_initializer(),
                           tf.local_variables_initializer())

    
        # VIDEO CAPTUREING
        cap = cv2.VideoCapture(0)
        F_HEIGHT = int(cap.get(4))
        F_WIDTH = int(cap.get(3))
        ####
        ####  Network definition ends here!!!
        ####
        # Create a session for running operations in the Graph.

        with tf.Session(config=
    tf.ConfigProto(inter_op_parallelism_threads=1,
                   intra_op_parallelism_threads=1)) as sess:

            
            print("Loading following model:ResNet56_valence_lr_5-86000 ")# + tf.train.latest_checkpoint('./Snapshots/'))
            start_time = time.time()
            import os
            saver.restore(sess, "Snapshots/ResNet56_valence_lr_5_classified-250500")#tf.train.latest_checkpoint(os.getcwd()))

            duration = time.time() - start_time
            print("Done! in %.3f seconds" % duration)
            accs = []
            try:
                # creating the buffer
                buffer_ = deque()
                while True:
                    start_time = time.time()
                    ret, frame = cap.read()
                    if frame is not None:
                        emotion_ID = -1
                        # Detecting faces using detectors
                        image = cv2.flip(frame, 1)
                        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        # faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
                        # if (len(faces) == 0):
                            # faces = face_cascade3.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
                            # if (len(faces) == 0):
                                # faces = face_cascade2.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
                        (boxes, scores, classes, num_detections) = tDetector.run(image)

                        # Checking if any faces were found and selecting the largest face among them
                        if len(boxes) >= 1:
                            face = boxes[0,np.argmax(scores),:]
                            ymin, xmin, ymax, xmax = face
                            ymin = int(ymin*480)
                            ymax = int(ymax*480)
                            xmin = int(xmin*640)
                            xmax = int(xmax*640)
                            patch = image[ ymin:ymax, xmin:xmax, :]
                            cv2.rectangle(frame, (640-xmin, ymin ), (640-xmax, ymax), (0, 255, 0), 2)
                            if patch is not None:
                                # Preparing the face region for the network
                                patch = cv2.resize(patch, (64, 64), interpolation=cv2.INTER_CUBIC)
                                patch = cv2.cvtColor(patch, cv2.COLOR_BGR2RGB)
                                patch = patch.astype(np.float32)
                                ## normalization
                                norm_image = patch * (1.0 / 255.0)
                                ## zscore normalization
                                norm_image_expanded = np.expand_dims(norm_image, axis=0)
                                pred_val = sess.run(pred, feed_dict={image_batch_placeholder: norm_image_expanded})

                                emotion_ID = pred_val[0].argmax(axis=0)
                                confidence = max(self.softmax(pred_val[0]))
                                confidence_str = "%.2f" % confidence

                        # Pusing in the buffer
                        if len(buffer_) < BUFFER_CAPACITY:
                            buffer_.append(emotion_ID)
                        else:
                            buffer_.popleft()
                            buffer_.append(emotion_ID)
                        counter = collections.Counter(buffer_)

                        # Selecting the most common emotion in the buffer
                        vote = counter.most_common(1)[0][0]
                        '''
          
                        Your modifications can go here...
          
          
                        '''
                        emotion_str = ""
                        if vote != -1:
                            emotion_str = self.switch(vote)
                        else:
                            emotion_str = -1

                        if True:
                            if vote != -1:
                                cv2.putText(frame, emotion_str + " " + confidence_str, (640-int(xmin), int(ymin)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                            duration = time.time() - start_time
                            # Frame rate calculation
                            fr_rate = "%.2f" % (1 / duration)
                            cv2.putText(frame, fr_rate, (20, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

                            # Display
                            cv2.imshow('frame', frame)

                            # Exit condition
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                cap.release()
                                cv2.destroyAllWindows()
                                break
                        else:
                            cv2.destroyAllWindows()



                    time.sleep(0.01)
            except tf.errors.OutOfRangeError:
                quit()


    def main(self):
        global FLAGS
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--num_epochs',
            type=int,
            default=1,
            help='Number of epochs to run trainer.')
        parser.add_argument('--batch_size', type=int, default=512, help='Batch size.')
        FLAGS, unparsed = parser.parse_known_args()
        self.run_validation()



if __name__ == "__main__":
    DeepFER().main()
