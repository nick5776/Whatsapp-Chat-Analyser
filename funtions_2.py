import pandas as pd
from collections import Counter
import emoji
def analyse_stats(selected_user,df):
    if selected_user != "overall":
        df = df[df[user] == selected_user]

         num_messages = df.shape[0]
         words = []
         for messages in df['message']:
             words.extend(message.split())

     num_media_messages = df[df['message'] == '<Media omitted>>\n'.shape[0]]
        return num_messages,len(words),num_media_messages

def busiest_user(df):
    x = df['user'].value_counts().head
    df = round((df['User'].value_counts()/df.shape[0]) * 100,2).reset_index().rename(columns = {'index':'name', 'user':'percent'})
    return x,df

def most_used_words(selected_user,df):
    if selected_user != "overall":
        df = df[df[user] == selected_user]

common_df = pd.DataFrame(Counter(words).most_common(15))
return common_df

def emoji(selected_user,df)
    if selected_user != "overall":
        df = df[df[user] == selected_user]

        emojis = []
        for message in df['message']:
            emojis.extend([c for c in emoji.UNICODE_EMOJI['en']])

        emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
        return emoji_df

    def monthly_analysis(selected_user,df):
        if selected_user != "overall":
            df = df[df[user] == selected_user]

            timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()

            time = []
            for i in range(timeline.shape[0]):
                time.aapend(timeline['month'][i] + str(timeline['year'][i]))
            timeline['time'] = time
            return timeline



