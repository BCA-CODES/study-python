from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} Name: {video['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name, "time": time})
    print("-" * 50)
    print("Video added successfully!!!")
    print("-" * 50)
    list_videos()

def update_video(video_id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, 
        {"$set": {'name': name, 'time': time}}
    )
    print("-" * 50)
    print("Video details updated successfully!!!")
    print("-" * 50)
    list_videos()

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    print("-" * 50)
    print("Video deleted successfully!!!")
    print("-" * 50)
    list_videos()

def main():
    while True:
        print("\n Youtube Manager with MongoDB")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter a number of your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter a video name: ")
            time = input("Enter a video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter a video ID: ")
            name = input("Enter a video name: ")
            time = input("Enter a video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter a video ID: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()