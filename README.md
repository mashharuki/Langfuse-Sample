# Langfuse-Sample

LLM 監視・評価ツール Langfuse を調査・検証するためのリポジトリです。

## Langfuse とは

Langfuse は、LLM（大規模言語モデル）アプリケーションのためのオープンソースの観測性（Observability）および分析プラットフォームです。LLM を活用したアプリケーションの開発、デバッグ、最適化、モニタリングを支援するツールとして設計されています。

<div align="center">
  <img src="https://raw.githubusercontent.com/langfuse/langfuse/main/docs/static/img/banner.png" alt="Langfuse Banner" width="600"/>
</div>

## 主な機能

### 1. トレーシング（Tracing）

- **リクエストの可視化**: LLM へのリクエストとレスポンスを詳細に記録
- **複雑なワークフローの追跡**: 複数のモデル呼び出しや処理ステップを含むワークフローを視覚化
- **コンテキストの保持**: プロンプト、パラメータ、メタデータなどの重要な情報を保存

### 2. スコアリング（Scoring）

- **品質評価**: LLM の出力品質を評価するためのスコアリングシステム
- **フィードバックの収集**: ユーザーや自動評価からのフィードバックを統合
- **パフォーマンス指標**: 応答時間、コスト、品質などの指標を追跡

### 3. データセット管理（Datasets）

- **テストデータの作成**: 実際のユーザーデータから評価用データセットを構築
- **継続的評価**: モデルの変更やプロンプトの更新に対する影響を評価
- **バージョン管理**: データセットのバージョン管理とモデル評価の履歴追跡

### 4. 分析とモニタリング（Analytics & Monitoring）

- **使用状況の分析**: モデル使用量、コスト、パフォーマンスの詳細な分析
- **異常検知**: 品質低下や異常なパターンの検出
- **ダッシュボード**: カスタマイズ可能な視覚化ツール

## Langfuse を使うメリット

1. **開発の加速**: LLM アプリケーションの開発サイクルを短縮
2. **品質向上**: 継続的なモニタリングと評価による出力品質の向上
3. **コスト最適化**: モデル使用量とパフォーマンスの最適化によるコスト削減
4. **透明性の確保**: LLM の動作と意思決定プロセスの透明化
5. **セキュリティとプライバシー**: オープンソースでセルフホスティング可能なため、データの管理が容易

## インストールと設定

Langfuse は複数の方法でデプロイできます：

### クラウドホスティング

最も簡単な方法は、Langfuse が提供するクラウドサービスを利用することです：

1. [Langfuse Cloud](https://langfuse.com) にアクセスしてアカウントを作成
2. プロジェクトを作成し、API キーを取得
3. SDK をインストールしてアプリケーションに統合

```bash
# Node.js/TypeScript
npm install langfuse

# Python
pip install langfuse
```

### セルフホスティング

プライバシーやセキュリティの要件が厳しい場合は、自社インフラ上で Langfuse をホスティングできます：

1. GitHub リポジトリをクローン：

```bash
git clone https://github.com/langfuse/langfuse.git
```

2. Docker Compose を使用してデプロイ：

```bash
cd langfuse
docker-compose up -d
```

## 基本的な使い方

### 1. SDK の初期化

```python
# Python
from langfuse import Langfuse

langfuse = Langfuse(
    public_key="pk-lf-...",
    secret_key="sk-lf-...",
    host="https://cloud.langfuse.com"  # セルフホスティングの場合は自分のホストURLを指定
)
```

```typescript
// TypeScript
import { Langfuse } from "langfuse";

const langfuse = new Langfuse({
  publicKey: "pk-lf-...",
  secretKey: "sk-lf-...",
  host: "https://cloud.langfuse.com", // セルフホスティングの場合は自分のホストURLを指定
});
```

### 2. トレースの作成と記録

```python
# トレースの開始
trace = langfuse.trace(name="user-query")

# LLMの呼び出しを記録
generation = trace.generation(
    name="initial-response",
    model="gpt-4",
    prompt="ユーザーの質問に回答してください: {query}",
    completion="ここにLLMの回答が入ります",
    metadata={
        "temperature": 0.7,
        "user_id": "user-123"
    }
)

# スコアの記録
trace.score(name="relevance", value=0.95)
```

### 3. フィードバックの収集

```python
# ユーザーフィードバックの記録
langfuse.score(
    trace_id=trace.id,
    name="user-satisfaction",
    value=4,  # 5段階評価
    comment="回答が非常に役立ちました"
)
```

## 高度な機能

### 1. カスタムイベントの記録

```python
# カスタムイベントの記録
trace.event(
    name="user-interaction",
    input={"action": "click-more-info"},
    output={"displayed": "additional-context"},
    metadata={"session_duration": 120}
)
```

### 2. スパンによる処理ステップの詳細化

```python
# 処理ステップの詳細記録
with trace.span(name="data-processing") as span:
    # データ処理ロジック
    processed_data = process_data(raw_data)
    span.update(output={"processed_items": len(processed_data)})
```

### 3. 複数モデルの比較

```python
# 複数モデルの比較
for model in ["gpt-3.5-turbo", "gpt-4", "claude-2"]:
    with trace.span(name=f"model-comparison-{model}") as span:
        response = call_llm_api(model, prompt)
        span.generation(
            name=model,
            model=model,
            prompt=prompt,
            completion=response,
            metadata={"latency": measure_latency()}
        )
        span.score(name="accuracy", value=evaluate_accuracy(response))
```

## ダッシュボードと分析

Langfuse のダッシュボードでは以下のような分析が可能です：

- **トレース詳細**: 個々のユーザーリクエストの完全な処理フロー
- **モデルパフォーマンス**: 各モデルの応答時間、コスト、品質の比較
- **プロンプト効果**: 異なるプロンプトバージョンの効果分析
- **コスト分析**: モデル使用量とコストの詳細な内訳
- **品質トレンド**: 時間経過に伴う出力品質の変化

## 参考文献

- [Langfuse 公式ドキュメント](https://langfuse.com/docs)
- [Langfuse GitHub](https://github.com/langfuse/langfuse)
- [LLM アプリケーションのモニタリングベストプラクティス](https://langfuse.com/blog)
- [Langfuse Python SDK](https://langfuse.com/docs/sdk/python)
- [Langfuse TypeScript SDK](https://langfuse.com/docs/sdk/typescript)
- [OpenAI + Langfuse 統合ガイド](https://langfuse.com/docs/integrations/openai)
- [LangChain + Langfuse 統合ガイド](https://langfuse.com/docs/integrations/langchain)
- [LlamaIndex + Langfuse 統合ガイド](https://langfuse.com/docs/integrations/llamaindex)
- [Langfuse API リファレンス](https://langfuse.com/docs/api)
- [Langfuse CLI ツール](https://langfuse.com/docs/cli)
- [Langfuse セルフホスティングガイド](https://langfuse.com/docs/deployment)
- [Langfuse セキュリティガイド](https://langfuse.com/docs/security)
- [Langfuse コミュニティフォーラム](https://github.com/langfuse/langfuse/discussions)
- [Langfuse ロードマップ](https://github.com/langfuse/langfuse/projects)
- [LLM アプリを Ragas で評価して、Langfuse で可視化しよう！](https://speakerdeck.com/minorun365/llmapuriworagasdeping-jia-site-langfusedeke-shi-hua-siyou?slide=17)
- [Qiita - 【LLMOps】あなたの生成 AI アプリを監視＆評価しよう！ Langfuse 入門ハンズオン](https://qiita.com/minorun365/items/9d0d11f0ecb4c29924d5)
