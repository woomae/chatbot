import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
result = openai.FineTune.list()
fine_tuned_model = "davinci"#result['data'][0]["fine_tuned_model"] #fine_tune한 모델의 이름 or davinci

new_prompt = "다음 데이터를 참고해서 어디가 가장많이 검색된지 알려줘! 최근 검색된 시간, 검색어, 검색지역은 다음과 같아 : 2023-11-29, 만화, 순천, 2023-11-29, 만화, 순천, 2023-11-29, 아트박스, 나주,"
answer = openai.Completion.create(
	model=fine_tuned_model,
	prompt=new_prompt
)
print(answer)
print(answer['usage']['total_tokens']) #토큰 수
print(answer.choices[0].text.strip()) #결과 텍스트