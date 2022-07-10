import streamlit as st
import functions,functions_2
import matplotlib.pyplot as plt
st.sidebar.title("Whatsapp Chat Analysis")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = functions.preprocess(data)

    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt,user_list")

    if st.sidebar.button("Show Analysis"):
        num_messages,words,num_media_messages = functions_2.analyse_stats(selected_user,df)0

        col1, col2, col3, = st.beta_columns(3)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
    if selected_user == 'Overall':
        st.title('Busiest User')
        x,new_df = functions_2.busiest_user(df)
        fig, ax = plt.subplots()

        col1,col2 = st.beta_columns(2)

        with col1:
            ax.bar(x.index,x.values)
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)
        with col2:
            st.dataframe(new_df)

common_df = functions_2.most_common_words(selected_user,df)
fig,ax = plt.subplots()
ax.bar(common_df[0],common_df[1])
plt.xticks(rotation='vertical')
st.title('Most used words')
st.pyplot(fig)

emoji_df = functions_2.emoji_helper(selected_user,df)
st.title('Emoji Analysis')
st.dataframe(emoji_df)

st.title("Monthly Analysis")
timeline = functions_2.monthly_analysis(selected_user,df)
fig,ax = plt.subplots()
ax.plot(timeline['time'],timeline['message'])
plt.xticks(rotation='vertical')
st.pyplot(fig)




