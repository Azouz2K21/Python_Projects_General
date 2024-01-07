
import psycopg2
from datetime import datetime
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['postgresql']

# Function to save sudo data to PostgreSQL
def save_sudo_data():
    # Example sudo data (replace this with actual sudo data)
    sudo_temperature = 28.0
    sudo_humidity = 60.0

    # Read database configuration
    db_config = read_config()

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        database=db_config['database'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )

    # Create a cursor
    cur = conn.cursor()

    # Insert data into PostgreSQL
    try:
        cur.execute("INSERT INTO weather_data (temperature, humidity, timestamp) VALUES (%s, %s, %s)",
                    (sudo_temperature, sudo_humidity, datetime.now()))
        conn.commit()
        print("Sudo Data saved successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        # Close communication with the database
        cur.close()
        conn.close()

if __name__ == "__main__":
    save_sudo_data()
