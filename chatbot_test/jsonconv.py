import json

def jsonl_to_json(jsonl_file, json_file):
    with open(jsonl_file, 'r', encoding='utf-8') as infile:
        # 각 라인을 읽어 JSON으로 파싱한 후 리스트에 추가
        data = [json.loads(line) for line in infile]

    # 리스트를 JSON 형식으로 변환하여 저장
    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=2)

# 사용 예시
jsonl_to_json('customlogdata2.jsonl', 'customlogdata3.json')
