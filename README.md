# AWSAutomaticTagging
AWSリソースへの自動タグ付けを行う

### 対象リソース

1. EC2

### タグ付け

| kye | value |
| --- | --- |
| Owner | $userName |
| CreationDate | $creationDate |

userName -> IAMユーザー

creationDate -> 構築日(YYYY-MM-DD)
