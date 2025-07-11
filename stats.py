def get_num_words(text):
     my_list = text.split()
     return len(my_list)

def count_char(text):
     my_dict = {}
     text = text.lower()
     for char in text:
          if char not in my_dict:
               my_dict[char] = 1
          else:
               my_dict[char] += 1
     return my_dict

def sort_on(items):
    return items["num"]

def sort_dict(my_dict):
    new_list = []
    for key, value in my_dict.items():
        new_dict = {}
        if key.isalpha():
            new_dict["char"] = key
            new_dict["num"] = value
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list