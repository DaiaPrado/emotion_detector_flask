from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #Test case for joy sentiment
        test_1 = emotion_detector("I am glad this happened")
        self.assertEqual(test_1["dominant_emotion"], "joy")

        #Test case for anger sentiment
        test_2 = emotion_detector("I am really mad about this")
        self.assertEqual(test_2["dominant_emotion"], "anger")

        #Test case for disgust sentiment
        test_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_3["dominant_emotion"], "disgust")

        #Test case for sadness sentiment
        test_4 = emotion_detector("I am so sad about this")
        self.assertEqual(test_4["dominant_emotion"], "sadness")

        #Test case for fear sentiment
        test_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_5["dominant_emotion"], "fear")

unittest.main()