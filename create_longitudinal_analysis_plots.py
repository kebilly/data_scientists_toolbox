import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 透過 matplotlib 的子圖功能將三個年份
# 的長條圖合併在一個畫布上
# ncol=3 : 要有三個水平排列的軸物件
# figsize=(32, 8) : 指定畫布的長與寬

def plot_horizontal_bars(sql_query: str, fig_name: str, shareyaxis: bool=False):
    connection = sqlite3.connect("data/kaggle_survey.db")
    response_counts = pd.read_sql(sql_query, con=connection)
    connection.close()
    fig, axes = plt.subplots(ncols=3, figsize=(32, 8), sharey=shareyaxis)
    survey_years = [2020, 2021, 2022]
    for i in range(len(survey_years)):
        survey_year = survey_years[i]
        response_counts_year = response_counts[response_counts["surveyed_in"] == survey_year]
        y = response_counts_year["response"].values
        width = response_counts_year["response_count"].values
        axes[i].barh(y ,width)
        axes[i].set_title(f"{survey_year}")
    plt.tight_layout()
    fig.savefig(f"{fig_name}.png")

# 從 aggregated_responses 檢視表中查詢
# 對應年份、題號的資料
# Select the title most similar to your current role.
# 2020: Q5
# 2021: Q5
# 2022: Q23
#從事資料科學工作的職缺抬頭（title）有哪些？
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
WHERE (question_index = 'Q5' AND surveyed_in IN (2020, 2021)) OR
      (question_index = 'Q23' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""

plot_horizontal_bars(sql_query, "data_science_job_titles")

#============================================================================
#從事資料科學工作的日常內容是什麼？
sql_query2 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q23' AND surveyed_in = 2020) OR
      (question_index = 'Q24' AND surveyed_in = 2021) OR
      (question_index = 'Q28' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
plot_horizontal_bars(sql_query2, "data_science_job_tasks", shareyaxis=True)

#============================================================================
#想要從事資料科學工作，需要具備哪些技能與知識？（程式語言）
sql_query3 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q7' AND surveyed_in IN (2020, 2021)) OR
      (question_index = 'Q12' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
plot_horizontal_bars(sql_query3, "data_science_job_programming_languages")

#============================================================================
#想要從事資料科學工作，需要具備哪些技能與知識？（資料庫）
sql_query4 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q29A' AND surveyed_in = 2020) OR
      (question_index = 'Q32A' AND surveyed_in = 2021) OR
      (question_index = 'Q35' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
plot_horizontal_bars(sql_query4, "data_science_job_databases")

#============================================================================
#想要從事資料科學工作，需要具備哪些技能與知識？（視覺化）
sql_query5 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q14' AND surveyed_in IN (2020, 2021)) OR
      (question_index = 'Q15' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
plot_horizontal_bars(sql_query5, "data_science_job_visualizations")

#============================================================================
#想要從事資料科學工作，需要具備哪些技能與知識？（機器學習）
sql_query6 = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
FROM aggregated_responses
WHERE (question_index = 'Q17' AND surveyed_in IN (2020, 2021)) OR
      (question_index = 'Q18' AND surveyed_in = 2022)
ORDER BY surveyed_in,response_count;
"""
plot_horizontal_bars(sql_query6, "data_science_job_machine_learnings")

