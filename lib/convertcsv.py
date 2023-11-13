import csv
import re

# log 텍스트 파일 이름
logs = "log.txt"

# 출력 CSV 파일 이름
csv_file = "output.csv"

# CSV 파일을 쓰기 모드로 엽니다.
with open(csv_file, mode='w', newline='',encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # 헤더를 쓰기
    writer.writerow(["검색시간", "검색어", "검색지역"])
    
    # 텍스트 파일을 읽어서 CSV 파일로 변환
    with open(logs, 'r', encoding='utf-8') as logs:
        for log in logs:
            log=log.replace(';', '').replace('`', '')
            
            #문자열에서 검색일자 추출
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', log)
            # 정규 표현식을 사용하여 "name"과 "address" 추출
            name_match = re.search(r'name\sLIKE\s\'%(.*?)%\'', log)
            address_match = re.search(r'address\sLIKE\s\'%(.*?)%\'', log)
            
            if address_match:
                address_match = address_match.group(1)
            else:
                address_match = "null"
            
            # name_match가 None일 경우 기본값 설정
            if name_match:
                name_match = name_match.group(1)
            else:
                name_match = "null"
            
            writer.writerow([date_match.group(1), name_match, address_match])

print(f"텍스트 파일이 {csv_file}으로 성공적으로 변환되었습니다.")
