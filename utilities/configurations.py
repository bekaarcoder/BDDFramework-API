import configparser
import psycopg2


def get_configuration():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\shash\\PycharmProjects\\BackendAutomation\\utilities\\properties.ini')
    return config


connect_config = {
    'host': get_configuration()['SQL']['host'],
    'database': get_configuration()['SQL']['database'],
    'user': get_configuration()['SQL']['user'],
    'password': get_configuration()['SQL']['password'],
}


def db_connect():
    try:
        conn = psycopg2.connect(**connect_config)
        if conn.status:
            print("Connection Successful!")
        return conn
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)
