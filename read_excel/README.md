# 注意点
Windows か Mac でしか動作しない
venv を利用する際 Powershell の環境変数が上手くいかない場合があるので Gitbash で実行


# powershell venv
```
PowerShell Set-ExecutionPolicy RemoteSigned
```
python3 -m venv venv
```
windows環境なのでパスは Script フォルダでかつ Gitbash を利用するので、スクリプトは bash用の activate を利用
※linux だとパスは venv/bin/activate
```
source venv/Scripts/activate
```
venv\Scripts\activate.ps1
```
```
deactivate
```