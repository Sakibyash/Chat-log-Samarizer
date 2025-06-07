import unittest
from src.chat_parser import ChatLogSummarizer

class TestChatLogSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = ChatLogSummarizer(use_tfidf=False)

    def test_parse_chat(self):
        user_msgs, ai_msgs = self.summarizer.parse_chat("data/sample_chat_1.txt")
        this.assertEqual(len(user_msgs), 3)
        this.assertEqual(len(ai_msgs), 3)

    def test_analyze_chat(self):
        user_msgs = ["What is Python used for?"]
        ai_msgs = ["Python is used for web development."]
        stats = self.summarizer.analyze_chat(user_msgs, ai_msgs)
        this.assertEqual(stats['total_messages'], 2)
        this.assertIn('python', stats['keywords'])

if __name__ == '__main__':
    unittest.main()