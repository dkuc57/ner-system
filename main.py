import spacy


def ner_system(input_string, language_code):
    """
    A multi-language NER system based on spaCy library.
    :param input_string: string with text
    :param language_code: language code
    :return: a list of entities, each entity is a dictionary with fields: text, type, start_pos, end_post
    """
    NER = spacy.load(language_code)
    text = NER(input_string)
    output = [{'text': word.text, 'type': word.label_, 'start_pos': word.start, 'end_pos': word.end} for word in
              text.ents]
    return output


if __name__ == '__main__':
    # text = ''
    # language = 'en_core_web_sm'
    text = input('Pass string with text')
    language = input('Pass language code')
    ner_system(text, language)
