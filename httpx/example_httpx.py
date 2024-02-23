import httpx
from pprint import pprint


def get_example(data: dict) -> dict:
    answer = httpx.get('https://httpbin.org/get', params=data)
    answer.raise_for_status()
    return answer.json()


def post_example(data: dict) -> dict:
    answer = httpx.post('https://httpbin.org/post', data=data)
    answer.raise_for_status()
    return answer.json()


def main():
    data = {'ключ': 'значение'}
    try:
        pprint(get_example(data))
        pprint(post_example(data))
    except Exception as e:
        print('Ошибка: ', e)


if __name__ == '__main__':
    main()
