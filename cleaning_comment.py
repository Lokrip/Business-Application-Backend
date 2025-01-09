import os
import re


def remove_comments_from_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        lines = file.readlines()
        
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            # Удаляем строки, которые начинаются с комментария
            if not line.strip().startswith('#'):
                # Удаляем комментарии внутри строки
                line = re.sub(r'#.*$', '', line)
                file.write(line + '\n')
                # Пропускаем пустые строки после удаления комментариев
                if line:
                    file.write(line + '\n')
                
def remove_comments_from_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            # Обрабатываем только .py файлы
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                remove_comments_from_file(file_path)
                
