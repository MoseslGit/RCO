import os
import json

data_folder = "data/tex/evanchen/"
output_file_path = 'data/problems/'

def escape_double_quotes(text):
    return text.replace('"', r'\"')

def output_problems(problems):
    os.makedirs(output_file_path, exist_ok=True)

    with open(output_file_path + 'evanchen.jsonl', 'w', encoding='utf-8') as output_file:
        for problem in problems:

            # if '"' in problem[0]:
            #     raise Exception(problem[0])
            # if '"' in problem[1]:
            #     raise Exception(problem[1])
            
            json_line = {'problem': escape_double_quotes(problem[0]), 'proof': escape_double_quotes(problem[1])}
            json_string = json.dumps(json_line, ensure_ascii=False)
            output_file.write(json_string + '\n')



problems = []
for filename in os.listdir(data_folder):
    if filename.endswith(".tex"):
        file_path = os.path.join(data_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            lines = content.split('\n')
            
            i = 0
            while i < len(lines):
                if "\\begin{mdframed}[style=mdpurplebox,frametitle={Problem statement}]" in lines[i]:
                    j = i + 1
                    while j < len(lines):
                        if "\\end{mdframed}" in lines[j]:
                            problem_statement = '\n'.join(lines[i+1:j]).strip()
                            i = j
                            break
                        j += 1
                    while j < len(lines):
                        if "\pagebreak" in lines[j]:
                            problem_proof = '\n'.join(lines[i+1:j]).strip()
                            i = j
                            break
                        j += 1

                    problems.append([problem_statement, problem_proof])
                i += 1

output_problems(problems)