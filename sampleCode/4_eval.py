import boto3
from langfuse import Langfuse
from langfuse.decorators import observe


def get_prompt(word):
	langfuse = Langfuse()
	prompt = langfuse.get_prompt("what-is")
	compiled_prompt = prompt.compile(name=word)
	return compiled_prompt

# 追加：正解データを定義する関数
@observe()
def get_truth(word):
    truth = ""
    if word == "かぐたん":
        truth = "かぐたんは、KAG社が開発したSlackチャットボットです。"
    return truth

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
	prompt = get_prompt(input)
	get_truth(input) # 追加
	output = invoke_bedrock(prompt)
	print(output)
	return output

main("かぐたん") # 入力ワードを変更
