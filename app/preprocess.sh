#!/bin/bash

python chunk_file.py --file_name teacher.mp3 --file_folder ./data
python chunk_file.py --file_name student.mp3 --file_folder ./data

python remove_silence.py --file_folder ./data/teacher_chunk --output_folder ./data/teacher_silence --export_format mp3
python remove_silence.py --file_folder ./data/student_chunk --output_folder ./data/student_silence --export_format wav