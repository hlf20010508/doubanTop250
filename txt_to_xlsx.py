import pandas as pd

file=open('doubanTop250/top250.txt','r',encoding='utf8')

df=pd.DataFrame(columns=['movie','director','brief','score','comment','quote'])

for i in range(250):
    movie=file.readline()
    director=file.readline()
    brief=file.readline()
    score=file.readline()
    comment=file.readline()
    quote=file.readline()

    line={
        'movie': movie,
        'director': director,
        'brief': brief,
        'score': float(score),
        'comment': int(comment),
        'quote': quote
    }

    df=df.append(line,ignore_index=True)

file.close()

df.to_excel('top250.xlsx',index=False)
