# その他のコンポーネント

> 本ガイドは、2024年5月2日に公開された[PAoC Other Components](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/paoc-other-components) をもとに作成されています。    
> その後の Planning Analytics on Cloud のアップデートにより、UI 表示、メニューの配置、設定項目、操作手順などが変更されている可能性があります。  
> 手順や画面が本ガイドと一致しない場合は、**IBM の最新ドキュメントや公式ガイドラインを必ず参照**し、最新版に沿った対応を行ってください。

---

## オプションコンポーネント

### IP許可リスト

必要に応じて **IP許可リスト**（IP Allow list）を有効にすることができます。  
これは、特定のIP範囲外からの Planning Analytics へのアクセスを制限する仕組みです。

たとえば、在宅勤務のユーザーや、インターネットカフェなど組織外の環境からアクセスするユーザーがいる場合は、IP範囲を特定するのが困難なため、IP許可リストを設定する必要があるかどうか慎重に検討する必要があります。

有効化にはサポートチケットの発行が必要です。  
詳細は以下をご参照ください：  
[Controlling access to services and shared folders](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=cloud-controlling-access-services-shared-folders)

---

### 非対話型アカウント（Non-interactive account）

必要に応じて **非対話型アカウント** を有効にすることができます。

Planning Analytics への一般的なログインは IBMid により行われ、ユーザーが対話的にログインする必要があります。  
一方、**restAPI の利用やバッチ処理など、対話を伴わないタスク**を実行する場合には、非対話型アカウントが必要です。  

このアカウントがまだ有効化されていない場合は、**サポートチケットを発行して有効化の依頼**を行ってください。

詳細はこちら：  
[Setting up a non-interactive account for use in the LDAP namespace](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=SSD29G_2.0.0/com.ibm.swg.ba.cognos.tm1_cloud_mg.2.0.0.doc/c_tm1_cloud_ccc_non_int_account.htm)

---

### その他のオプションツール

以下のようなツールが必要になる場合もありますが、本ガイドの対象外です。

- Cognos Integration Server  
- Cognos Command Center  

これらについては、**各製品のインストールガイド**を参照してください。
