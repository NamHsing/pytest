from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

def wordcloudplot(txt):
    path='d:/jieba/msyh.ttf'
    path=unicode(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open(r'd:\py\timg (2).jpg'))
    wordcloud = WordCloud(font_path=path, 
                          background_color="white",   
                          margin=5, width=1800, height=800,mask=alice_mask,max_words=2000,max_font_size=60,random_state=42) 
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('d:/py/she2.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
def main():
    a=[]
    f=open(r'D:\py\a.txt','r').read()
    words=list(jieba.cut(f))
    for word in words:
        if len(word)>1:
            a.append(word)
    txt=r' '.join(a)
    wordcloudplot(txt)
    
if __name__=='__main__':
    main()
