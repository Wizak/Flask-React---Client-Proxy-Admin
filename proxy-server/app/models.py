from inspect import stack
from multiprocessing.spawn import prepare


class DataBase:
    __stack_data = []
    

    @classmethod
    def set_data(cls, data):
        if data:
            cls.__stack_data.append(data)
        else:
            raise ValueError('Missing data')


    @classmethod
    def get_data(cls):
        prepare_data = []
        if cls.__stack_data:
            for id_, data in enumerate(cls.__stack_data):
                body_data = {
                    'id': id_ + 1,
                    'end_user_id': data['end_user_id'],
                    'web_page_url': data['web_page_url'],
                    'date': data['date']
                }
                prepare_data.append(body_data)
        return prepare_data


    @classmethod
    def pag_data(cls, data, pagRows):
        from_rows = (pagRows['page'] - 1) * pagRows['perPage']
        to_rows = pagRows['page'] * pagRows['perPage']
        
        total = len(data)
        pag_data = data[from_rows:to_rows]
        return pag_data, total
    

    @classmethod
    def sort_data(cls, data, sortColumn):
        sorted_data = sorted(data, key=lambda item: item[sortColumn['field']])
        if sortColumn['order'] == 'DESC':
            sorted_data = sorted_data[::-1]
        return sorted_data
