from api_service import get_weather_data
from analytics import get_info
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("city", help="Name of the city")
args = parser.parse_args()

def main():
    data = get_weather_data(args.city)
    report = get_info(data)
    print(report)
if __name__ == "__main__":
    main()