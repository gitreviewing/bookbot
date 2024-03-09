def sort_on(dictio):
    return dictio['num']


def main():

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.lower().split()
       
        word_dict = {}
        for c in file_contents:
            lowered = c.lower()
            if lowered in word_dict:
                word_dict[lowered] += 1
            else:
                word_dict[lowered] = 1
        # print(word_dict)
        c_list =[]
        for c_entry in word_dict:
            s_dict = {}
            print(c_entry)
            s_dict["char"] = c_entry
            s_dict["num"] = word_dict[c_entry]
            c_list.append(s_dict)
        c_list.sort(reverse=True, key=sort_on)
        # print(c_list)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f'{len(words)} words found in the document')
        print("")
        for item in c_list:
            print(f"The {item['char']} character was found {item['num']} times")
            
            

        
main()