# 블로그 글 작성 스크립트

import os
from openai import OpenAI
api_key = os.getenv('OPENAI_API_KEY')


OpenAI.api_key = api_key
client = OpenAI()

def generate_blog_content(keyword):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role" :"system", "content" : "당신은 블로그 글 작성 전문가 입니다 .핫 토픽 키워드를 가지고 사용자 유입을 효과적으로 이끌어 내게 글을 쓸 수 있습니다."},
          {"role" :"user", "content" : f"{keyword}'에 대한 흥미로운 블로그 글을 작성해 주세요. 트렌드 이유와 관련된 흥미로운 사실을 포함해 주세요."}
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message

if __name__ == "__main__":
    sample_keyword = "example keyword"
    content = generate_blog_content(sample_keyword)
    print(content)