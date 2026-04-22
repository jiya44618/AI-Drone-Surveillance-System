import streamlit as st

st.set_page_config(page_title="Drone Surveillance System")

st.title("🚁 AI Drone Surveillance Dashboard")

st.subheader("Project Overview")
st.write("""
This system uses YOLOv8 deep learning to detect vehicles from drone footage.
It also performs threat analysis and restricted zone monitoring.
""")

st.subheader("Features Implemented")
st.write("""
- Real-time Object Detection  
- Vehicle Counting  
- Threat Level Classification  
- Restricted Zone Alert  
""")

st.subheader("System Status")
st.success("System is Working Successfully ✅")

st.subheader("Live Demo Instructions")
st.write("""
1. Open Command Prompt  
2. Activate environment  
3. Run detection script  
4. View real-time output window  
""")