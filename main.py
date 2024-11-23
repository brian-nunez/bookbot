def count_words(text):
    count = 0

    for word in text.split():
        count += 1

    return count


def count_characters(text):
    character_dict = {}

    for character in text:
        lower_character = character.lower()
        if lower_character in character_dict:
            character_dict[lower_character] += 1
        else:
            character_dict[lower_character] = 1

    return character_dict


def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def generate_report(word_count, character_count):
    report = "--- Begin report of books/frankenstein.txt ---"
    report += f"\n{word_count} words found in the document"
    report += "\n"

    for character, count in character_count:
        report += f"\nThe '{character}' character was found {count} times"

    report += "\n--- End report ---"

    return report


def dict_to_sorted_array(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def main(file_path):
    content = read_file(file_path)
    word_count = count_words(content)
    character_count = count_characters(content)
    sorted_character_count = dict_to_sorted_array(character_count)

    report = generate_report(word_count, sorted_character_count)

    print(report)


if __name__ == "__main__":
    main("./books/frankenstein.txt")
