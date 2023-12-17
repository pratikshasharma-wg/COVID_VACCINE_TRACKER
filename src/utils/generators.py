def list_generator(lst):
    length = len(lst)
    index = 0
    page = 1
    counter = 0
    data = []
    while index < length and counter < 5:
        data.append(lst[index])
        counter += 1
        index += 1
        if counter > 5 or index == length:
            print(f"------Page: {page}------", "\n")
            page += 1
            print(data)
            yield data
            data = []
            counter = 0

