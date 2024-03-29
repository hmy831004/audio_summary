# 프로젝트명 onuii

이 파일은 프로젝트의 초기 설정과 데이터 전처리 및 요약의 단계를 설명합니다.

## 초기 설정

### Miniconda 설치

1. 리눅스 환경에 Miniconda를 설치합니다. 다음 링크로 이동하여 Miniconda를 다운로드하고 설치할 수 있습니다: [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. 설치가 완료되면, `.bashrc` 파일에 path를 설정합니다:

   ```sh
   echo \'export PATH="$HOME/miniconda3/bin:$PATH"\' >> ~/.bashrc
   source ~/.bashrc
   ```

### 가상환경 생성 및 실행

1. 가상환경 `bsj`를 생성합니다:

   ```sh
   conda create -n bsj python=3.9
   ```

2. 가상환경을 활성화합니다:

   ```sh
   conda activate bsj
   ```

### 필요한 패키지 설치

1. `requirements.txt` 파일을 이용하여 필요한 패키지를 설치합니다:

   ```sh
   pip install -r requirements.txt
   ```

### FFmpeg 설치

1. 오디오 처리를 위한 `ffmpeg`를 설치합니다:

   ```sh
   apt-get install ffmpeg
   ```

## 데이터 전처리
1. `app/data` 폴더에  `teacher.mp3` `student.mp3` 파일을 위치 시킨다.
2. `app/data/teacher_chunk`,`app/data/teacher_silence`,`app/data/student_chunk`,`app/data/student_silence` 4개 폴더 생성.
   
### 오디오 파일 처리
1. `teacher.mp3`와 `student.mp3`의 오디오를 10분씩 자릅니다.
2. 10분씩 나누어진 audio파일을 STT(음성 인식) 작업을 위하여 묵음 부분을 제거하여 오디오 파일을 저장합니다.
   ```sh
   sh preprocess.sh
   # python chunk_file.py --file_name teacher.mp3 --file_folder ./data
   # python chunk_file.py --file_name student.mp3 --file_folder ./data

   # python remove_silence.py --file_folder ./data/teacher_chunk --output_folder ./data/teacher_silence --export_format mp3
   # python remove_silence.py --file_folder ./data/student_chunk --output_folder ./data/student_silence --export_format wav
   ```

## OpenAI를 이용한 STT 출력과 텍스트 요약

### STT(Text 추출) 실행

1. `onuii.py` 스크립트를 실행하여 OpenAI의 STT API를 이용해 텍스트를 추출합니다.

   ```sh
   python onuii.py 
   ```

2. `teacher`와 `student`의 오디오를 10분 단위로 묶어 OpenAI의 Chat 기능을 이용하여 텍스트를 요약합니다.

이 과정들을 통해 데이터 전처리 및 요약이 이루어집니다.

### gunicorn과 FastAPI를 이용한 API 서버 구축

1. 서비스 실행
   ```sh
   gunicorn --bind 0:8500 main:app --worker-class uvicorn.workers.UvicornWorker --reload 
   ```
2. 브라우저 에서 `http://3.34.134.205:8500/onuii` 실행

