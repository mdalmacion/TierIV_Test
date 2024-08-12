# TierIV_Test: Assignment for TierIV Application

<b>Twitch.tvの「登録」リンクを検証するテスト</b>

<b>テスト条件</b>
- <b>必須なソフトエア、パッケージ</b>
  - Google Chrome、互換性しているChromedriver
  - Python　3以降
  - Selenium
  - PageFactory、Unittest
<br>

| ソース名  | テスト内容 | テスト手順 | 期待値 |
| ------------- | ------------- |------------- |------------- |
| TierIV_001.py  | 「ログイン」ボタンで登録ウインドウを開く |1.「Log In」ボタンをクリックする<br>2.「Don't have an account? Sign up」ボタンをクリックする<br>3.「Join Twitch today」というのポップアップウインドウが出ることを確認する |　「Join Twitch today」ポップアップウインドウが出ること |
| TierIV_002.py  | 「登録」ボタンを検証 |1.「Sign Up」ボタンをクリックする<br>2.「Join Twitch today」というのポップアップウインドウが出ることを確認する<br>3.Username、Passwordフィールドを入力する|1.Username,Passwordフィールドを入力できること<br>2.「Join Twitch today」というのポップアップウインドウが出ることを確認する  |
