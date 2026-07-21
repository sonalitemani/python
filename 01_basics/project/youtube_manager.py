import json
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def list_of_videos(videos):
    
    
    for i ,video in enumerate(videos,start=1):
        print(f"{i}. Video name: {video['name']} , duration: {video['time']}")
   
  
        
def save_video(videos):
    with open ('youtube.txt','w') as file:
        json.dump(videos,file)
        
def add_a_video(videos):
    name = input('Enter the name of the video :')
    time = input('Enter the time of the video :')
    videos.append({'name':name,'time':time})
    save_video(videos)

def update_a_video(videos):
    index = int(input('Enter the video number to be updated : '))

    if 1 <= index <= len(videos):
        name = input('Enter the updated name :')
        time = input('Enter the updated time :')
        videos[index-1]= {'name' : name, 'time' : time}
        save_video(videos)
    else:
        print('invalid input')

def delete_a_video(videos):
    index = int(input('Enter the video number to be deleted : '))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_video(videos)
    else:
        print('invalid input')


def main():
    videos =load_data()
    while True:
        print("\n YOUTUBE VIDEO MANAGER |choose an option")
        print("1. list of video")
        print("2. add a video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit")

        choice = input('Enter your choice : ')
        match choice:
            case '1':
                list_of_videos(videos)
            case '2':
                add_a_video(videos)
            case '3':
                update_a_video(videos)
            case '4':
                delete_a_video(videos)
            case '5':
                break
            case _:
                print("Invalid input try again")    
        
if __name__ == '__main__':
    main()        
            
        
        