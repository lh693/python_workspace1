#conda install -c conda-forge plotly -y
import plotly.express as px

# Plotly 내장 데이터셋(iris) 불러오기
df = px.data.iris()

# 산점도 그리기
fig = px.scatter(
    df, 
    x="sepal_width", 
    y="sepal_length", 
    color="species",       # 그룹별 색상 지정 (범례 클릭 시 필터링 가능)
    size="petal_length",    # 데이터 크기 반영
    hover_data=['petal_width'], # 마우스 오버 시 추가로 보여줄 데이터
    title="Iris 데이터셋 인터렉티브 산점도"
)

# 차트 출력
fig.show()
