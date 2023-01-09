# 牛啤購物後端

## 環境設定

1. 請先安裝 [pipenv](https://github.com/pypa/pipenv#installation)
2. 安裝 [PostgreSQL](https://www.postgresql.org/download/)
3. 新增一個名為 niupi 的資料庫
4. 在專案目錄下新增一個 `.env` 檔，並在 `.env` 檔輸入以下內容（{} 不用打）
```env
ENV="development"
POSTGRESS_ADDRESS = "postgresql://{你的使用者名稱}@localhost:{運行 PostgreSQL 的 port，預設是 5432}/niupi"
```
5. 在專案目錄下開啟終端機並輸入
```bash
pipenv install --dev
```

6. 在專案目錄下新增 `.vscode` 目錄
7. 在 `.vscode` 目錄新增 `settings.json`，並貼上以下內容
```json
{
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=100",
        "--ignore=F401"
    ],
}
```

## Pipenv Script

有設定 3 個 Pipenv Script 幫助開發

### 執行後端程式

如果你想要執行後端程式，可以在終端機輸入
```bash
pipenv run dev
```

### 檢查 Coding Style

如果你想要執行 [flake8]() 檢查 Coding Style，可以在終端機輸入
```bash
pipenv run lint
```

### 執行測試

如果你想要執行測試，可以在終端機輸入
```bash
pipenv run tests
```
