from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set a seed for reproducibility
DetectorFactory.seed = 0

# Language code to name mapping with more languages added
language_names = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'ru': 'Russian',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'mr': 'Marathi',
    'te': 'Telugu',
    'ta': 'Tamil',
    'ur': 'Urdu',
    'tr': 'Turkish',
    'nl': 'Dutch',
    'sv': 'Swedish',
    'fi': 'Finnish',
    'no': 'Norwegian',
    'da': 'Danish',
    'el': 'Greek',
    'he': 'Hebrew',
    'vi': 'Vietnamese',
    'th': 'Thai',
    'cs': 'Czech',
    'pl': 'Polish',
    'hu': 'Hungarian',
    'uk': 'Ukrainian',
    'ro': 'Romanian',
    'bg': 'Bulgarian',
    'sk': 'Slovak',
    'id': 'Indonesian',
    'ms': 'Malay',
    'fa': 'Persian',
    'sw': 'Swahili',
    'gu': 'Gujarati',
    'ml': 'Malayalam',
    'kn': 'Kannada',
    'si': 'Sinhala',
    'my': 'Burmese',
    'km': 'Khmer',
    'la': 'Latin'
}

def identify_language(text):
    try:
        language_code = detect(text)
        return language_names.get(language_code, language_code)  # Return full name if available, otherwise code
    except LangDetectException as e:
        return f"Language detection error: {str(e)}"

# Get input from the user
sentence = input("Enter a sentence with mixed languages: ")

# Split the sentence into segments based on spaces
segments = sentence.split(' ')

# Identify language for each segment
results = []
current_segment = []

for word in segments:
    current_segment.append(word)
    combined_text = ' '.join(current_segment)
    language = identify_language(combined_text)
    if language != "Language detection error: ":
        results.append(f"Segment: '{combined_text}' -> Language: {language}")
        current_segment = []

# Print results
for result in results:
    print(result)
