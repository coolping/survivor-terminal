import os
import re
import json

# 設定你的日誌資料夾名稱與輸出的 JSON 檔名
LOGS_DIR = 'logs'
OUTPUT_FILE = 'logs.json'

def scan_and_generate():
    print("===================================================")
    print("[SYS] INITIATING RADAR SCAN...")
    print("===================================================\n")
    
    logs_data = []

    # 確認資料夾是否存在
    if not os.path.exists(LOGS_DIR):
        print(f"[ERROR] 找不到 '{LOGS_DIR}' 資料夾！請確認目錄結構。")
        return

    # 掃描資料夾內的 .md 檔案
    files = [f for f in os.listdir(LOGS_DIR) if f.endswith('.md')]
    
    if not files:
        print(f"[WARN] 在 '{LOGS_DIR}' 中沒有發現任何 .md 日誌檔。")
    
    for filename in files:
        # 使用正規表達式抓取檔名中的 YYYY-MM-DD
        match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
        date_str = match.group(1) if match else "1999-12-31" # 找不到日期就給個預設舊日期
        
        logs_data.append({
            "filename": filename,
            "date": date_str
        })
        print(f"  -> 發現訊號: {filename} (日期: {date_str})")

    # 依照日期由新到舊排序 (reverse=True)
    logs_data.sort(key=lambda x: x['date'], reverse=True)

    # 將結果寫入 logs.json
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 確保中文不會變成亂碼，indent=2 讓 JSON 格式排版整齊
        json.dump(logs_data, f, ensure_ascii=False, indent=2)
        
    print("\n===================================================")
    print(f"[SYS] 掃描完成！共記錄 {len(logs_data)} 筆生存日誌。")
    print(f"[SYS] 檔案 '{OUTPUT_FILE}' 已成功更新。")
    print("===================================================")

if __name__ == '__main__':
    scan_and_generate()