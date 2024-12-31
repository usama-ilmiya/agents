import whisper

# from app.models.buckwalter_converter import arabic_to_buckwalter, normalize_arabic_text

model = whisper.load_model("medium", device="cpu")


def recognize_speech_whisper(file_path, target_word):
    """
    Recognize speech from an audio file and compare it with the target word.
    """
    result = model.transcribe(file_path, language="ar")
    recognized_text = result["text"].strip()

    # Normalize text
    normalized_recognized = normalize_arabic_text(recognized_text)
    normalized_target = normalize_arabic_text(target_word)

    # Convert to Buckwalter
    buck_recognized = arabic_to_buckwalter(normalized_recognized)
    buck_target = arabic_to_buckwalter(normalized_target)

    return buck_recognized, buck_target


def arabic_to_buckwalter(arabic_text):
    """
    Convert Arabic text to Buckwalter transliteration.
    """
    buck_map = {
        "ا": "A",
        "ب": "b",
        "ت": "t",
        "ث": "v",
        "ج": "j",
        "ح": "H",
        "خ": "x",
        "د": "d",
        "ذ": "*",
        "ر": "r",
        "ز": "z",
        "س": "s",
        "ش": "$",
        "ص": "S",
        "ض": "D",
        "ط": "T",
        "ظ": "Z",
        "ع": "E",
        "غ": "g",
        "ف": "f",
        "ق": "q",
        "ك": "k",
        "ل": "l",
        "م": "m",
        "ن": "n",
        "ه": "h",
        "و": "w",
        "ي": "y",
        "ء": "'",
        "ئ": "}",
        "ؤ": "&",
        "إ": "<",
        "أ": ">",
        "آ": "|",
        "ة": "p",
        "ى": "Y",
        "\u064e": "a",
        "\u064f": "u",
        "\u0650": "i",
        "\u064b": "F",
        "\u064c": "N",
        "\u064d": "K",
        "\u0651": "~",
        "\u0652": "o",
        " ": " ",
    }
    return "".join(buck_map.get(char, char) for char in arabic_text)


def normalize_arabic_text(text):
    """
    Normalize Arabic text by removing diacritics and standardizing characters.
    """
    diacritics = [
        "\u064e",
        "\u064f",
        "\u0650",
        "\u064b",
        "\u064c",
        "\u064d",
        "\u0651",
        "\u0652",
    ]
    for d in diacritics:
        text = text.replace(d, "")
    return text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").strip()
