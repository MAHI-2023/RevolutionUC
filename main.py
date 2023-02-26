#importing packages
from utils import *
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi

#setting up the web page width
st.set_page_config(layout="wide")


st.markdown("<h1 style='text-align: center; color: #6C244C; font-size: 60px;'>Sign Speller 🧏 </h1>", unsafe_allow_html=True)
st.markdown("***")
st.subheader("find your sign titles below :point_down: :")
st.markdown("--")

#getting the input and processing it
video_URL = st.sidebar.text_input('Enter YouTube video URL: :point_down: ', 'https://www.youtube.com/watch?v=fN1Cyr0ZK9M')
video_id = video_URL.split('=')[-1]

#video is displayed upon entering the video URL
st.sidebar.video(video_URL)

#extracting the video subtitles
srt = YouTubeTranscriptApi.get_transcript(video_id)
srt = pd.DataFrame(srt)
srt = srt.text.to_list()

#converting the subtitles in sign language
speech_in_images = get_speech_images(srt)

st.set_option('deprecation.showPyplotGlobalUse', False)

#displaying the output on web page
for i in range(len(srt)):
    st.write(srt[i])
    display_speech_image(speech_in_images[i])






