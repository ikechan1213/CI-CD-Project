#  CI/CDパイプライン構築  (FastAPI × Docker × GitHub Actions)
 ## 概要
 このリポジトリは、FastAPIアプリケーションをDockerでコンテナ化し、  
 GitHub ActionsによるCI/CDパイプラインを構築するためのテンプレートです。  
 このテンプレートを使用することで、アプリ開発からテスト・ビルド・デプロイまでを自動化できます。
##  1.目的
手動で行っていたテスト・ビルド・デプロイ作業を自動化させ、開発効率の向上を目的としてCI/CD環境を構築すること。  
 　　　　　　　　↓  
 mainにコードpushでテスト・ビルド・デプロイを自動化させること。
 
## 2.工夫点
Dockerを用いて開発環境をコンテナ化し、環境差異による不具合を防止  
GitHub Actionsを使用することで、push時に自動でテストとビルドを実行するCI環境を構築

## 3.開発に至った経緯
開発をする上で、手動ビルドやテストに時間がかかることへの煩雑さからこのようなプロジェクトを作成しようと考えた。

 ## 4.技術スタック
 ・Backend：FastAPI(Python)  
 ・Container：Docker  
 ・CI/CD：GitHub Actions  
 ・その他：pytest

 ## 5.CI/CDの流れ
 コード修正  
 　　↓  
 git push  
 　　↓  
 GitHub Actions（テスト・ビルド）  
 　　↓  
 EC2へデプロイ  
 　　↓  
 アプリ反映

 ## 6.実装機能
・APIエンドポイント作成  
・Dockerによるコンテナ化  
・push時の自動テスト,自動デプロイ  
・Dockerイメージの自動ビルド

## 7.使用手順
①テンプレートからリポジトリ作成  
「Use this template」ボタンをクリックし、新しいリポジトリを作成してください。  

② Secretsの設定（必須）  
GitHubリポジトリの以下にアクセス：  
Settings → Secrets and variables → Actions  

以下のSecretsを登録してください：  

・EC2_HOST：EC2のパブリックIP  
・EC2_USER：ec2-user  
・EC2_KEY：.pemファイルの中身  

※ EC2のセキュリティグループで以下を許可してください。

・SSH（22番） → 自分のIP  
・HTTP（80番） → Anywhere（0.0.0.0/0）

③ EC2の事前準備  

Amazon EC2 上で以下を実施：  

## 　サーバにログイン

```
ssh -i "key.pem" ec2-user@<EC2のパブリックIPv4アドレス>
```

## 必要ツールのインストール

```
sudo dnf update -y
sudo dnf install docker -y git -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
```
## 権限設定
```
sudo usermod -aG docker ec2-user
```
※ 実行後は一度ログアウトして再ログインしてください。  

④ アプリの編集  

main.py を編集して、任意のAPIを作成してください。  

例：
```
@app.get("/")
def read_root():
    return {"message": "Hello World"}
```
⑤ デプロイ
## 初回デプロイ（初回のみ実施）
```
sudo dnf install git -y

git clone https://github.com/ユーザー名/リポジトリ名.git

cd リポジトリ名

docker build -t myapp .

docker run -d -p 80:8000 --name myapp myapp
```

※ 初回のみ、EC2上でアプリケーションを起動する必要があります。  
※ 既に `myapp` コンテナが存在する場合：  

```
docker stop myapp
docker rm myapp
```

実行後、再度 `docker run` を実行してください。  

---

### 2回目以降のデプロイ

コード修正後、以下を実行するだけで自動デプロイされます。

```bash
git add .
git commit -m "update"
git push
```
### 動作確認

ブラウザで以下へアクセスしてください：

```
http://<EC2のパブリックIPv4アドレス>
```
この例の通り実行した場合、  
`{"message":"Hello World"}` が表示されれば成功です。


## 8.使用上の注意点⚠️  
・　.pemファイルは絶対に公開しないこと  
・　セキュリティグループでポート80を開放すること  
・　Dockerコンテナ名やリポジトリ名が変更された場合、cd.ymlの修正が必要

## 9.今後の改善・修正案
・AWSへの完全自動デプロイ  
・Slack通知機能追加  

## 10.実行した結果・効果
手動で行っていたビルド・テスト作業を自動化し、作業時間を削減に成功。  
pushで処理が実行されるため、開発フローの効率化を実現された。  
環境依存の問題を排除し、再現性の高い開発環境を構築出来た。

## 11.最後に
このテンプレートは「開発基盤の再利用」を目的としています。  
プロジェクトごとに最小限の変更で、同じCI/CD環境を構築可能です。
