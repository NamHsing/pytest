from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np

def wordcloudplot(txt):
    path='d:/py/gb2312.ttf'
    path=unicode(path,'utf8')#.encode('gb2312')
    alice_mask = np.array(PIL.Image.open(r'd:\py\timg (2).jpg'))
    wordcloud = WordCloud(font_path=path) 
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('d:/py/out.jpg')
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
