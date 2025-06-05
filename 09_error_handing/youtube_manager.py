import json

data = 'youtube.txt'

def load_video():
    try:
        with open(data,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_video(videos):
    with open(data, 'w') as file:
        json.dump(videos, file)

def get_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 50)

def add_videos(videos):
    name = input("Enter a video name: ")
    time = input("Enter a video time: ")
    videos.append({"name": name, "time":time})
    save_data_video(videos)
    print("-" * 50)
    print("Video added successfully!!!")
    get_all_videos(videos)

def update_videos(videos):
    get_all_videos(videos)
    update = int(input("Enter a video number to update: "))

    if 1 <= update <= len(videos):
        name = input("Enter a new video name: ")
        time = input("Enter a new video time: ")
        videos[update-1] = {"name": name, "time": time}
        save_data_video(videos)
        print("-" * 50)
        print("Video updated sucessfully!!!")
        get_all_videos(videos)
    else:
        print("Invalid number entered")

def delete_videos(videos):
    get_all_videos(videos)
    delete = int(input("Enter a video number to be deleted: "))

    if 1 <= delete <= len(videos):
        del videos[delete-1]
        save_data_video(videos)
        print("-" * 50)
        print("Video deleted successfully!!!")
        get_all_videos(videos)
    else:
        print("Invalid video number entered")

def main():
    videos = load_video()

    while True:
        print("\n Youtube Manager | Choose any one ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit ")

        choice = input("Enter a choice: ")

        match choice:
            case '1':
                get_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invaild Choice")

if "__main__" == __name__:
    main()