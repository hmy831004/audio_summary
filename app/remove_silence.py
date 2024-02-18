from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from glob import glob
import argparse
import os
# import speech_recognition as sr

def remove_silence(audio_path,output_path ,export_format='mp3',silence_thresh=-40, chunk_size=800):
    """
    무음 부분을 제거하는 함수.

    Params:
      audio_path (str): 원본 오디오 파일 경로
      silence_thresh (int): 무음으로 판단되는 임계값(dB)
      chunk_size (int): 무음 감지를 위한 청크 사이즈(ms)
    Returns:
      AudioSegment: 무음이 제거된 오디오 세그먼트
    """
    # 오디오 파일 읽기
    audio = AudioSegment.from_file(audio_path)

    front_file_name = os.path.basename(audio_path).split('.')[0]
    # 무음이 아닌 부분 감지
    nonsilent_chunks = detect_nonsilent(audio, min_silence_len=chunk_size, silence_thresh=silence_thresh)

    # 무음이 아닌 청크 합치기
    audio_processed = AudioSegment.empty()
    for start, end in nonsilent_chunks:
        audio_processed += audio[start:end+600]

    # export_format = "wav"  # \'wav\' 형식으로 저장하는 것이 일반적으로 STT에는 더 좋습니다.
    output_file_name = os.path.join(output_path,front_file_name)+'.'+ export_format
    audio_processed.export(output_file_name, format=export_format)

    # return audio_processed

if __name__=="__main__":
    
    parser = argparse.ArgumentParser(description='Process some files.')

    # file_folder 인자 추가
    parser.add_argument('--file_folder', type=str, default='./data/student_chunk',help='Path to the folder to process')
    # output folder 
    parser.add_argument('--output_folder', type=str, default='./data/student_silence',help='Output file Path')
    parser.add_argument('--export_format', type=str, default='mp3',help='audio format')

    # 인자들을 파싱
    args = parser.parse_args()
    # 인자 값 출력
    print(f"File folder: {args.file_folder}")
    # 오디오 파일 경로들
    files = glob(args.file_folder+f'/*')
    print(f"parsing Files: {files}")
    
    # audio_path = './data/student.mp3'  # .mp3, .wav 등 다양한 포맷을 지원합니다.
    for file in files:
        # 무음 제거
        remove_silence(file,args.output_folder,export_format=args.export_format)
        # front_file_name = os.path.basename(file).split('.')[0]
        # print(front_file_name)

