# IBMid フェデレーション設定ガイド

> 本ガイドは、2024年5月2日に公開された [IBMid Federation](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/ibmid-federation)記事をもとに作成されています。  
> ただし、Planning Analytics on Cloud の認証環境や UI、運用ポリシーは継続的に更新されているため、本資料の内容と現時点の仕様が異なる可能性があります。  
> 内容と操作が一致しない場合は、**IBM の最新ドキュメントやサポートポータルを必ず参照**し、最新版に沿って対応を進めてください。

---

## フェデレート認証とは

IBMid は、IBMid 対応アプリケーション全体でユーザー認証を管理する仕組みです。以下の2つの形態があります：

1. IBM 管理型：IBM が管理するユーザー ID とパスワードのグローバルディレクトリ。  
   詳細は [Create an IBMid](./creating-an-ibmid/) を参照。
2. エンタープライズ・フェデレーション型：ユーザーの認証を外部の ID プロバイダー（idProvider）で管理します。  
   例：AzureAD、PingFederate、OKTA、ADFS など

---

## フェデレーションが不要な場合

- デフォルトは IBM 管理型です。
- 組織がすでにフェデレートされている場合は、追加の設定は不要です。

---

## エンタープライズ・フェデレーションの利点

- 他の同じ ID プロバイダーを使用するアプリケーションでもシングルサインオン（SSO）が可能です。
- 詳細手順や設定は [IBMid Enterprise Federation](https://www.ibm.com/docs/en/ief) を参照してください。

---

## フェデレーションの開始方法

My Support ポータルで、以下の製品に対してサポートチケットを作成してください：

「IBMid Enterprise Federation」

製品がドロップダウンに表示されない場合は、「IBMid」と入力してください。

![製品選択画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/KXQzPPGbRnChqrEusnvy_Product%20selection.jpeg)

---

## 注意事項

- IBMid Enterprise Federation はアプリケーション単位ではなく、会社単位（Company to Company）の設定です。  
  例：@ibm.com のメールドメイン単位で適用されます。
- フェデレーションが有効になると、組織の ID プロバイダーに登録されていないユーザーは IBMid を利用できません。
- 各アプリケーションでの利用許可（例：Planning Analytics へのモデラー権限など）はアプリケーション側で管理されます。

---

## フェデレーション設定中の作業について

フェデレーション完了前でも、IBM 管理型 IBMid を使って作業を進めることが可能です。

例：ユーザーが IBMid に登録 → アプリケーションを開発 → フェデレーション後にアカウントが自動的に移行されます。

---

## 開始のタイミングについて

今すぐ開始してください。

IBMid フェデレーションには最短でも35日かかります。  
社内での稟議やリソース調整が必要な場合はさらに時間がかかるため、可能な限り早くサポートチケットを作成してください。

---

## よくあるエラーについて

フェデレーションの途中で発生する代表的なエラーについては、以下のリンクを参照してください：  
[IBMid common errors](https://www.ibm.com/docs/en/ief?topic=general-errors)
