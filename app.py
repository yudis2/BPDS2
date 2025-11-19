import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pathlib import Path

st.set_page_config(page_title="🎓 Student Performance Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("clean_data.csv")
    return df

df = load_data()

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=80)
st.sidebar.title("🎯 Filter Data")

gender = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=df["Gender"].unique())
status = st.sidebar.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
course = st.sidebar.multiselect("Course", df["Course"].unique(), default=df["Course"].unique())

filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["Status"].isin(status)) &
    (df["Course"].isin(course)) 
]

st.title("🎓 Student Performance Analytics Dashboard")
st.markdown("Interactive visualization to understand student academic performance based on various demographic and academic factors.")


tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "📈 Academic Performance", "🔍 Insights", "🕵🏻 Analyze"])


with tab1:
    st.subheader("📊 Data Overview")
    col1, col2, col3 = st.columns(3)

    col1.metric("Average Admission Grade", round(filtered_df["Admission_grade"].mean(), 2))
    col2.metric("Average Age", round(filtered_df["Age_at_enrollment"].mean(), 1))
    col3.metric("Total Students", len(filtered_df))

    st.markdown("---")

    fig_gender = px.pie(filtered_df, names="Gender", title="Gender Distribution", color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_status = px.pie(filtered_df, names="Status", title="Student Status Distribution", color_discrete_sequence=px.colors.qualitative.Safe)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig_gender, use_container_width=True)
    col2.plotly_chart(fig_status, use_container_width=True)
    
    #inrelevant pie chart but its oke
    # fig_nasional = px.pie(df["Nacionality"].value_counts().nlargest(3).index, names="Nacionality", title="Nationality", color_discrete_sequence=px.colors.qualitative.Safe)
    # fig_age = px.pie(df["Age_at_enrollment"].value_counts().nlargest(3).index, names="Age_at_enrollment", title="Age", color_discrete_sequence=px.colors.qualitative.Safe)
    # col1, col2 = st.columns(2)
    # col1.plotly_chart(fig_nasional, use_container_width=True)
    # col2.plotly_chart(fig_age, use_container_width=True)


with tab2:
    st.subheader("📈 Admission Grade Distribution")
    fig_grade = px.histogram(
        filtered_df, x="Admission_grade", color="Gender",
        nbins=30, barmode='overlay',
        title="Distribution of Admission Grades by Gender",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_grade, use_container_width=True)

    st.subheader("🎯 Course vs Average Grade")
    avg_course = filtered_df.groupby("Course")["Admission_grade"].mean().reset_index()
    fig_course = px.bar(
        avg_course, x="Course", y="Admission_grade",
        title="Average Admission Grade per Course",
        color="Admission_grade", color_continuous_scale="Blues"
    )
    st.plotly_chart(fig_course, use_container_width=True)

    st.subheader("📊 Performance per Semester")
    sem_cols = ["Curricular_units_1st_sem_grade", "Curricular_units_2nd_sem_grade"]
    avg_sem = filtered_df[sem_cols].mean().reset_index()
    avg_sem.columns = ["Semester", "Average Grade"]
    fig_sem = px.bar(avg_sem, x="Semester", y="Average Grade", color="Average Grade", color_continuous_scale="Purples")
    st.plotly_chart(fig_sem, use_container_width=True)

with tab3:
    st.subheader("📉 Correlation Between Numerical Variables")

    numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr()
        fig_corr = px.imshow(
            corr, text_auto=True, aspect="auto",
            title="Correlation Heatmap", color_continuous_scale="RdBu_r"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.warning("Not enough numerical data for correlation analysis.")

with tab4:
    st.write("### 🎓 Student Dropout Prediction System")

    # --------------------------
    # Load Data
    # --------------------------
    @st.cache_data
    def load_data():
        df = pd.read_csv("clean_data.csv")   # Ganti sesuai path Anda
        return df

    @st.cache_resource
    def load_model():
        model = joblib.load(Path(__file__).parent / "modelRF.joblib") 
        return model

    df = load_data()
    model = load_model()

    # --------------------------
    # Optional Mapping (contoh)
    # --------------------------
    education_mapping = {
        1: "SMP",
        2: "SMA",
        3: "Diploma",
        4: "Sarjana",
        5: "Magister"
    }

    # --------------------------
    # Input Features
    # --------------------------
    st.subheader("Input Student Features")

    input_data = {}

    for col in df.columns:

        # Lewati kolom target
        if col in ["Dropout", "dropout", "Status", "label"]:
            continue

        # Contoh jika Anda punya kolom tingkat pendidikan
        if col == "EducationLevel":
            selected_value = st.selectbox(
                f"Select {col}",
                options=list(education_mapping.keys()),
                format_func=lambda x: education_mapping[x]
            )
            input_data[col] = selected_value
            continue

        # Jika kolom kategori (object)
        if df[col].dtype == 'object':
            input_data[col] = st.selectbox(
                f"Select {col}",
                df[col].unique()
            )
        else:
            # Kolom numerik
            input_data[col] = st.number_input(
                f"Input {col}",
                value=float(df[col].mean())
            )

    # --------------------------
    # Predict
    # --------------------------
    if st.button("Predict Dropout"):
        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.subheader("📘 Result Prediction")

        dropout_result = (
            "⚠️ Student predicted Drop Out"
            if prediction[0] == 1
            else "✅ Student predict keep studying"
        )

        st.write(f"**Status Prediksi:** {dropout_result}")
        st.write(f"**Probabilitas Drop Out:** {prediction_proba[0][1]:.2f}")
    
    

st.markdown("---")
st.caption("📘 Data source: Student Dataset | Created By Yudisdwi")
