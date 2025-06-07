import os
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize NLTK resources (downloads punkt and stopwords)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class ChatLogSummarizer:
    def __init__(self, use_tfidf=False):
        self.use_tfidf = use_tfidf
        self.stop_words = set(stopwords.words('english'))

    def parse_chat(self, file_path):
        """Parse chat log file into user and AI messages."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        
        user_msgs, ai_msgs = [], []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("User:"):
                    user_msgs.append(line[5:].strip())
                elif line.startswith("AI:"):
                    ai_msgs.append(line[3:].strip())
        return user_msgs, ai_msgs

    def clean_text(self, text):
        """Clean text by removing punctuation and converting to lowercase."""
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        return [token for token in tokens if token not in self.stop_words and token.isalpha()]

    def get_top_keywords(self, messages, top_n=5):
        """Extract top N keywords using frequency or TF-IDF."""
        if not messages:
            return []
        
        if self.use_tfidf:
            vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
            tfidf_matrix = vectorizer.fit_transform(messages)
            return vectorizer.get_feature_names_out().tolist()
        else:
            all_words = []
            for message in messages:
                all_words.extend(self.clean_text(message))
            return [word for word, _ in Counter(all_words).most_common(top_n)]

    def analyze_chat(self, user_msgs, ai_msgs):
        """Analyze messages and extract statistics."""
        total_msgs = len(user_msgs) + len(ai_msgs)
        user_count = len(user_msgs)
        ai_count = len(ai_msgs)
        keywords = self.get_top_keywords(user_msgs + ai_msgs)
        return {
            'total_messages': total_msgs,
            'user_messages': user_count,
            'ai_messages': ai_count,
            'keywords': keywords
        }

    def generate_summary(self, stats, output_path=None):
        """Generate and optionally save a summary."""
        summary = (
            "Chat Log Summary:\n"
            f"- Total exchanges: {stats['total_messages']}\n"
            f"- User messages: {stats['user_messages']}\n"
            f"- AI messages: {stats['ai_messages']}\n"
            f"- Main topics discussed: {', '.join(stats['keywords'])}\n"
            f"- Top keywords: {', '.join(stats['keywords'])}\n"
        )
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary)
        return summary

    def process_folder(self, folder_path, output_dir):
        """Process all .txt files in a folder."""
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder {folder_path} not found.")
        
        summaries = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                user_msgs, ai_msgs = self.parse_chat(file_path)
                stats = self.analyze_chat(user_msgs, ai_msgs)
                output_path = os.path.join(output_dir, f"summary_{filename}")
                summary = self.generate_summary(stats, output_path)
                summaries.append((filename, summary))
        return summaries

if __name__ == "__main__":
    summarizer = ChatLogSummarizer(use_tfidf=True)
    user_msgs, ai_msgs = summarizer.parse_chat("data/sample_chat_1.txt")
    stats = summarizer.analyze_chat(user_msgs, ai_msgs)
    summary = summarizer.generate_summary(stats, "output/summary_1.txt")
    print(summary)