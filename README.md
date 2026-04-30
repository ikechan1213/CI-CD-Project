#  CI/CDパイプライン構築  (FastAPI × Docker × GitHub Actions)
##  1.目的
手動で行っていたテスト・ビルド・デプロイ作業を自動化させ、開発効率の向上を目的としてCI/CD環境を構築すること。  
 　　　　　　　　↓  
 コードpushでテスト・ビルドを自動化させること。
 
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

 ## 5.システムの構成
 User → GitHub push  
 　　　↓  
 GitHub Actions  
 　↓　　　　　↓  
 Test　　　Build(Docker)  
　　　　　　　↓  
　　　　　　deploy

 ## 6.実装機能
・APIエンドポイント作成  
・Dockerによるコンテナ化  
・push時の自動テスト  
・Dockerイメージの自動ビルド

## 7.実行方法
```
git clone https://github.com/ユーザー名/リポジトリ名.git
cd myapp
docker build -t myapp .
docker run -p 8000:8000 myapp
```

## 8.今後の改善・修正案
・AWSへの自動デプロイ  
・Slack通知機能追加  

## 9.実行した結果・効果
手動で行っていたビルド・テスト作業を自動化し、作業時間を削減に成功。  
pushで処理が実行されるため、開発フローの効率化を実現された。  
環境依存の問題を排除し、再現性の高い開発環境を構築出来た。
