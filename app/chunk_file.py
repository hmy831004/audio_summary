from pydub import AudioSegment
import math
import os
import argparse

def split_voice_file_to_chunk_size(file_folder,file_name,export_format='mp3'):
    """
    Params:
      file_folder (str): 원본 오디오 파일 경로
      file_name (str): 파일 이름
      export_format (int): 파일 포맷 = mp3 or wav

    Returns:
        10분 단위로 나뉘어진 오디오 파일.
    """
    # MP3 파일 로드
    file_folder = file_folder
    file_name = file_name # 여기에 파일 경로 입력
    front_file_name = file_name.split('.')[0]

    output_path = os.path.join(file_folder,front_file_name+"_chunk")
    export_format = export_format

    file_path = os.path.join(file_folder,file_name)
    audio = AudioSegment.from_mp3(file_path)

    # 파일 길이 계산 (ms 단위)
    file_length_ms = len(audio)

    # 10분을 ms단위로 변환
    ten_minutes_ms = 10 * 60 * 1000

    # 파일을 10분 단위로 나눌 개수 계산
    num_segments = math.ceil(file_length_ms / ten_minutes_ms)

    # # 파일 나누기 및 저장
    for i in range(num_segments):
        # 현재 세그먼트의 시작과 종료 시점 계산
        start_ms = i * ten_minutes_ms
        end_ms = min(start_ms + ten_minutes_ms, file_length_ms)
        
        # 현재 세그먼트 자르기
        segment = audio[start_ms:end_ms]
        
        # 세그먼트 저장 (이름은 0001, 0002 등의 형식으로 지정)
        segment_path = os.path.join(output_path,f'{front_file_name}_{i+1:04d}.{export_format}')
        segment.export(segment_path, format=export_format)
        print(f"Segment {i+1} exported as {segment_path}")
    


if __name__=="__main__":
    
    parser = argparse.ArgumentParser(description='Process some files.')

    # file_path 인자 추가
    parser.add_argument('--file_name', type=str,default='teacher.mp3', help='file nameh to process')

    # file_folder 인자 추가
    parser.add_argument('--file_folder', type=str, default='./data',help='Path to the folder to process')

    # 인자들을 파싱
    args = parser.parse_args()
    print(args)
    # 인자 값 출력
    print(f"File folder: {args.file_folder}")
    print(f"File name: {args.file_name}")
    split_voice_file_to_chunk_size(args.file_folder,args.file_name)
