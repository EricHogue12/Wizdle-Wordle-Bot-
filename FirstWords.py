import random
import heapq

# class that generates an object containing the best five words in the tuple to use as the starting wordle word
class FirstWords:

    
    # creates FirstWord object which is one of the five best words to use
    def __init__(self, words):
        mylist = self.goodFirstWords(words)
        self.first = random.choice(mylist)
        
    # returns list of five best first words using the list returned by frequencies method
    def goodFirstWords(self, words: tuple):
        # list of frequencies
        freq1 = self.frequencies(words)

        # list of the five highest indices
        index1 = heapq.nlargest(5, range(len(freq1)), key=freq1.__getitem__)
        # the list of best words to return
        retWordList = []
        for i in range(5):
            retWordList.append(words[index1[i]])
        return retWordList



    # returns a list of total frequencies for each word
    def frequencies(self, words: tuple):
        # list 1 is list of letter frequencies for the 1st letter of wordle words
        # respectively works for list2, list3, list4, list5
        list1 = self.count_letters(words, 0)
        list2 = self.count_letters(words, 1)
        list3 = self.count_letters(words, 2)
        list4 = self.count_letters(words, 3)
        list5 = self.count_letters(words, 4)
        
        freqList = []

        for word in words:
            freq = 0
            for i in range(5):
                if i == 0:
                    if word[i] == 'a':
                        freq += list1[0]
                    if word[i] == 'b':
                        freq += list1[1]
                    if word[i] == 'c':
                        freq += list1[2]
                    if word[i] == 'd':
                        freq += list1[3]
                    if word[i] == 'e':
                        freq += list1[4]
                    if word[i] == 'f':
                        freq += list1[5]
                    if word[i] == 'g':
                        freq += list1[6]
                    if word[i] == 'h':
                        freq += list1[7]
                    if word[i] == 'i':
                        freq += list1[8]
                    if word[i] == 'j':
                        freq += list1[9]
                    if word[i] == 'k':
                        freq += list1[10]
                    if word[i] == 'l':
                        freq += list1[11]
                    if word[i] == 'm':
                        freq += list1[12]
                    if word[i] == 'n':
                        freq += list1[13]
                    if word[i] == 'o':
                        freq += list1[14]
                    if word[i] == 'p':
                        freq += list1[15]
                    if word[i] == 'q':
                        freq += list1[16]
                    if word[i] == 'r':
                        freq += list1[17]
                    if word[i] == 's':
                        freq += list1[18]
                    if word[i] == 't':
                        freq += list1[19]
                    if word[i] == 'u':
                        freq += list1[20]
                    if word[i] == 'v':
                        freq += list1[21]
                    if word[i] == 'w':
                        freq += list1[22]
                    if word[i] == 'x':
                        freq += list1[23]
                    if word[i] == 'y':
                        freq += list1[24]
                    if word[i] == 'z':
                        freq += list1[25]
                if i == 1:
                    if word[i] == 'a':
                        freq += list2[0]
                    if word[i] == 'b':
                        freq += list2[1]
                    if word[i] == 'c':
                        freq += list2[2]
                    if word[i] == 'd':
                        freq += list2[3]
                    if word[i] == 'e':
                        freq += list2[4]
                    if word[i] == 'f':
                        freq += list2[5]
                    if word[i] == 'g':
                        freq += list2[6]
                    if word[i] == 'h':
                        freq += list2[7]
                    if word[i] == 'i':
                        freq += list2[8]
                    if word[i] == 'j':
                        freq += list2[9]
                    if word[i] == 'k':
                        freq += list2[10]
                    if word[i] == 'l':
                        freq += list2[11]
                    if word[i] == 'm':
                        freq += list2[12]
                    if word[i] == 'n':
                        freq += list2[13]
                    if word[i] == 'o':
                        freq += list2[14]
                    if word[i] == 'p':
                        freq += list2[15]
                    if word[i] == 'q':
                        freq += list2[16]
                    if word[i] == 'r':
                        freq += list2[17]
                    if word[i] == 's':
                        freq += list2[18]
                    if word[i] == 't':
                        freq += list2[19]
                    if word[i] == 'u':
                        freq += list2[20]
                    if word[i] == 'v':
                        freq += list2[21]
                    if word[i] == 'w':
                        freq += list2[22]
                    if word[i] == 'x':
                        freq += list2[23]
                    if word[i] == 'y':
                        freq += list2[24]
                    if word[i] == 'z':
                        freq += list2[25]
                if i == 2:
                    if word[i] == 'a':
                        freq += list3[0]
                    if word[i] == 'b':
                        freq += list3[1]
                    if word[i] == 'c':
                        freq += list3[2]
                    if word[i] == 'd':
                        freq += list3[3]
                    if word[i] == 'e':
                        freq += list3[4]
                    if word[i] == 'f':
                        freq += list3[5]
                    if word[i] == 'g':
                        freq += list3[6]
                    if word[i] == 'h':
                        freq += list3[7]
                    if word[i] == 'i':
                        freq += list3[8]
                    if word[i] == 'j':
                        freq += list3[9]
                    if word[i] == 'k':
                        freq += list3[10]
                    if word[i] == 'l':
                        freq += list3[11]
                    if word[i] == 'm':
                        freq += list3[12]
                    if word[i] == 'n':
                        freq += list3[13]
                    if word[i] == 'o':
                        freq += list3[14]
                    if word[i] == 'p':
                        freq += list3[15]
                    if word[i] == 'q':
                        freq += list3[16]
                    if word[i] == 'r':
                        freq += list3[17]
                    if word[i] == 's':
                        freq += list3[18]
                    if word[i] == 't':
                        freq += list3[19]
                    if word[i] == 'u':
                        freq += list3[20]
                    if word[i] == 'v':
                        freq += list3[21]
                    if word[i] == 'w':
                        freq += list3[22]
                    if word[i] == 'x':
                        freq += list3[23]
                    if word[i] == 'y':
                        freq += list3[24]
                    if word[i] == 'z':
                        freq += list3[25]
                if i == 3:
                    if word[i] == 'a':
                        freq += list4[0]
                    if word[i] == 'b':
                        freq += list4[1]
                    if word[i] == 'c':
                        freq += list4[2]
                    if word[i] == 'd':
                        freq += list4[3]
                    if word[i] == 'e':
                        freq += list4[4]
                    if word[i] == 'f':
                        freq += list4[5]
                    if word[i] == 'g':
                        freq += list4[6]
                    if word[i] == 'h':
                        freq += list4[7]
                    if word[i] == 'i':
                        freq += list4[8]
                    if word[i] == 'j':
                        freq += list4[9]
                    if word[i] == 'k':
                        freq += list4[10]
                    if word[i] == 'l':
                        freq += list4[11]
                    if word[i] == 'm':
                        freq += list4[12]
                    if word[i] == 'n':
                        freq += list4[13]
                    if word[i] == 'o':
                        freq += list4[14]
                    if word[i] == 'p':
                        freq += list4[15]
                    if word[i] == 'q':
                        freq += list4[16]
                    if word[i] == 'r':
                        freq += list4[17]
                    if word[i] == 's':
                        freq += list4[18]
                    if word[i] == 't':
                        freq += list4[19]
                    if word[i] == 'u':
                        freq += list4[20]
                    if word[i] == 'v':
                        freq += list4[21]
                    if word[i] == 'w':
                        freq += list4[22]
                    if word[i] == 'x':
                        freq += list4[23]
                    if word[i] == 'y':
                        freq += list4[24]
                    if word[i] == 'z':
                        freq += list4[25]
                if i == 4:
                    if word[i] == 'a':
                        freq += list5[0]
                    if word[i] == 'b':
                        freq += list5[1]
                    if word[i] == 'c':
                        freq += list5[2]
                    if word[i] == 'd':
                        freq += list5[3]
                    if word[i] == 'e':
                        freq += list5[4]
                    if word[i] == 'f':
                        freq += list5[5]
                    if word[i] == 'g':
                        freq += list5[6]
                    if word[i] == 'h':
                        freq += list5[7]
                    if word[i] == 'i':
                        freq += list5[8]
                    if word[i] == 'j':
                        freq += list5[9]
                    if word[i] == 'k':
                        freq += list5[10]
                    if word[i] == 'l':
                        freq += list5[11]
                    if word[i] == 'm':
                        freq += list5[12]
                    if word[i] == 'n':
                        freq += list5[13]
                    if word[i] == 'o':
                        freq += list5[14]
                    if word[i] == 'p':
                        freq += list5[15]
                    if word[i] == 'q':
                        freq += list5[16]
                    if word[i] == 'r':
                        freq += list5[17]
                    if word[i] == 's':
                        freq += list5[18]
                    if word[i] == 't':
                        freq += list5[19]
                    if word[i] == 'u':
                        freq += list5[20]
                    if word[i] == 'v':
                        freq += list5[21]
                    if word[i] == 'w':
                        freq += list5[22]
                    if word[i] == 'x':
                        freq += list5[23]
                    if word[i] == 'y':
                        freq += list5[24]
                    if word[i] == 'z':
                        freq += list5[25]
            freqList.append(freq)

        return freqList

                    


                
    
    #returns list of letter frequencies for the ith position of wordle words (index 0 of list is how many times A occurs)
    def count_letters(self, words: tuple, i: int):
        acount = 0
        bcount = 0
        ccount = 0
        dcount = 0
        ecount = 0
        fcount = 0
        gcount = 0
        hcount = 0
        icount = 0
        jcount = 0
        kcount = 0
        lcount = 0
        mcount = 0
        ncount = 0
        ocount = 0
        pcount = 0
        qcount = 0
        rcount = 0
        scount = 0
        tcount = 0
        ucount = 0
        vcount = 0
        wcount = 0
        xcount = 0
        ycount = 0
        zcount = 0

        for word in words:
            if word[i] == 'a':
                acount+=1
            if word[i] == 'b':
                bcount+=1
            if word[i] == 'c':
                ccount+=1
            if word[i] == 'd':
                dcount+=1
            if word[i] == 'e':
                ecount+=1
            if word[i] == 'f':
                fcount+=1
            if word[i] == 'g':
                gcount+=1
            if word[i] == 'h':
                hcount+=1
            if word[i] == 'i':
                icount+=1
            if word[i] == 'j':
                jcount+=1
            if word[i] == 'k':
                kcount+=1
            if word[i] == 'l':
                lcount+=1
            if word[i] == 'm':
                mcount+=1
            if word[i] == 'n':
                ncount+=1
            if word[i] == 'o':
                ocount+=1
            if word[i] == 'p':
                pcount+=1
            if word[i] == 'q':
                qcount+=1
            if word[i] == 'r':
                rcount+=1
            if word[i] == 's':
                scount+=1
            if word[i] == 't':
                tcount+=1
            if word[i] == 'u':
                ucount+=1
            if word[i] == 'v':
                vcount+=1
            if word[i] == 'w':
                wcount+=1
            if word[i] == 'x':
                xcount+=1
            if word[i] == 'y':
                ycount+=1
            if word[i] == 'z':
                zcount+=1    
        return [acount, bcount, ccount, dcount, ecount, fcount, gcount, hcount, icount, jcount, kcount, lcount, mcount, ncount,
                ocount, pcount, qcount, rcount, scount, tcount, ucount, vcount, wcount, xcount, ycount, zcount]       

        