import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ==========================================
# 1. 데이터 로드 및 전처리
# ==========================================
iris = load_iris() #사이킷런은 bunch 타입의 데이터를 전달한다 
print(type(iris))
print( iris.keys())
print( iris['target_names'])
print( iris['feature_names'])

feature_names =  iris['feature_names']

# DataFrame 변환 및 컬럼명 직관적으로 변경
df = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

df['target'] = iris.target
print(df.iloc[:15, :])

# 숫자로 된 타겟을 실제 꽃 이름 문자열로 매핑
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['target'].map(species_map)

print(df.iloc[:15, :])
# ==========================================
# 2. 텍스트 기반 요약 통계 출력
# ==========================================
print("=" * 60)
print(" [1] 데이터 기본 제원 (결측치 및 데이터 타입)")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print(" [2] 전체 데이터 요약 통계량")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print(" [3] 품종별 특징(Feature) 평균값 비교")
print("=" * 60)

#df.drop(columns='target') - target 필드는 제거
print(df.drop(columns='target').groupby('species').mean())
print("=" * 60)


# ==========================================
# 3. 데이터 시각화 (EDA)
# ==========================================
# 시각화 스타일 및 한글 깨짐 방지 설정
sns.set_theme(style="whitegrid")
plt.rc('font', family='Malgun Gothic') # Mac 사용 시 'AppleGothic'으로 변경
plt.rcParams['axes.unicode_minus'] = False


# [시각화 1] Pairplot (변수 간 상관관계 및 분포)- 필드의 개수가 많을 경우에는 사용불가 
sns.pairplot(df, hue='species', palette='Set2', diag_kind='kde')
plt.suptitle("Iris 데이터셋 변수 간 상관관계 및 분포", y=1.02)
plt.show()

# [시각화 2] Boxplot (품종별 특징 분포 및 이상치 확인)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for i, col in enumerate(features):  #features 배열의 인덱스와 요소를 가져온다 
    ax = axes[i // 2, i % 2] #축
    sns.boxplot(x='species', y=col, data=df, ax=ax, palette='pastel')
    ax.set_title(f'품종별 {col} 분포')
    ax.set_xlabel('품종')
    ax.set_ylabel('길이/너비 (cm)')

plt.tight_layout()
plt.show()

# # [시각화 3] Heatmap (수치형 변수 간 피어슨 상관계수)
# plt.figure(figsize=(8, 6))
# correlation_matrix = df[features].corr()
# sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r', vmin=-1, vmax=1, linewidths=0.5)
# plt.title("Iris 특징 변수 간 상관계수 행렬")
# plt.show()
