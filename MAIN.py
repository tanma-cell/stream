


import requests
from streamlit_option_menu import option_menu
from PIL import Image
import webbrowser
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sky Coding",  layout="wide")
image = Image.open('1.webp')


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contacts"],
    icons = ["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css('style.css')
if selected == "Home":   

    
        



    lottie=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")
    with st.container():
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown('<h1 class="big-font">Sky Coding</h1   >', unsafe_allow_html=True)
            st.subheader("Hello, I am Tanmay Gupta. I am young Programmer. Also I have a youtube channel name is SKY CODING")
            st.write("---")
            st.header("Subscriber:")
            st.subheader("128")
            
            st.header("Videos:")
            st.subheader("16")
            st.write("---")

        with right_column:
            st_lottie(lottie, height=500, key="coding")

    with st.container():
        left_column, middle_Colum ,right_column = st.columns(3)
        col1, col2, col3 = st.columns([1,1,1])

        with middle_Colum:

                    

            with col2:
                if st.button("My Channel"):
                    webbrowser.open_new_tab('https://www.youtube.com/channel/UCgAtkIFTM2ks5Atr6G69KLQ')
if selected == "Projects":


    ani = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_eeuhulsy.json')

    with st.container():
        
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown("""
                                <style>
                                .big-font {
                                    font-size:70px !important;
                                }
                                </style>
                            """, unsafe_allow_html=True)

                st.markdown('<h1 class="big-font">My Projects</h1   >', unsafe_allow_html=True)
                
 

            with right_column:
                st_lottie(ani, height=150, key="coding")

            st.write("---")   

    with st.container():
        
        
        st.write("##")
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image, width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Making Notes App</h1   >', unsafe_allow_html=True)
            
            if st.button("Watch  ''Making Notes App''  Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=c_9JtGKq8Rs")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image='https://i.ytimg.com/vi/a8gfO1VRzng/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLD0KpaBf_nVXN1QHtN6ATJdxMpVTg', width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Image To Url convertor</h1   >', unsafe_allow_html=True)
            
            if st.button("Watch  ''Image To Url convertor''  Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=a8gfO1VRzng")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image='https://i.ytimg.com/vi/Wj6D1FMv7jY/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLCnoGuiB8PHJk5AapccGg70n0snzA', width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Hack Whatspp using Python</h1   >', unsafe_allow_html=True)

            if st.button("Watch ''Hack Whatspp using Python'' Video" ):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=Wj6D1FMv7jY")          
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image='https://i.ytimg.com/vi/rNonGSIS-kI/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLCqYF5Y-LhaEobussTtK2HahxcYbQ', width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Auto Text Writer in Python</h1   >', unsafe_allow_html=True)

            if st.button("Watch ''Auto Text Writer in Python'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=rNonGSIS-kI")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image="https://i.ytimg.com/vi/t-KOYjJWvD4/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLC5qo1yQyT9N2E5jBioQDO3elD4eg", width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Phone Information provider in Python</h1   >', unsafe_allow_html=True)

            if st.button("Watch ''Phone Information provider in Python'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=t-KOYjJWvD4&t=171s")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image='https://i.ytimg.com/vi/r2D2_lxDoV0/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLCD1WH7-AoPKVqPW0mFum6jXgM3XQ', width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Hack Google Chrome Dino Game</h1   >', unsafe_allow_html=True)
            if st.button("Watch ''Hack Google Chrome Dino Game'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=r2D2_lxDoV0")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image="https://i.ytimg.com/vi/qLZr5VciN-c/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLDDS3RDw7-LKqlQwIpgrB4Z9MaobA", width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Instagram Clone in code.org</h1   >', unsafe_allow_html=True)
            if st.button("Watch ''Instagram Clone in code.org'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=qLZr5VciN-c")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image="https://i.ytimg.com/vi/05eRjzZyX3I/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLCH4ejlLBUWNJ8kjvg-wvZT9VaD0A", width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Google Meet Clone in Code.org</h1   >', unsafe_allow_html=True)
            if st.button("Watch ''Google Meet Clone in Code.org'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=05eRjzZyX3I")
    with st.container():
        
        st.write("---")
        
        img_colo, text_colo = st.columns((1,2)) 
        with img_colo:
            st.image(image='https://i.ytimg.com/vi/YIeINBiSwTo/hqdefault.jpg?s…AFwAcABBg==&rs=AOn4CLCELd1sHDsoNXkKwqxjd8apGDq48A', width=400)

        with text_colo:
            st.markdown('<h1 class="bold-font">Making a browser in code.org</h1   >', unsafe_allow_html=True)
            if st.button("Watch ''Making a browser in code.org'' Video"):
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=YIeINBiSwTo")
if selected == "Contacts":
    st.header("Get in touch with me!")
    st.write("##")

    contact_form= """
    <form action="https://formsubmit.co/tanmaygupta735@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Enter Your Name" required>
     <input type="email" name="email" placeholder="Enter Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>   
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        anio = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_u25cckyh.json')
        st_lottie(anio, height=300  , key="coding")

    
            
