def single_root_words (root_world, *other_words) :
        root_world ='rich'
        same_words = []
        for word in other_words:
            if root_world in word:
                same_words.append(word)




        return same_words
print(single_root_words('rich', 'Arich'.lower(), 'richerd', 'aruricherton', 'dom', 'fricher', 'frICHER'.lower()))

