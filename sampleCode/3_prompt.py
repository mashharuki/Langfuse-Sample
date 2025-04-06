import boto3
from langfuse import Langfuse  # 追加
from langfuse.decorators import observe


# 追加：Langfuseからプロンプトを取得する関数
def get_prompt(word):
	langfuse = Langfuse()
	# 追加：Langfuseからプロンプトを取得
	prompt = langfuse.get_prompt("what-is")
	# 追加：プロンプトをコンパイル
	compiled_prompt = prompt.compile(name=word)
	return compiled_prompt

@observe()
def invoke_bedrock(prompt):
	bedrock = boto3.client("bedrock-runtime")
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

@observe()
def main(input):
	# 追加：Langfuseからプロンプトテンプレートを取得
	prompt = get_prompt(input) # 追加
	output = invoke_bedrock(prompt)
	print(output)
	return output

main("Langfuse") # 引数を変更
