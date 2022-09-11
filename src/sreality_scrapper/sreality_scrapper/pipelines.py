# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
import os

class SavingToPostgresPipeline(object):

    def __init__(self):

        self.create_connection()


    def create_connection(self):

        self.database = os.getenv("POSTGRES_DB")
        self.connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=self.database,
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"))

        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS srealitky (
            id SERIAL PRIMARY KEY,
            title TEXT,
            image_url TEXT
        );
        """)


    def process_item(self, item, spider):

        self.store_db(item)
        #we need to return the item below as scrapy expects us to!
        return item

    def store_db(self, item):

        try:
            self.cur.execute(""" INSERT INTO srealitky (title, image_url) VALUES (%s, %s)""", (
                item.title,
                item.image_url
            ))
            self.connection.commit()
        except BaseException as e:
            print(e)
            self.connection.commit()

    def close_spider(self, spider):

        self.cur.close()
        self.connection.close()