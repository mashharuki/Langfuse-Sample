# ハンズオン用のコード

## 動かし方

```bash
python 1_bedrock.py
```

以下のようになれば OK!

```bash
Langfuseは、AIアプリケーションのためのオープンソースのオブザーバビリティ・プラットフォームです。主に以下の機能を提供しています：

1. LLM（大規模言語モデル）の応答をログ記録、トレース、評価する機能
2. AIアプリケーションのパフォーマンスと品質を監視する機能
3. 開発者がプロンプトエンジニアリングを改善し、AIモデルの出力を最適化するためのツール

Langfuseは特に生成AIアプリケーションの開発やデプロイを行うチームにとって、AIシステムの透明性と信頼性を高めるのに役立つツールです。OpenAI、Anthropic、Google、Mistralなどの様々なLLMプロバイダーと統合することが できます。
```

環境変数の設定

```bash
export LANGFUSE_SECRET_KEY=sk-XXXXXXXXXXXXXXXXXXXXXX
export LANGFUSE_PUBLIC_KEY=pk-XXXXXXXXXXXXXXXXXXXXXX
export LANGFUSE_HOST=https://XXXXXXX.langfuse.com
```

計測トレースを加えたバージョンで実行

```bash
python 2_trace.py
```

```bash
# Langfuseとは

Langfuse（ラングフューズ）はLLM（大規模言語モデル）アプリケーション向けのオープンソースの監視・分析プラットフォームです。以下の特徴があります：

- LLM（大規模言語モデル）を使ったアプリケーションのログ記録と分析機能を提供
- プロンプト管理やトレーシングを含むデバッグツール
- パフォーマンス評価と品質モニタリング
- オープンソースで自己ホスティング可能
- Python、TypeScript、その他の言語用のSDKを提供

開発者がLLMベースのシステムを効率的に構築・最適化・モニタリングするためのツールとして機能します
```

```bash
python 3_prompt.py
```

langfuse の方に監視結果が出力されていれば OK!

```bash
python 4_eval.py
```

データセットから値を取得して来るようにする。

```bash
python 5_dataset.py
```

```bash
"かぐたん"（Kagutan）は、宇宙航空研究開発機構（JAXA）の月探査機「かぐや（SELENE）」の愛称の一つです。「かぐや」をより親しみやすく呼ぶ際に「かぐたん」と呼ばれることがあります。「かぐや」は2007年に打ち上げられ 、月の詳細な観測を行いました。
```
