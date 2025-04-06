import boto3
from langfuse.decorators import observe  # 追加


@observe() # 追加
def invoke_bedrock(prompt):
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

@observe() # 追加
def main(input):
	# 呼び出し
	output = invoke_bedrock(input)
	print(output)
	return output

main("Langfuseって何？")
