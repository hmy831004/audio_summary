from openai import OpenAI
import sys,os
from pydub import AudioSegment
import re


class SttToSummary():

    def __init__(self) -> None: 
        self.client = OpenAI(api_key=f'{Your_Open_API_KEY}')

    def stt_with_openai(self,file):

        audio_file= open(file, "rb")
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        
        return transcript.text

    def summary_teacher_student(self,teacher_text,student_text):
        response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system",
                    "content": "선생님과 학생이 온라인 과외를 통해 나눈 대화를 제공할거야. 선생님의 말과 학생의 말을 각각 제공할거야. 너는 대화를 보고 시간별로 요약을 진행해줘."
                    },
                    {"role": "user", "content": f"선생님:{teacher_text}\n\n학생:{student_text}"}
                ]
            )
            
        text = response.choices[0].message.content
        text = re.sub('\s+',' ',text)
        return text





if __name__=="__main__":
    stt_to_summary = SttToSummary()


    from glob import glob 
    teacher_files = sorted(glob('./data/teacher_silence/*'))
    student_files = sorted(glob('./data/student_silence/*.wav'))
    # stt_to_summary.stt_with_openai(teacher_files[0],student_files[0])
    print(teacher_files)
    print(student_files)
    teacher_texts = [stt_to_summary.stt_with_openai(file) for file in teacher_files]
    student_texts = [stt_to_summary.stt_with_openai(file) for file in student_files]
    
    summarys = [f'{i*10}~{(i+1)*10}분 요약\n'+stt_to_summary.summary_teacher_student(t,s) for i,(t,s) in enumerate(zip(teacher_texts,student_texts)) ]
    print(summarys)
    
    f = open('result.txt','w',encoding='utf-8')
    f.write('\n\n'.join(summarys))
    f.close()
