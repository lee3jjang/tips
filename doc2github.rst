sphinx로 만든 문서 github에 올리기
===================================

1. ``conf.py`` -> ``extensions`` 에 ``sphinx.ext.githubpages`` 추가
2. github repo. (예: tips) 만들기
3. ``make.bat html`` 해서 나오는 ``_build/html`` 폴더를 ``docs`` 로 복사
4. github settings 가서 /docs 물리게 설정
