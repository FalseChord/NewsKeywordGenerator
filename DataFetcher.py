import os
import requests
from datetime import datetime
from dateutil.rrule import rrule, DAILY
import gzip
import shutil
import time


class DataFetcher:
    def __init__(self, base_url: str, start_date: datetime, end_date: datetime, target_dir: str):
        self.__base_url = base_url
        self.__start_date = start_date
        self.__end_date = end_date
        self.__target_dir = target_dir

    def execute(self, post_action=None):
        for date in list(rrule(freq=DAILY, dtstart=self.__start_date, until=self.__end_date, interval=1)):
            target_url = self.__get_url(date)
            http_response = self.__fetch_data_from_target_url_through_date(target_url)
            file_path = self.__write_http_content_to_file(http_response=http_response, target_url=target_url)
            print("{} saved.".format(file_path))
            if post_action is not None:
                post_action(file_path)

            time.sleep(2)

    def __get_url(self, date):
        date_in_string = date.strftime("%Y%m%d")
        target_url = self.__base_url.format(date_in_string)

        return target_url

    def __fetch_data_from_target_url_through_date(self, target_url: str):
        print("download: {}".format(target_url))
        response = requests.get(target_url)
        print("done")

        return response

    def __write_http_content_to_file(self, http_response, target_url: str):
        file_name = target_url.rsplit("/", 1)[1]
        file_path = os.path.join(self.__target_dir, file_name)

        with open(file_path, 'wb') as file:
            file.write(http_response.content)

        return file_path


class DataExtractor:
    def execute(self, source_file_path):
        target_file_path = self.__get_target_file_path(source_file_path)

        with gzip.open(source_file_path, 'rb') as gzip_file:
            with open(target_file_path, 'wb') as unzipped_file:
                shutil.copyfileobj(gzip_file, unzipped_file)

        print("extract {} to {}.".format(source_file_path, target_file_path))

    def __get_target_file_path(self, source_file_path):
        source_file_name = os.path.basename(source_file_path)
        split_source_file_name = os.path.splitext(source_file_name)

        filename_without_extension = split_source_file_name[0]
        extracted_extension = split_source_file_name[1]
        target_file_name = "{}{}".format(filename_without_extension, extracted_extension)

        target_file_path = os.path.join(os.path.dirname(source_file_path), target_file_name)

        return target_file_path


if __name__ == '__main__':
    target_dir = os.path.join("news")
    os.makedirs(target_dir, exist_ok=True)

    zipped_base_url = "http://g0v-data.gugod.org/people-in-news/db/articles-{}.jsonl.gz"
    zipped_start_date = datetime(2018, 10, 19)
    zipped_end_date = datetime(2018, 12, 20)
    DataFetcher(
        base_url=zipped_base_url, start_date=zipped_start_date, end_date=zipped_end_date, target_dir=target_dir
    ).execute()
