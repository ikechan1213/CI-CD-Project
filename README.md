#  CI/CDパイプライン構築（FastAPI × Docker × GitHub Actions）
##  1.目的
 今後のプロジェクト開発効率上昇のためCI/CD環境の構築  
 　　　　　　　　↓  
 コードpushでテスト・ビルドを自動化させること。
 
## 2.工夫点
Dockerを用いて環境差異,環境依存を解消したこと。

## 3.開発に至った経緯
開発をする上で、手動ビルドやテストに時間がかかることへの煩雑さからこのようなプロジェクトを作成しようと考えました。

 ## 4.技術スタック
 ・Backend：FastAPI(Python)  
 ・Container：Docker  
 ・CI/CD：GitHub Actions  
 ・その他：pytest

 ## 5.システムの構成
 User → GitHub push  
 　　　↓  
 GitHub Actions  
 　　　↓  
 Testや、Build(Docker)

 ## 6.実装機能
・APIエンドポイント作成  
・Dockerによるコンテナ化  
・push時の自動テスト  
・Dockerイメージの自動ビルド
