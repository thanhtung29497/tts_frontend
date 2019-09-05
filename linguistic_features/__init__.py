import numpy as np

dic_sign = [("À", "A", 1), ("Á", "A", 2), ("Ả", "A", 3), ("Ã", "A", 4), ("Ạ", "A", 5), ("Ầ", "Â", 1), ("Ấ", "Â", 2),
            ("Ẩ", "Â", 3), ("Ẫ", "Â", 4), ("Ậ", "Â", 5), ("Ằ", "Ă", 1), ("Ắ", "Ă", 2), ("Ẳ", "Ă", 3), ("Ẵ", "Ă", 4),
            ("Ặ", "Ă", 5), ("Ù", "U", 1), ("Ú", "U", 2), ("Ủ", "U", 3), ("Ũ", "U", 4), ("Ụ", "U", 5), ("Ừ", "Ư", 1),
            ("Ứ", "Ư", 2), ("Ử", "Ư", 3), ("Ữ", "Ư", 4), ("Ự", "Ư", 5), ("È", "E", 1), ("É", "E", 2), ("Ẻ", "E", 3),
            ("Ẽ", "E", 4), ("Ẹ", "E", 5), ("Ề", "Ê", 1), ("Ế", "Ê", 2), ("Ể", "Ê", 3), ("Ễ", "Ê", 4), ("Ệ", "Ê", 5),
            ("Ò", "O", 1), ("Ó", "O", 2), ("Ỏ", "O", 3), ("Õ", "O", 4), ("Ọ", "O", 5), ("Ồ", "Ô", 1), ("Ố", "Ô", 2),
            ("Ổ", "Ô", 3), ("Ỗ", "Ô", 4), ("Ộ", "Ô", 5), ("Ờ", "Ơ", 1), ("Ớ", "Ơ", 2), ("Ở", "Ơ", 3), ("Ỡ", "Ơ", 4),
            ("Ợ", "Ơ", 5), ("Ì", "I", 1), ("Í", "I", 2), ("Ỉ", "I", 3), ("Ĩ", "I", 4), ("Ị", "I", 5)]
dic_sign =  np.array(dic_sign)

dict_map_full = [['A', 'a'], ['Ă', 'aw'], ['Â', 'aa'], ['E', 'e'], ['Ê', 'ee'], ['I', 'i'], ['Y', 'i'], ['O', 'o'],
                 ['Ô', 'oo'], ['Ơ', 'ow'], ['U', 'u'], ['Ư', 'uw'], ['AI', 'ai'], ['AY', 'ay'], ['ÂY', 'aay'],
                 ['AO', 'ao'], ['AU', 'au'], ['ÂU', 'aau'], ['EO', 'eo'], ['ÊU', 'eu'], ['IA', 'ia'], ['IU', 'iu'],
                 ['IÊ', 'ie'], ['OA', 'oa'], ['OĂ', 'oaw'], ['OE', 'oe'], ['OI', 'oi'], ['ÔI', 'ooi'], ['ƠI', 'owi'],
                 ['UA', 'ua'], ['UÂ', 'uaw'], ['UÊ', 'ue'], ['UI', 'ui'], ['UÔ', 'uo'], ['UY', 'uy'], ['ƯA', 'uwa'],
                 ['ƯI', 'uwi'], ['ƯƠ', 'uow'], ['ƯU', 'uu'], ['IÊU', 'ieu'], ['YÊU', 'ieu'], ['OAI', 'oai'], ['OAY', 'oay'],
                 ['UÂY', 'uay'], ['UÔI', 'uoi'], ['ƯƠI', 'uowi'], ['ƯƠU', 'uou'], ['UYA', 'yua'], ['UYÊ', 'uye'], ['B', 'b'],
                 ['C', 'c'], ['K', 'c'], ['CH', 'ch'], ['TR', 'ch'], ['Đ', 'dd'], ['G', 'g'], ['H', 'h'],
                 ['KH', 'kh'], ['L', 'l'], ['N', 'n'], ['M', 'm'], ['NG', 'ng'], ['NGH', 'ng'], ['NH', 'nh'],
                 ['P', 'p'], ['Q', 'c'], ['PH', 'f'], ['T', 't'], ['TH', 'th'], ['V', '63'], ['X', 'x'],
                 ['S', 'x'], ['D', 'd'], ['GI', 'd'], ['R', 'd'], ['1', '1'], ['2', '2'], ['3', '3'],
                 ['4', '4'], ['5', '5'], ['.', 'dot'], [' ', '0']]

