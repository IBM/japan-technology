---
authors: ''
completed_date: '2021-08-10'
components:
- openshift
- kubernetes
- devops
draft: false
excerpt: このガイドでは、KubernetesからOpenShiftにサービスを移行する方法を、イメージやセキュリティポリシーを変更してOpenShiftの標準に準拠する方法を中心に説明しています。
menu_order: 5
meta_description: このガイドでは、KubernetesからOpenShiftにサービスを移行する方法を、イメージやセキュリティポリシーを変更してOpenShiftの標準に準拠する方法を中心に説明しています。
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
meta_title: まとめ、次のステップ、IoT開発のための追加リソース
primary_tag: containers
subtitle: まとめ、次のステップ、追加リソース
title: 概要
---

アプリケーションがKubernetesで正常にデプロイされて動作している場合、それをOpenShiftに移行するには。
1. コンテナイメージの移行
1. PSP を SCC に移行する。

これにより、アプリケーションがOpenShift上でも適切にデプロイされ、実行されるようになります。実行できたら、「[Make your solution run as a service and add it to service catalogs](https://developer.ibm.com/articles/a-guide-to-turning-your-solution-into-a-service-on-kubernetes-and-adding-it-to-service-catalogs/)」で説明しているように、自己管理できるようにしたり、認証を取得したり、Red Hat Marketplaceなどのサービスカタログに追加したりする作業を進めることができます。