from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        for text, emo in {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }.items():
            result_1 = emotion_detector(text)
            self.assertEqual(result_1["dominant_emotion"], emo)


unittest.main()
