import os
import asyncio
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']


async def callchat(message):
    async with openai.AsyncClient(api_key=api_key) as client:
        run = await client.beta.threads.create_and_run(
            assistant_id="asst_FPg6Rlt9WKrgjROV07Du4joO", # 본인 assistant id 입력
            thread={
                "messages": [
                    {"role": "user", "content": message},
                ]
            }
        )

        await asyncio.sleep(5)# 이럴거면 왜 비동기씀?

        run_steps = await client.beta.threads.runs.steps.list(
            thread_id=run.thread_id,
            run_id=run.id
        )

        run_step = await client.beta.threads.runs.steps.retrieve(
            thread_id=run.thread_id,
            run_id=run.id,
            step_id=run_steps.data[0].id
        )

        message = await client.beta.threads.messages.retrieve(
            message_id=run_step.step_details.message_creation.message_id,
            thread_id=run.thread_id,
        )

        return message.content[0].text.value

# 비동기 함수 실행을 위한 메인 함수
async def main():
    response = await callchat("넌 누구니?")
    print(response)

# 이벤트 루프 실행
asyncio.run(main())
