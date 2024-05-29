def process_comments(response_items):
    comments = []
    for comment in response_items:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        comment_info = {'author': author, 'comment': comment_text, 'published_at': publish_time}
        comments.append(comment_info)
    print(f'Finished processing {len(comments)} comments.')
    return comments

def main():
    import os
    import googleapiclient.discovery
    import pandas as pd


    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""  # Replace with your actual API key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="q8q3OFFfY6c"  # Replace with your actual video ID
    )
    response = request.execute()

    comments = process_comments(response['items'])
    
    # converting comments to a dataframe
    df = pd.DataFrame(comments)
    
    df.to_csv('comments.csv', index = False)
    
    
        

if __name__ == "__main__":
    main()