# dict_map_full = [['A', '0'], ['Ă', '1'], ['Â', '2'], ['E', '3'], ['Ê', '4'], ['I', '5'], ['Y', '5'], ['O', '6'],
#                  ['Ô', '7'], ['Ơ', '8'], ['U', '9'], ['Ư', '10'], ['AI', '11'], ['AY', '12'], ['ÂY', '13'],
#                  ['AO', '14'], ['AU', '15'], ['ÂU', '16'], ['EO', '17'], ['ÊU', '18'], ['IA', '19'], ['IU', '20'],
#                  ['IÊ', '21'], ['OA', '22'], ['OĂ', '23'], ['OE', '24'], ['OI', '25'], ['ÔI', '26'], ['ƠI', '27'],
#                  ['UA', '28'], ['UÂ', '29'], ['UÊ', '30'], ['UI', '31'], ['UÔ', '32'], ['UY', '33'], ['ƯA', '34'],
#                  ['ƯI', '35'], ['ƯƠ', '36'], ['ƯU', '37'], ['IÊU', '38'], ['YÊU', '38'], ['OAI', '39'], ['OAY', '40'],
#                  ['UÂY', '41'], ['UÔI', '42'], ['ƯƠI', '43'], ['ƯƠU', '44'], ['UYA', '45'], ['UYÊ', '46'], ['B', '47'],
#                  ['C', '48'], ['K', '48'], ['CH', '49'], ['TR', '49'], ['Đ', '50'], ['G', '51'], ['H', '52'],
#                  ['KH', '53'], ['L', '54'], ['N', '54'], ['M', '55'], ['NG', '56'], ['NGH', '56'], ['NH', '57'],
#                  ['P', '58'], ['KW', '59'], ['PH', '60'], ['T', '61'], ['TH', '62'], ['V', '63'], ['X', '64'],
#                  ['S', '64'], ['D', '65'], ['GI', '65'], ['R', '65'], ['1', '66'], ['2', '67'], ['3', '68'],
#                  ['4', '69'], ['5', '70'], ['.', '71'], [' ', '72']]

dict_map_full = np.array(dict_map_full)
dictionary_phoneme = dict_map_full


def clean_sign(label):
    l = []
    sign = '0'
    for char in label:
        if char == ' ' and sign != '0':
            l.append(sign)
            sign = '0'
        if char in dic_sign[:, 0]:
            idx = np.where(dic_sign[:, 0] == char)
            char, sign = dic_sign[idx][0][1], dic_sign[idx][0][2]

        l.append(char)
    if sign != '0':
        l.append(sign)
    return l


def encode_labels_phoneme(labels, lm=False):
    result = []
    max_length_label = 0
    for label in labels:
        label = clean_sign(label)
        encode = []
        start = 0
        for idx in range(len(label)):
            if idx <= start and idx != 0:
                continue
            # max of phoneme is 3
            start = idx
            for i in range(2, -1, -1):
                aa = label[start: start + i + 1]
                pho = ''.join(aa)
                if pho in dictionary_phoneme[:, 0]:
                    start = start + i
                    # print(pho)
                    iz = np.where(dictionary_phoneme[:, 0] == pho)[0][0]
                    encode.append(dictionary_phoneme[iz][1])
                    break
        # print(encode)
        integer_encoded = encode
        if max_length_label < len(integer_encoded):
            max_length_label = len(integer_encoded)
        result.append(np.array(integer_encoded))
        # print(encode)
    if not lm:
        for i in range(len(result)):
            result[i] = np.pad(result[i], (0, max(0, max_length_label - len(result[i]))), "constant",
                               constant_values=71)
        result = np.array(result)

    return result


def decode_label_to_char(label_encode):
    result = []
    for le in label_encode:
        indices = np.where(dict_map_full[:, 1] == str(le))[0]
        re = dict_map_full[indices]
        if len(re) > 1:
            # print(re)
            result.extend(['('] + list(re[:, 0]) + [')'])
        else:
            if re[:, 0] == '.':
                continue
            result.extend(re[:, 0])
    # print(result)
    return ''.join(result)

def is_tone(text):
    return "1" <= text <= "5"


def is_punctuation(text):
    return text == "0" or text == "dot"

def is_phoneme(text):
    return not (is_tone(text) or is_punctuation(text))


def create_label_phoneme(sentence):
    sentence = sentence.upper()
    labels = []
    null_value = "nul"
    word_id = 0
    phone_id = 1
    phonemes_queue = [null_value, null_value]
    all_phonemes = encode_labels_phoneme([sentence])
    phonemes_queue.extend(all_phonemes[0])
    phonemes_queue.extend([null_value, null_value])
    phonemes_queue = list(filter(lambda phone: is_phoneme(phone), phonemes_queue))
    print(phonemes_queue)

    for word in sentence.split():
        word_id = word_id + 1
        phonemes = encode_labels_phoneme([word])[0]
        tone = 0
        if is_tone(phonemes[-1]):
            tone = int(phonemes[-1])
            phonemes = np.delete(phonemes, -1, 0)

        for phoneme in phonemes:
            phone_id = phone_id + 1
            print(phoneme)
            prev_phone = phonemes_queue[phone_id - 1]
            # prev_prev_phone = phonemes_queue[phone_id - 2]
            next_phone = phonemes_queue[phone_id + 1]
            # next_next_phone = phonemes_queue[phone_id + 2]
            label = prev_phone + "-" + phoneme + "+" + next_phone + "@" + str(tone)
            labels.append(label)

    return labels


def main():
    test = "Đây là lần đầu tiên"
    label = create_label_phoneme(test)
    print(label)


if __name__ == "__main__":
    main()

