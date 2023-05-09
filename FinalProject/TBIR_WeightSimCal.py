import math
def get_words():
    f = open("D:\\SUMMER_TERM2\\EIE3280\\PROJECT\\data3\\img_tags3.txt","r")
    flag = 0
    global all_word_lists                  #所有词的列表
    all_word_lists = []
    while flag <= 1000:
        line = f.readline()
        line = line[:-1]
        #print(line)
        flag += 1
        pos_dou = line.find(",")
        pos_dian = line.find("'")
        #print(pos_dian,pos_dou)
        word_list = []
        pos_kuo = line.find("]")
        while pos_dou != -1 :
            pos_dou = line.find(",")
            pos_dian = line.find("'")
            word = str(line[pos_dian + 1: pos_dou - 1])
            #print(word)
            word_list.append(word)
            line = line[pos_dou + 1 : pos_kuo + 1]
        all_word_lists.append(word_list)
    all_word_lists = all_word_lists[:-1]
    #print(all_word_lists)
    f.close()
    return all_word_lists
#print(get_words())
get_words()

def make_dictinary ():
    i = 0
    global all_word_dict
    global all_word_dict_ID
    all_word_dict = {}
    all_word_dict_ID = {}
    print('%-30s%-20s' %("words","IDS"))
    print('*'*50)
    while i<1000:
        for word in all_word_lists[i]:
            if word not in all_word_dict:
                all_word_dict[word] = 1
            else: all_word_dict[word] += 1
            all_word_dict_ID[word] = i + 1
        i+=1
    print(all_word_dict)
    #print(all_word_dict_ID)
    #for k in sorted(all_word_dict_ID):
    #    print('%-30s%-20s' %(k,all_word_dict_ID[k]))
    for p in sorted(all_word_dict):
        print('%-30s%-20s' %(p,all_word_dict[p]))
make_dictinary()

def Weight_cal(DocumentNumber):
    global weight_words                       #每一个单词的权重字典，已排序
    weight_words = {}
    pos = 0
    WeightVector = [0]*len(all_word_dict)
    for i in sorted(all_word_dict):
        df_t = all_word_dict[i]
        tf_td = 1
        weight_td =  tf_td * math.log(1000/df_t)
        weight_words[i] = weight_td
        Documentlist = all_word_lists[DocumentNumber]
        #print(i)
        if i in Documentlist: WeightVector[pos] = weight_td
        #print(pos)
        pos+=1
    # print(weight_words) 
    # print(WeightVector)
    # print(weight_words['orange']) 
    return WeightVector

#Weight_cal(1)
#print(Weight_cal(1))
#print(Weight_cal(2))

def Cos_Sim (Vector1 , Vector2):
    num = 0
    numerator = 0 
    denominator1 = 0 
    denominator2 = 0
    while num < len(Vector1):
        numerator += Vector1[num] * Vector2[num]
        denominator1 += Vector1[num] * Vector1[num]
        denominator2 += Vector2[num] * Vector2[num]
        num += 1
    #print(numerator,denominator1,denominator2)
    denominator = (denominator1**(1/2)) * (denominator2**(1/2)) 
    #print(denominator)
    if denominator == 0 : Similarity_V1_V2 = 0
    else: Similarity_V1_V2 = numerator/denominator
    return Similarity_V1_V2


#print(Cos_Sim(Weight_cal(1), Weight_cal(0)))
print('*********************************')

def Get_All_Sim(VectorNum):
    Allsim = []
    Sim_Dict = {}                #以首字母为序的相似度字典
    p=0
    for i in all_word_lists:
        Sim = Cos_Sim(Weight_cal(VectorNum),Weight_cal(p))
        #print(Sim)
        Allsim.append(Sim)
        Sim_Dict[p] = Sim
        p+=1
    #print(p)
    # print(Allsim)
    # print(Sim_Dict)                        
    sordic = sorted(Sim_Dict.items(),key = lambda item: item[1] )
    # print(sordic)                           #排序好的similarity与序号tuple的list
    return Allsim

Get_All_Sim(102)