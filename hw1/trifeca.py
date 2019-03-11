
def trifeca(word):
    if len(word)<6:
        return False
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                print(f'Word contains 3 consecutive double letters')
                return True
    
    print(f'Word does not contain 3 consecutive double letters')   
    return False
    
if __name__ == '__main__':
    word='aabbcc'
    trifeca(word)
   