class Encode:
    _trans_dict = {
        "آسان": "easy",
        "سخت": "difficult",
        "زیاد": "much",
        # # "متوسط": "avg
        "کم": "few",
        "بله": "yes",
        "خیر": "no",
        "بالا": "high",
        "پایین": "low",
        "سست": "weak",
        "متراکم": "strong",
        "دشت": "plain",
        "کوهستانی": "mountain",
        "تپه ماهور": "hill",
        "مدت دار": "long",
        "کوتاه مدت": "short",
    }

    _encode_dict = {
        "easy": 0,
        "difficult": 1,
        "much": 2,
        # "avg": 1,
        "few": 0,
        "yes": 1,
        "no": 0,
        "high": 1,
        "low": 0,
        "weak": 1,
        "strong": 0,
        "plain": 0,
        "mountain": 1,
        "hill": 2,
        "long": 0,
        "short": 1,
    }

    def translate_list(self, entry_list):
        """
        This convert entry_list (a list of persian words) to English.
        :param entry_list: List
        :return: List in English
        """
        translated_list = []
        for entry in entry_list:
            translated_list += [self._trans_dict[entry]]
        return translated_list

    def translate_word(self, word):
        return self._trans_dict[word]

    def encode_words(self, word_list):
        encoded_list = []
        for word in word_list:
            try:
                encoded_list += [self._encode_dict[word]]
            except KeyError:
                encoded_list += [word]

        return encoded_list

    def separate(self, entry_list: list):
        pass

    def convert(self, entry: str):
        """
        Encode the entry list for feeding to model.
        :type entry: list
        """
        pass
