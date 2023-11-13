import os
import time
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

#스레드 생성,연결(runs)
run = client.beta.threads.create_and_run(
    assistant_id="asst_FPg6Rlt9WKrgjROV07Du4joO", #본인 assistant id 입력
    thread={
    "messages": [
        {"role": "user", "content": "어떤 검색어가 가장 많이 검색됐어?"}
    ]
    }
)
#3초 대기
time.sleep(3)
#실행 단계 나열
run_steps = client.beta.threads.runs.steps.list(
    thread_id=run.thread_id,
    run_id=run.id
)
#실행 단계 검색
run_step = client.beta.threads.runs.steps.retrieve(
    thread_id=run.thread_id,
    run_id=run.id,
    step_id=run_steps.data[0].id
)
#메세지 검색
message = client.beta.threads.messages.retrieve(
    message_id=run_step.step_details.message_creation.message_id,
    thread_id=run.thread_id,
)
print(message.content[0].text.value)