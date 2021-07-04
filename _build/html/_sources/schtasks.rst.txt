Schtasks 사용법
================

작업 생성
~~~~~~~~~~
``schtasks /create /tn "python" /tr "C:\Users\11700205\workspace\99. 기타\(2021.06) 스케줄러\requirements.txt" /sc minute /mo 30 /sd 2021/07/04 /st 00:00``

작업 조회
~~~~~~~~~~
``schtasks /query /tn python /fo list /v``

작업 삭제
~~~~~~~~~~
``schtasks /delete /tn python``

한번 실행
~~~~~~~~~~
``schtasks /create /tn "python" /tr "C:\Users\11700205.EDBINS\Desktop\login.vbs" /sc once /st 14:19``

매개변수
~~~~~~~~~~
.. list-table:: **/create 매개변수 설명**
    :widths: 50 100
    :header-rows: 1

    * - 매개변수
      - 의미
    * - /tn
      - task 이름
    * - /tr
      - 실행파일 경로
    * - /sc
      - minute, hourly, daily, once 등
    * - /mo
      - 30, 60, 90
    * - /d
      - 실행요일 (mon, tue, wed 등)
    * - /sd
      - 시작시간일 (yyyy/mm/dd)
    * - /st
      - 시작시간 (HH:mm)