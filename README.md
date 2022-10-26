# 牛啤購物後端

## 開發規則與流程

- [開發規則](https://github.com/gacky1601/niupi-backend/wiki/%E9%96%8B%E7%99%BC%E8%A6%8F%E5%89%87)
- [開發流程](https://github.com/gacky1601/niupi-backend/wiki/%E9%96%8B%E7%99%BC%E6%B5%81%E7%A8%8B)

## 環境設定

1. 請先安裝 [pipenv](https://github.com/pypa/pipenv#installation)
2. 在專案目錄下開啟終端機並輸入
```bash
pipenv install --dev
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
