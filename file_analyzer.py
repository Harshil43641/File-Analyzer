import sys
import re
import collections

# Define a minimal set of stop words to ignore
STOP_WORDS = {'the', 'is', 'and', 'a' , 'an', 'to', 'of' , 'in'}

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Extract words (convert to lower-case for uniformity)
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    
    # Calculate average word length
    total_characters = sum(len(word) for word in words)
    avg_word_length = total_characters / total_words if total_words > 0 else 0

    # Count sentences by splitting on common sentence-ending punctuation.
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings that may result from split
    sentences = [s for s in sentences if s.strip()]
    total_sentences = len(sentences)
    
    # Filter out stop words for frequency analysis.
    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_counts = collections.Counter(filtered_words)
    top_5 = word_counts.most_common(5)

    # Output the summary report.
    print("File Analysis Report")
    print("====================")
    print(f"Total number of words: {total_words}")
    print("Top 5 most frequent words (excluding stop words):")
    for word, count in top_5:
        print(f"  {word}: {count}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Number of sentences: {total_sentences}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python file_analyzer.py <path_to_txt_file>")
    else:
        analyze_file(sys.argv[1])
