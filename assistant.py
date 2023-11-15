import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv
from collections import OrderedDict

def callchat(message):
    load_dotenv()
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )
    
    #스레드 생성,연결(runs)
    run = client.beta.threads.create_and_run(
        assistant_id="asst_FPg6Rlt9WKrgjROV07Du4joO", #본인 assistant id 입력
        thread={
        "messages": [
            {"role": "user", "content": message},
        ]
        }
    )
    #5초 대기
    time.sleep(5)
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
    response = message.content[0].text.value
    build_dict = OrderedDict([
    ("statusCode", 200),
    ("message", "api.common.ok"),
    ("data", {
        "reply": response
    })
    ])
    converte_json = json.dumps(build_dict, indent=2)
    print(converte_json)
    return converte_json