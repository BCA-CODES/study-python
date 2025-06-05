import sqlite3

conn = sqlite3.connect("youtube_video.py")
cursor = conn.cursor()

cursor.execute('''
    create table if not exists videos(
        Id integer primary key,
        Name text not null,
        Time text not null
               )
''')

def list_all_videos():
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")

def add_video(name, time):
    cursor.execute("insert into videos(name, time) values(?, ?)", (name, time))
    conn.commit()
    print("-" * 50)
    print("Video Added Successfully!!!")
    print("-" * 50)
    list_all_videos()

def update_video(video_id, new_name, new_time):
    cursor.execute("update videos set name = ?, time = ? where id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("-" * 50)
    print("Video Updated Successfully!!!")
    print("-" * 50)
    list_all_videos()

def delete_video(video_id):
    cursor.execute("delete from videos where id = ?", (video_id,))
    conn.commit()
    print("-" * 50)
    print("Video Deleted Successfully!!!")
    print("-" * 50)
    list_all_videos()

def main():
    while True:
        print("---------- Youtube video manager | choose any one ----------")
        print("1. list all videos ")
        print("2. Add a video ")
        print("3. Update video ")
        print("4. Delete video ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter a video name: ")
            time = input("Enter a video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video id to update: ")
            name = input("Enter a video name: ")
            time = input("Enter a video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    
    conn.close()


if __name__ == "__main__":
    main()