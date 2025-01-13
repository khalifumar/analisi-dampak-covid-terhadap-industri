# Setup Environtment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
conda install -r requirements.txt

# Run Streamlit App
streamlit run yourDashboard.py