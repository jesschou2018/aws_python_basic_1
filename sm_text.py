class sm_text:
    def __init__(self, input_txt):
        self.text = input_txt

    def clean_sm_text(self):
        # clean input and convert to list for # and @ extraction
        # punctiontoreplace=[',','.','/',';','|','}','{','[',']','!','$','%','^','&','*','(',')']
        clean_txt = self.text.replace(";", " ")
        lower_text = clean_txt.lower()
        all_words = lower_text.split()
        return all_words

    def extract_hashtags(self):
        clean_txt = self.text.replace(";", " ")
        lower_text = clean_txt.lower()
        all_words = lower_text.split()
        tag_locations = list(map(lambda x: x.find("#"), all_words))
        tag_list_loc = [i for i, e in enumerate(tag_locations) if e == 0]
        tag_values = [all_words[i] for i in tag_list_loc]
        return tag_values

    def extract_at_tags(self):
        clean_txt = self.text.replace(";", " ")
        lower_text = clean_txt.lower()
        all_words = lower_text.split()
        at_locations = list(map(lambda x: x.find("@"), all_words))
        at_list_loc = [i for i, e in enumerate(at_locations) if e == 0]
        at_values = [all_words[i] for i in at_list_loc]
        return at_values
