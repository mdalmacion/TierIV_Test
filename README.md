# TierIV_Test: Assignment for TierIV Application

<b>PythonおよびSeleniumでTwitch.tvの「登録」リンクを検証するテスト</b>

<b>テスト条件</b>
- <b>必須なソフトエア、パッケージ</b>
  - Google Chrome、互換性しているChromedriver
  - Python　3以降
  - Selenium
  - PageFactory、Unittest、HTMLTestRunner
<br>

| ソース名  | テスト内容 | テスト手順 | 期待値 |
| ------------- | ------------- |------------- |------------- |
| TierIV_001.py  | 「ログイン」ボタンで登録ウインドウを開く |1.「Log In」ボタンをクリックする<br>2.「Don't have an account? Sign up」ボタンをクリックする<br>3.「Join Twitch today」というのポップアップウインドウが出ることを確認する |　「Join Twitch today」ポップアップウインドウが出ること |
| TierIV_002.py  | 「登録」ボタンを検証 |1.「Sign Up」ボタンをクリックする<br>2.「Join Twitch today」というのポップアップウインドウが出ることを確認する<br>3.Username、Passwordフィールドを入力する|1.Username,Passwordフィールドを入力できること<br>2.「Join Twitch today」というのポップアップウインドウが出ることを確認する  |
| TierIV.py  | TierIV_001、TierIV_002と同じ （Jenkins実行用）| - | - |
<br>

<b>Jenkinでの実施：必要な設定</b>
- Jenkins.warをCMDで実行する（java -jar jenkins.war）
- HTML Publisher pluginをインストールする
- Manage Jenkins > Manage Nodes > Settings > Script Console　でこのスクリプトを実実行する：System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
- Jenkins UIで新規システム変数を作成する：JAVA_TOOL_OPTIONS（変数名）、-Dfile.encoding=Shift-JIS -Dsun.jnu.encoding=Shift-JIS（変数値）
