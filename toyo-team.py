#!/usr/bin/env python3
"""
Toyo Security AI Team - CrewAI Demo (Ollama)
為 Toyo Security 創建的 AI 員工團隊
使用 Ollama API
"""

import os

# 配置 Ollama API
os.environ['OPENAI_API_KEY'] = '24eb99cd231348d28cab9f2f6c5fe656.y3hVb_bR0H8eNh4IUKmX9sSh'
os.environ['OPENAI_API_BASE'] = 'http://ollama.com/v1'

from crewai import Agent, Task, Crew, Process
from datetime import datetime
import json

print("=" * 60)
print("🤖 Toyo Security AI Team - CrewAI Demo (Ollama)")
print("=" * 60)
print()

# ========== 創建團隊成員 ==========

# 1. CEO
ceo = Agent(
    role='Chief Executive Officer (CEO)',
    goal='制定公司戰略決策，優化保安服務質量',
    backstory='''你係 Toyo Security 嘅 CEO，有 20 年保安行業經驗。
你擅長制定戰略決策，提升服務質量同客戶滿意度。
你關注 GPS Check-in 系統嘅數據，用嚟優化人手部署同服務流程。''',
    verbose=True,
    allow_delegation=False,
)

# 2. 保安主管
security_chief = Agent(
    role='Security Operations Chief',
    goal='優化保安巡邏流程，確保員工工作效率',
    backstory='''你係 Toyo Security 嘅保安主管，負責管理外勤保安員。
你擅長分析 GPS Check-in 數據，發現巡邏路線問題。
你關注員工嘅出勤情況同工作表現。''',
    verbose=True,
    allow_delegation=True,
)

# 3. 數據分析師
data_analyst = Agent(
    role='Data Analyst',
    goal='分析 GPS Check-in 數據，提供洞察建議',
    backstory='''你係 Toyo Security 嘅數據分析師，擅長從數據中發現趨勢。
你負責分析員工打卡記錄，找出異常模式。
你提供數據驅動嘅建議，幫助管理層決策。''',
    verbose=True,
    allow_delegation=True,
)

# 4. 客服經理
customer_service = Agent(
    role='Customer Service Manager',
    goal='處理客戶查詢，提升客戶滿意度',
    backstory='''你係 Toyo Security 嘅客服經理，負責同客戶溝通。
你根據 GPS Check-in 數據回應客戶查詢。
你確保客戶對保安服務滿意。''',
    verbose=True,
    allow_delegation=True,
)

# 5. 文書秘書
secretary = Agent(
    role='Executive Secretary',
    goal='撰寫專業報告，整理會議記錄',
    backstory='''你係 Toyo Security 嘅行政秘書，負責文書工作。
你擅長撰寫專業報告，整理數據同建議。
你確保報告格式正確，語言清晰。''',
    verbose=True,
    allow_delegation=False,
)

# ========== 創建任務 ==========

# 任務 1: 數據分析
task_analysis = Task(
    description='''
分析以下 GPS Check-in 數據（2026 年 4 月）：

員工打卡記錄：
- John Chan: 出勤率 98%, 平均打卡時間 08:55, 異常 0 次
- Mary Wong: 出勤率 95%, 平均打卡時間 09:02, 異常 1 次 (遲到)
- Peter Lee: 出勤率 92%, 平均打卡時間 08:58, 異常 2 次 (早退)
- Sarah Lau: 出勤率 100%, 平均打卡時間 08:50, 異常 0 次
- David Ip: 出勤率 88%, 平均打卡時間 09:10, 異常 3 次 (遲到 + 早退)

請找出：
1. 出勤率最高同最低嘅員工
2. 常見異常類型
3. 建議改善措施
''',
    expected_output='''數據分析報告，包含：
- 出勤率統計
- 異常類型分佈
- 3 個具體改善建議''',
    agent=data_analyst,
)

# 任務 2: 保安流程優化
task_security = Task(
    description='''
根據數據分析結果，優化保安巡邏流程：

現況：
- 5 名保安員負責 3 個大廈
- 每棟大廈需要 2 小時巡邏一次
- 部分員工有遲到/早退問題

請制定：
1. 新嘅巡邏路線安排
2. 人手調配建議
3. 考勤管理改進措施
''',
    expected_output='''保安流程優化方案，包含：
- 新巡邏路線圖
- 人手調配表
- 考勤管理建議''',
    agent=security_chief,
)

# 任務 3: 客戶回應模板
task_customer = Task(
    description='''
準備客戶查詢回應模板：

常見查詢：
1. 「點解我大廈嘅保安員有時唔見人？」
2. 「可唔可以提供月度巡邏報告？」
3. 「點樣確保保安員按時巡邏？」

請撰寫專業回應，並說明 GPS Check-in 系統點樣解決呢啲問題。
''',
    expected_output='''客戶回應模板，包含：
- 3 個查詢嘅專業回應
- GPS 系統優勢說明
- 客戶信心建立話術''',
    agent=customer_service,
)

# 任務 4: 月度報告
task_report = Task(
    description='''
整合以上所有分析同建議，撰寫《Toyo Security 月度保安報告》（2026 年 4 月）

報告結構：
1. 執行摘要 (1 段)
2. GPS Check-in 數據分析
3. 保安流程優化建議
4. 客戶服務改進措施
5. 下月行動計劃

請用專業格式，包括標題、子標題、要點列表。
''',
    expected_output='''完整月度報告 (800-1000 字)，包含：
- 執行摘要
- 數據分析結果
- 優化建議
- 行動計劃''',
    agent=secretary,
)

# ========== 創建團隊 ==========

print("📋 創建 AI 團隊...")
print()

crew = Crew(
    agents=[ceo, security_chief, data_analyst, customer_service, secretary],
    tasks=[task_analysis, task_security, task_customer, task_report],
    verbose=True,
    process=Process.sequential,  # 順序執行
)

# ========== 執行任務 ==========

print("🚀 開始執行任務...\n")
print("=" * 60)
print()

result = crew.kickoff()

print()
print("=" * 60)
print("✅ 任務完成！")
print("=" * 60)
print()
print("📄 最終報告：")
print()
print(result)

# 保存報告
with open('monthly-report.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))

print()
print("💾 報告已保存到：monthly-report.txt")
print()
print("🎉 Toyo Security AI Team Demo 完成！")
