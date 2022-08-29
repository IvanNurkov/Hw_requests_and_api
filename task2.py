from pip._vendor import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def upload(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'True'}
        headers = self.get_headers()
        link_dickt = requests.get(url, headers = headers, params = params).json()
        href = link_dickt.get('href', '')
        post_ = requests.put(href, data = open(file_path, 'rb'))
        return print(post_.status_code)

if __name__ == '__main__':
    path_to_file = 'Text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
