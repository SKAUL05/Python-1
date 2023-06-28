# Created by sarathkaul on 14/11/19


def remove_duplicates(sentence: str) -> str:
    """
    Reomove duplicates from sentence
    >>> remove_duplicates("Python is great and Java is also great")
    'Java Python also and great is'
    """
    sen_list = sentence.split(" ")
    check = set(sen_list)
    return " ".join(sorted(check))


if __name__ == "__main__":
    print(remove_duplicates("INPUT_SENTENCE"))
