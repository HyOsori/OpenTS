
# coding: utf-8

# # base line script

# 1. anacoda를 설치
# 2. jupyter notebook 사용법을 익혀야함
# 3. pandas로 데이터 전처리에 대해 익혀야함
# 4. sci-kit learn lib을 통해 머신러닝 알고리즘 적용을 익혀야함
# 5. model tunning 과 validation을 이해하고 다시 3으로 돌아가서 반복적으로 실험을 할 수 있어야함

# In[113]:

import pandas as pd
import numpy as np


#
# ## load data

# In[114]:

file_num = 1
merged_df = None


# In[115]:

for each_file in range(file_num):
        df = pd.read_csv('%d_2016-11-14.csv' % each_file, index_col='date', parse_dates=['date'])
        if merged_df is None:
            merged_df = pd.DataFrame(columns=df.columns)
        df.sort_index(inplace=True)
        merged_df = pd.concat([merged_df, df])


# In[116]:

merged_df.head(3)


# In[ ]:




# * 같은 디렉토리내의 csv 파일을 pandas dataframe으로 가져온 것임
# * 보면 Unnamed와 같은 쓸모 없는 칼럼이 있음 드랍해줍시다

# In[117]:

merged_df.drop(['Unnamed: 0', 'shcode'], axis=1, inplace=True)


# In[118]:

merged_df.head(3)


# ## data preprocessing
# 1. 이제 데이터 전처리를 해야하는데 중간에 미싱데이터는 있는지 정규화를 할지 등등을 판단하고 처리해야합니다.
# 2. 위에서 한 정렬과 컬럼제거 작업도 전처리에 포홤됩니다.

# In[119]:

merged_df.info()


# * 전체 데이터가 3만개 정도 이고 널데이터는 없는 것을 알 수 있음
# * 무엇을 예측 해볼 것인가? 간단하게 sign(그날 오르고 내렸나를 값으로 가지고 있음 1:상한, 2:상승, 3:보합, 4:하한, 5:하락)을 예측해봅시다.
# * 현재 sign은 그날 당시를 표현하니 그 다음 날의 sign을 가지고 있다면 맞추고자 하는 레이블을 가지고 있다고 할수 있죠

# In[120]:

merged_df['y']=merged_df['sign'].shift(-1)


# In[121]:

merged_df[['sign','y']].tail(3)


# In[122]:

merged_df.dropna(inplace=True)


# In[123]:

merged_df[['sign','y']].tail(3)


# ## feature egineering
# 1. 여기가 결국은 모델의 성능 즉. 퍼포먼스와 직결되는 부분인데 아이디어가 필요합니다.
# 2. 예를 들어 위 데이터는 시계열기반의 데이터인데 시계열 특성을 나타내는 컬럼이 부족합니다. 어떻게 시계열을 반영할지 생각해야함

# ## modeling
# 1. 위에서 처리가 다 끝났으면 이제 학습을 시작해봅시다.
# 2. 데이터 특성에 기반해서 어떤 머신러닝 모델을 쓸지 판단할 수 있지만 결국은 실험을 해봐야함

# In[124]:

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.grid_search import GridSearchCV
from sklearn import svm

# In[130]:

features = merged_df.columns.drop(['y'])
print(features)
label = 'y'
train_X = merged_df[features]
train_y = merged_df[label]


# In[1]:

svc_param = {'C':np.logspace(-2,0,30), 'gamma':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]}


# In[127]:

gs_svc = GridSearchCV(svm.SVC(kernel='rbf'),svc_param,cv=5,n_jobs=4,verbose=1)


# In[128]:

gs_svc.fit(np.array(train_X),np.array(train_y))


# In[129]:

print (gs_svc.best_params_, gs_svc.best_score_)


# * 지금 하는 작업은 학습을 하면서 최적화된 파라미터를 구하는 과정입니다. 다 설명하기 넘나 귀찮 ㅠ 찾아보세요 무엇을 하는지
# * 위에보이는 는 cross-validation-value입니다. 이게 높으면 일반화된 좋은 모델이라는 뜻이죠 트레이닝 스코어는 어떻게 구할까요?
# * 모두 sklearn에 함수가 있습니다. 구해봐
# * 결국 cv값과 트레이닝값을 비교해서 어떻게 feature engineering을 할지 생각하고 반복해야합니다. feature engineering으로 돌아가세요
# * 참고로 학습된 모델을 사용하는 방법도 있는데 찾아보세요 ㅋㅋ

# In[ ]:

