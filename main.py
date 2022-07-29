import random



class zipfAlgorithm():

    def __init__(self, loop):

        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '     
        ] # 50% chance letters, 50% chance spaces

        word, words, self.words_lenghts, self.decimals_percentage = list(), list(), list(), 4 # just initializing variables 
        self.lenghts_frequency, self.percentual_per_frequency, self.organized_percentuals, self.total_frequency = dict(), dict(), dict(), int()

        while len(words) < loop: # arg from a class call

            word.append(random.choice(letters))

            if word[-1] == letters[26]: 
                
                # if last item from word is ' ' (space), then remove ' ' it and append the list as a str to words
                word.remove(letters[26])

                if word == []:
                    # if word ends being a empty list, then continue the loop
                    continue 

                words.append(str().join(word))
                word = list() #  reinitializing word variable
        
        self.words = words
        #return self.words
    #   
    #
    #
    def statistics(self):

        for item in self.words:
            self.words_lenghts.append(len(item))

        for item in self.words_lenghts:

            if item not in self.lenghts_frequency:
                self.lenghts_frequency[item] = 1
            else:
                self.lenghts_frequency[item] += 1
        
        for item in self.lenghts_frequency:
            self.total_frequency += self.lenghts_frequency.get(item)
        
        percentual_per_singular_item = round(100 / self.total_frequency, self.decimals_percentage)

        for item in self.lenghts_frequency:
            self.percentual_per_frequency[item] = f'{round(self.lenghts_frequency[item]*percentual_per_singular_item, self.decimals_percentage)}%'
        
        for iterator in range(1, len(self.percentual_per_frequency)*2):
            try:
                if self.percentual_per_frequency.get(iterator) is not None:
                    self.organized_percentuals[iterator] = self.percentual_per_frequency.get(iterator)

            except KeyError:
                del self.organized_percentuals[iterator]
                continue
            
        return self.organized_percentuals




if __name__ == '__main__':
    probabilistic_shit = zipfAlgorithm(1000000)
    print(probabilistic_shit.statistics())
