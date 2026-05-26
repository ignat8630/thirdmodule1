import requests
from bs4 import BeautifulSoup

def get_builtin_functions():
    url = "https://docs.python.org/3/library/functions.html"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем все элементы <dl> с классом 'function' — каждый такой блок описывает одну функцию
        function_blocks = soup.find_all('dl', class_='function')
        base_url = "https://docs.python.org/3/library/functions.html"

        functions_list = []

        for block in function_blocks:
            # Внутри блока ищем тег <dt> — там находится якорь и название функции
            dt_tag = block.find('dt')
            if dt_tag and dt_tag.get('id'):
                func_name = dt_tag['id']
                # Формируем ссылку
                link = f"{base_url}#{func_name}"
                functions_list.append((func_name, link))

        # Выводим в требуемом формате
        for func_name, link in sorted(functions_list):
            print(f"{func_name}() {link}")

    except requests.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запускаем функцию
get_builtin_functions()
