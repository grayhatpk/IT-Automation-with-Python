freq={}
def checking(temp):
    for i in temp:
        if (i.isalpha()==False):
            index=temp.index(i)
            temp=temp.replace(temp[index],'')
    return temp
def generate():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    file=open('text.txt','r')
    line=file.read()

    while line!='':
    
        line=line.lower()
    
        word=line.split()
    
        for temp in word:
        
            while(temp.isalpha()==False):
                 temp=checking(temp)   
         
            if (not(temp in uninteresting_words)):    
                if temp in freq:
                    freq[temp]+=1
                else:
                    freq[temp]=1
            
    
        line=file.read()

    file.close()

def main():

    generate()
    print(freq)
   
main()
