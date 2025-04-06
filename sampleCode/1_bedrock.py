import boto3


# Bedrockの推論APIを実行する関数
def invoke_bedrock(prompt):
	# このコードは、AWSのBedrockを使用して、指定されたプロンプトに基づいて応答を生成します。
	bedrock = boto3.client("bedrock-runtime")
	
  # モデルを指定してLLMに推論させる
	response = bedrock.converse(
		modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
		messages=[
			{
				"role": "user",
				"content": [{"text": prompt}]
			}
		]
	)
	output = response["output"]["message"]["content"][0]["text"]
	return output

# 上記の関数を呼び出し、結果を画面出力するメイン関数
def main(input):
	output = invoke_bedrock(input)
	print(output)
	return output

# メイン関数に入力を与えて呼び出す
main("Langfuseって何？")
