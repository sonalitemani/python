import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT,
    time TEXT
    )
''')

def list_of_videos():
    cursor.execute('''
    SELECT * FROM videos
    ''')
    for video in cursor.fetchall():
        print(video)

def add_a_video(name , time):
    cursor.execute('''
    INSERT INTO videos (name,time)values(?,?)
    ''',(name,time))
    conn.commit()
    print('video added')


def update_a_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name=? , time=? where id=?",(name,time,video_id))
    conn.commit()
    print('video updated')


def delete_a_video(video_id):
    cursor.execute("DELETE FROM videos where id=?",(video_id,))
    conn.commit()
    print('video deleted')

def main():
    while True:
        print("\n Youtube Video Manager | Choose an option")
        print("1. List of videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input('Enter your choice :')
        match choice:
            case '1':
                list_of_videos()
            case '2':
                name = input('Enter the name of the video :')
                time = input('Enter the time of the video :')
                add_a_video(name,time)
            case '3':
                video_id = input('Enter a video id to update : ')
                name = input('Enter the name of the video :')
                time = input('Enter the time of the video :')
                update_a_video(video_id , name, time)
            case '4':
                video_id = input('Enter a video id to update : ')
                delete_a_video(video_id)
            case '5':
                break
            case _:
                print("Invalid input try again")

    conn.close()


if __name__ == '__main__':
    main()
