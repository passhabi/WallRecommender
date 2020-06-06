import re
import numpy as np
import math


def check_dim(testlist, dim=0):
    # deprecated.
    """tests if testlist is a list and how many dimensions it has
    returns -1 if it is no list at all, 0 if list is empty
    and otherwise the dimensions of it"""
    if isinstance(testlist, list):
        if testlist == []:
            return dim
        dim = dim + 1
        dim = check_dim(testlist[0], dim)
        return dim
    else:
        if dim == 0:
            return -1
        else:
            if type(testlist) == np.ndarray:
                return dim + testlist.ndim  # its array then.
            else:
                return dim


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

    _wall_decode_dict = {
        1: " پیش ساخته",
        2: "درجاریز",
        3: "سیم خاردار",
        4: "بدون حفاظ",
    }

    # wall name patterns:
    _walls_pattern = [
        "_",  # number zero #
        "[پب][یب]?ش[ ‌]*[سش]اخا?ته",  # 1 pre cast wall - پیش ساخته
        "در[ ‌]?جا[ ‌]*(ر[یب]ز)?",  # 2 retaining wall - درجاریز
        "س[یب]م[ ‌]*خاردار|[فق]نس",  # 3 barbed wire - سیم خاردار و فنس
        "بدون[ ‌]*[جحخ][فق]ا[طظ]|بدون[ ‌]*م[جحخ]ا[فق][طظ]|م[جحخ]ا[فق][طظ]ت[ ‌]*ن[سش]ده?"  # 4 non_protection - بدون حفاظ
    ]

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

    def encode_words(self, word_list, non_english=True):
        """
        Get a list of wall names and convert them to numbers.
        Note: if the words are in english language set non_english to False.
        return the encoded list (numbers)
        """
        # careful: uncomment it.
        # if non_english:
        #     word_list = self.translate_list(word_list)  # call by value.

        encoded_list = []
        for word in word_list:
            try:
                encoded_list += [self._encode_dict[word]]
            except KeyError:
                encoded_list += [word]  # dont change it.

        return encoded_list

    def separate(self, entry_list: list):
        pass

    def decode_wall_name(self, number: int):
        """
        Encode the Integer
        :type number: int
        """
        return self._wall_decode_dict[number]

    def encode_walls_name(self, polls):
        """
        Change the non_english wall names to it's corresponding numbers. (inplace)
        return: None

        Notes:

            it handles one dimensional arrays too.
        """

        if polls.ndim == 1:
            polls = [polls]  # handle one dimensional list.

        file_number = 0
        for poll in polls:
            for i in range(len(poll)):
                # for each wall name in input list, check which pattern covers that:
                for j, pattern in enumerate(self._walls_pattern):
                    if re.search(pattern, str(poll[i])) is not None:  # if the wall name is covered by this pattern:
                        poll[i] = j  # replaced with index pattern (which is corresponding to the wall names).
                        # its a call by reference. changing the entity of the list.
                        break
                else:
                    if 'nan' != str(poll[i]):
                        print(
                            "\033[91m" + f"Warning!! value '{poll[i]}' {type(poll[i])} in row {i} of"
                                         f"the file {file_number} has been compromised." + "\033[0m")
                        # todo: warnings?
                    poll[i] = np.nan
            file_number += 1
