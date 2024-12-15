import pandas as pd 

def merge(load_dt="20240724"):
    read_df = pd.read_parquet('~/tmp/test_parquet')
    cols = ['movieCd', #영화의 대표코드를 출력합니다.
       'movieNm', #영화명(국문)을 출력합니다.
       #'openDt', #영화의 개봉일을 출력합니다.
       #'audiCnt', #해당일의 관객수를 출력합니다.
       'load_dt', # 입수일자
       'multiMovieYn', #다양성영화 유무
       'repNationCd', #한국외국영화 유무
       ]
    df = read_df[cols]
    # 울버린 만조회 지우고 ...
    dw = df[(df['movieCd'] == '20235974') & (df['load_dt'] == int(load_dt))].copy() #날짜조건 load_dt 인자 받기 print(dw)

    # 카테고리 타입 -> Object
    dw['load_dt'] = dw['load_dt'].astype('object')
    dw['multiMovieYn'] = dw['multiMovieYn'].astype('object')
    dw['repNationCd'] = dw['repNationCd'].astype('object')

    # df[' x '].fillna(df[' x '].mode()[0],inplace=T
    dw['multiMovieYn']=dw['multiMovieYn'].fillna(dw['multiMovieYn'].mode()[0])
    dw['repNationCd']=dw['repNationCd'].fillna( dw['repNationCd'].mode()[0])
    print(dw)

    # 중복행 제거 
    dw_unique=dw.drop_duplicates()
    print(dw_unique)

