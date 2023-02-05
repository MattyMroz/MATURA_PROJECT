def compress_list(lst):
    seen = {}
    result = []
    for sublist in lst:
        new_sublist = []
        for i, word in enumerate(sublist):
            if i in seen and word == seen[i]:
                new_sublist.append("-")
            else:
                new_sublist.append(word)
                seen[i] = word
        result.append(new_sublist)
    return result

names = [['algorytm'], ['algorytm', 'iteracyjny'], ['algorytm', 'naiwny'], ['algorytm', 'obliczania', 'silni'], ['algorytm', 'obliczania', 'silni', 'iteracyjny'], ['algorytm', 'obliczania', 'silni', 'rekurencyjny'], ['algorytm', 'rekurencyjny'], ['algorytm', 'sortowania', 'przez', 'prosta', 'zamiane'], ['algorytm', 'sortowania', 'przez', 'wstawianie'], ['algorytm', 'sortowania', 'przez', 'wybieranie']]

result = compress_list(names)
print(result)
