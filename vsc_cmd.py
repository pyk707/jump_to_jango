##vsc에서 cmd를 사용하고 싶을 때
#ctrl + shift + p → shell입력 → command prompt 선택 → 터미널 재시작(휴지통 클릭 후 ctrl + `)

##cmd창에서 다음과 같이 입력
#mkdir venvs → venvs폴더 만들고
#cd venvs → venvs로 이동
#python -m venv mysite  → 파이썬 모듈 중 venv라는 가상 모듈을 사용하고, 가상 모듈의 이름은 mysite
#cd를 사용하여 vevns의 Scripts에 들어가서
#activate // deactivate를 사용하여 가상화를 끄고 킬 수 있다

#pip upgrade → python -m pip install --upgrade pip

##프로젝트 루트에 디렉터터리 생성하고 가상 환경에 진입하기
#적당한 곳에 mkdir projects
#projects로 이동해서 'C:\venvs\mysite\Scripts\activate' 활성화
#mkdir mysite
#cd mysite
#django-admin startproject config .
#(.)점은 '현재 디렉터리를 프로젝트 디렉터리로 만들어라'는 뜻 