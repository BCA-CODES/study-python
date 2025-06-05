import requests

def fetch_one():
    url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=hard&type=multiple"

    response = requests.get(url)
    real_data = response.json()

    if "results" in real_data:
        data = real_data["results"]
        correct_answer = data[1]
        return correct_answer
    else:
        raise Exception("failed to load data")

def main():
    try:
        correct_answer = fetch_one()
        print(f"answer: {correct_answer}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
