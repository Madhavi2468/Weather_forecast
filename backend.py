import requests

# To get below api_key for our weather forcast visit the 'api.openweathermap.org' url"
API_KEY = "1fda4bfe620de28c803f4739ac0edd43"


def get_data(place, forecasted_days):
    # creating the url
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # filtering the data based on our requirements.
    filtered_data = data['list']
    nr_values = 8 * forecasted_days

    # getting the data upto given days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    get_data(place="Nellore", forecasted_days=5)