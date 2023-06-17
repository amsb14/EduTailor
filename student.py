import streamlit as st
import pandas as pd
from teacher import questions_to_dict, display_questions_and_collect_answers

def student_actions():
    # load the questions from the file
    file_name = 'questions.txt'
    with open(file_name, "r") as file:
        data = file.read()
        MCQs = questions_to_dict(data)
            
    display_questions_and_collect_answers(MCQs)
