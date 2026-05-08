import requests
from requests.exceptions import RequestException, Timeout
from models import API_CATEGORY, API_ITEM


class YC:
    # TODO Ավելացնել ֆունկցիա get_item

    def __init__(self):
        # TODO Փոփոխականները դնել .env-ի մեջ
        self.headers = {}
        self.url_category = ''
        self.url_item = ''


    def get_by_category(self, category_id):
        data_body = {
            "categoryId": category_id,
            "count": 10000,
            "page": 1,
            "parentId": category_id,
        }

        try:
            res = requests.post(self.url_category, headers=self.headers, json=data_body, timeout=(5, 15))
            res.raise_for_status()

            try:
                return API_CATEGORY.model_validate(res.json())
            except Exception as e:
                print(f"Տվյալների վալիդացման սխալ: {e}")
        except Timeout:
            print("Հարցումը չեղարկվեց ժամանակի սպառման պատճառով (Timeout).")
        except RequestException as e:
            print(f"Տեղի է ունեցել սխալ հարցման ընթացքում: {e}")
        # TODO Ավելացնել լոգավորում

        return None

    def get_item(self, item_id: int):
        url = self.url_item + str(item_id)
        try:
            res = requests.get(url, headers=self.headers, timeout=(5, 15))
            res.raise_for_status()

            try:
                return API_ITEM.model_validate(res.json())
            except Exception as e:
                print(f"Տվյալների վալիդացման սխալ: {e}")
        except Timeout:
            print("Հարցումը չեղարկվեց ժամանակի սպառման պատճառով (Timeout).")
        except RequestException as e:
            print(f"Տեղի է ունեցել սխալ հարցման ընթացքում: {e}")
        # TODO Ավելացնել լոգավորում

        return None

