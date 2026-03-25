import argparse
from api_service import get_weather_data
from ai_service import get_advice
from analytics import get_info


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()

    data = get_weather_data(args.city)

    if data:
        report = get_info(data)
        print (f"\n--- Tecnical information for {args.city} ---")
        print(report)

        print ("\n --- Advice AI ---")
        ai_advice = get_advice(data)
        print(ai_advice)
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()