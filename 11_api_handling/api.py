import requests

def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"

    response = requests.get(url)
    real_data = response.json()

    if real_data["success"] and "data" in real_data:
        bookData = real_data["data"]
        bookName = bookData["volumeInfo"]["title"]
        author = bookData["volumeInfo"]["authors"]
        publisher = bookData["volumeInfo"]["publisher"]
        pdf = bookData["accessInfo"]["pdf"]["acsTokenLink"]
        return bookName, author, publisher, pdf 
    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        bookName, author, publisher, pdf = fetch_api()
        print(f"Book name: {bookName} \nBook author: {author} \nBook publisher: {publisher} \nPDF Token: {pdf}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main() 