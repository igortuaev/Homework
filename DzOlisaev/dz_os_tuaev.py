import shutil
import os
import datetime



'''1.Написать функцию, которая выводит список файлов заданного каталога, с указанием размеров файлов и даты их последней модификации'''



def list_directory_contents(directory_path):
    """Возвращает список файлов в заданном каталоге с информацией о размере и дате модификации.

    Args:
        directory_path (str): Путь к каталогу.

    Returns:
        list of dict: Список словарей, где каждый словарь содержит информацию о файле:
                       - 'name': имя файла
                       - 'size': размер файла в байтах
                       - 'modified': дата последней модификации в формате datetime
        str: Сообщение об ошибке, если каталог не найден.
    """

    if not os.path.exists(directory_path):
        return None, f"Каталог '{directory_path}' не найден." #Возвращаем None и сообщение об ошибке

    file_list = [] #Создаем пустой список для хранения информации о файлах
    for filename in os.listdir(directory_path): #Перебираем все элементы в каталоге
        filepath = os.path.join(directory_path, filename) #Формируем полный путь к файлу

        if os.path.isfile(filepath): #Проверяем, является ли элемент файлом (не каталогом)
            try:
                size = os.path.getsize(filepath) #Получаем размер файла
                timestamp = os.path.getmtime(filepath) #Получаем timestamp последней модификации
                modified_time = datetime.datetime.fromtimestamp(timestamp) #Преобразуем timestamp в объект datetime

                file_info = { #Создаем словарь с информацией о файле
                    'name': filename,
                    'size': size,
                    'modified': modified_time
                }
                file_list.append(file_info) # Добавляем словарь в список

            except OSError as e: #Обрабатываем возможные ошибки (например, проблемы с доступом к файлу)
                return None, f"Ошибка при обработке файла '{filename}': {e}"

    return file_list, None  #Возвращаем список файлов и None (ошибок нет)

'''2.Написать функцию, которая создает резервную копию заданного файла/каталога в имени резервной копии должны использоваться дата и время создания резервной копии'''

def create_backup(source_path, backup_dir=None):
    """Создает резервную копию файла или каталога.

    Args:
        source_path (str): Путь к файлу или каталогу для резервного копирования.
        backup_dir (str, optional): Путь к каталогу для сохранения резервной копии. 
                                     Если не указан, резервная копия будет создана 
                                     в текущем каталоге. Defaults to None.

    Returns:
        tuple: Кортеж (путь к резервной копии, сообщение об ошибке). 
               Если резервное копирование успешно, сообщение об ошибке будет None.
               Если произошла ошибка, путь к резервной копии будет None, а сообщение об ошибке 
               будет содержать описание ошибки.
    """

    if not os.path.exists(source_path):
        return None, f"Исходный файл/каталог '{source_path}' не найден."

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    source_name = os.path.basename(source_path)
    backup_name = f"{source_name}_{now}"

    if backup_dir:
        if not os.path.isdir(backup_dir):
            if os.path.exists(backup_dir):
                return None, f"'{backup_dir}' существует, но не является каталогом."
            else:
                try:
                    os.makedirs(backup_dir)
                except OSError as e: #Обработка потенциальной ошибки при создании каталога
                    return None, f"Ошибка при создании каталога '{backup_dir}': {e}"
        backup_path = os.path.join(backup_dir, backup_name)
    else:
        backup_path = backup_name

    try:
        if os.path.isfile(source_path):
            shutil.copy2(source_path, backup_path)
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, backup_path)
        return backup_path, None  #Успех - возвращаем путь и None как ошибку

    except Exception as e:
        return None, str(e) #Возвращаем None и сообщение об ошибке


 
