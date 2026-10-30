import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, roc_auc_score
)

st.set_page_config(page_title="AI Model Lab", page_icon="🧠", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#081225 0%,#101d35 55%,#172642 100%); color:#f4f7ff;}
[data-testid="stSidebar"] {background:#0b1427;}
.block-container {padding-top:2rem; max-width:1450px;}
h1,h2,h3,p,label {color:#f4f7ff !important;}
.hero {padding:28px 32px;border:1px solid #2b4266;border-radius:22px;
background:linear-gradient(120deg,#172d50,#17213b);margin-bottom:22px;}
.hero small {color:#a9c2e8;}
.metric {background:#142642;border:1px solid #294568;padding:18px;border-radius:16px;}
div[data-testid="stMetric"] {background:#142642;padding:15px;border:1px solid #294568;border-radius:14px;}
.stButton>button {background:#4f8cff;color:white;border:0;border-radius:10px;padding:10px 20px;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def load_uci():
    ds = fetch_ucirepo(id=350)
    X = ds.data.features.copy()
    y = ds.data.targets.iloc[:, 0].copy()
    ids = [c for c in X.columns if c.lower() in ["id","client_id","customer_id"]]
    X = X.drop(columns=ids, errors="ignore")
    keep = y.notna()
    return X.loc[keep].reset_index(drop=True), y.loc[keep].reset_index(drop=True), ds.metadata

def build_pipeline(model_name, X):
    numeric = X.select_dtypes(include=np.number).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scale", StandardScaler())
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    prep = ColumnTransformer([
        ("num", numeric_pipe, numeric),
        ("cat", categorical_pipe, categorical)
    ])
    if model_name == "Decision Tree":
        clf = DecisionTreeClassifier(max_depth=5, min_samples_split=20,
            min_samples_leaf=10, class_weight="balanced", random_state=42)
    elif model_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=7, weights="distance")
    else:
        clf = RandomForestClassifier(n_estimators=250, max_depth=None,
            min_samples_split=5, class_weight="balanced", random_state=42,
            n_jobs=-1)
    return Pipeline([("prep", prep), ("model", clf)])

@st.cache_data(show_spinner="UCI dataset yuklanmoqda...")
def cached_data():
    return load_uci()

st.sidebar.title("🧠 AI Model Lab")
st.sidebar.caption("Machine Learning Comparison Studio")
page = st.sidebar.radio("Bo‘limlar", [
    "Dashboard", "Model Training", "Model Comparison", "Model Details"
])
st.sidebar.markdown("---")
st.sidebar.write("**Dataset:** UCI ID 350")
st.sidebar.write("**Algoritmlar:** 3 ta")

st.markdown("""
<div class="hero">
  <small>ARTIFICIAL INTELLIGENCE • MACHINE LEARNING</small>
  <h1>AI Model Comparison Lab</h1>
  <p>Decision Tree, KNN va Random Forest algoritmlarini bitta platformada o‘qiting,
  baholang va natijalarini taqqoslang.</p>
</div>
""", unsafe_allow_html=True)

try:
    X, y_raw, metadata = cached_data()
except Exception as e:
    st.error(f"Datasetni yuklashda xatolik: {e}")
    st.info("Internet aloqasini tekshiring. Dataset UCI repository orqali yuklanadi.")
    st.stop()

le = LabelEncoder()
y = pd.Series(le.fit_transform(y_raw.astype(str)), name="target")
class_names = [str(c) for c in le.classes_]

with st.sidebar:
    st.caption(f"Qatorlar: {len(X):,} | Belgilar: {X.shape[1]}")

if "results" not in st.session_state:
    st.session_state.results = None

if page == "Dashboard":
    st.subheader("Loyiha ko‘rsatkichlari")
    a,b,c,d = st.columns(4)
    a.metric("Dataset qatorlari", f"{len(X):,}")
    b.metric("Xususiyatlar", X.shape[1])
    c.metric("Sinflar", len(class_names))
    d.metric("Algoritmlar", "3")
    st.markdown("### Dataset namunasi")
    st.dataframe(X.head(10), use_container_width=True)
    left,right = st.columns(2)
    with left:
        st.markdown("### Target taqsimoti")
        counts = y_raw.astype(str).value_counts()
        fig, ax = plt.subplots(figsize=(6,4))
        counts.plot(kind="bar", ax=ax)
        ax.set_xlabel("Sinf"); ax.set_ylabel("Soni"); ax.set_title("Target distribution")
        plt.xticks(rotation=25); st.pyplot(fig); plt.close(fig)
    with right:
        st.markdown("### Ma’lumotlar sifati")
        missing = X.isna().sum().sort_values(ascending=False).head(12)
        fig, ax = plt.subplots(figsize=(6,4))
        missing.sort_values().plot(kind="barh", ax=ax)
        ax.set_title("Bo‘sh qiymatlar"); ax.set_xlabel("Soni")
        st.pyplot(fig); plt.close(fig)
    st.caption("Target qiymatlari modelga berishdan oldin avtomatik raqamli kodga o‘tkaziladi.")

elif page == "Model Training":
    st.subheader("Modellarni o‘qitish")
    st.write("Uchala algoritm bir xil train/test bo‘linishida baholanadi.")
    test_size = st.slider("Test ulushi (%)", 10, 40, 20, 5)
    stratify_opt = st.checkbox("Sinflar nisbatini saqlash (stratify)", value=True)
    if st.button("🚀 Uchala modelni o‘qitish", use_container_width=True):
        try:
            strat = y if stratify_opt and y.value_counts().min() >= 2 else None
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size/100, random_state=42, stratify=strat
            )
            output = {}
            progress = st.progress(0)
            for i, name in enumerate(["Decision Tree", "KNN", "Random Forest"]):
                pipe = build_pipeline(name, X)
                pipe.fit(X_train, y_train)
                pred = pipe.predict(X_test)
                average = "binary" if len(class_names) == 2 else "weighted"
                kwargs = {"average": average, "zero_division": 0}
                if average == "binary":
                    kwargs["pos_label"] = 1
                metrics = {
                    "Accuracy": accuracy_score(y_test, pred),
                    "Precision": precision_score(y_test, pred, **kwargs),
                    "Recall": recall_score(y_test, pred, **kwargs),
                    "F1-score": f1_score(y_test, pred, **kwargs)
                }
                output[name] = {
                    "pipeline": pipe, "pred": pred, "y_test": y_test,
                    "metrics": metrics, "X_test": X_test
                }
                progress.progress((i+1)/3)
            st.session_state.results = output
            st.success("Barcha modellar muvaffaqiyatli o‘qitildi!")
        except Exception as e:
            st.error(f"Modelni o‘qitishda xatolik: {e}")

    if st.session_state.results:
        rows = [{"Model": n, **v["metrics"]} for n,v in st.session_state.results.items()]
        st.dataframe(pd.DataFrame(rows).set_index("Model").style.format("{:.3f}"),
                     use_container_width=True)
        st.info("Batafsil grafiklar uchun chap menyudan Model Comparison yoki Model Details bo‘limini oching.")

elif page == "Model Comparison":
    st.subheader("Natijalarni taqqoslash")
    if not st.session_state.results:
        st.warning("Avval Model Training bo‘limida modellarni o‘qiting.")
    else:
        result = st.session_state.results
        df = pd.DataFrame({n:v["metrics"] for n,v in result.items()}).T
        cols = st.columns(4)
        for col, metric in zip(cols, df.columns):
            best = df[metric].idxmax()
            col.metric(metric, f"{df.loc[best,metric]*100:.2f}%", best)
        st.markdown("### Ko‘rsatkichlar grafigi")
        fig, ax = plt.subplots(figsize=(10,5))
        (df*100).plot(kind="bar", ax=ax)
        ax.set_ylabel("Foiz (%)"); ax.set_ylim(0,105); ax.set_xlabel("")
        ax.legend(loc="lower right"); plt.xticks(rotation=0)
        st.pyplot(fig); plt.close(fig)
        st.markdown("### Natijalar jadvali")
        st.dataframe((df*100).round(2).rename_axis("Model"), use_container_width=True)
        st.markdown("### Confusion Matrix")
        chosen = st.selectbox("Modelni tanlang", list(result.keys()))
        cm = confusion_matrix(result[chosen]["y_test"], result[chosen]["pred"])
        fig, ax = plt.subplots(figsize=(6,5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                    xticklabels=class_names, yticklabels=class_names, ax=ax)
        ax.set_xlabel("Bashorat"); ax.set_ylabel("Haqiqiy qiymat")
        ax.set_title(f"{chosen} — Confusion Matrix")
        st.pyplot(fig); plt.close(fig)

elif page == "Model Details":
    st.subheader("Model tahlili")
    if not st.session_state.results:
        st.warning("Avval Model Training bo‘limida modellarni o‘qiting.")
    else:
        result = st.session_state.results
        chosen = st.selectbox("Model", list(result.keys()))
        item = result[chosen]
        st.markdown("### Classification Report")
        report = classification_report(item["y_test"], item["pred"],
            target_names=class_names, output_dict=True, zero_division=0)
        st.dataframe(pd.DataFrame(report).T.round(3), use_container_width=True)
        pipe = item["pipeline"]
        prep = pipe.named_steps["prep"]
        clf = pipe.named_steps["model"]
        feature_names = prep.get_feature_names_out()
        if hasattr(clf, "feature_importances_"):
            imp = pd.Series(clf.feature_importances_, index=feature_names).nlargest(15).sort_values()
            st.markdown("### Eng muhim 15 ta xususiyat")
            fig, ax = plt.subplots(figsize=(9,6))
            imp.plot(kind="barh", ax=ax); ax.set_xlabel("Importance")
            st.pyplot(fig); plt.close(fig)
        else:
            st.info("KNN algoritmida Decision Tree yoki Random Forest kabi feature importance mavjud emas.")
        if chosen == "Decision Tree":
            st.markdown("### Decision Tree grafigi")
            fig, ax = plt.subplots(figsize=(22,10))
            plot_tree(clf, feature_names=list(feature_names),
                class_names=class_names, filled=True, rounded=True,
                fontsize=7, max_depth=4, ax=ax)
            st.pyplot(fig); plt.close(fig)
        if len(class_names) == 2 and hasattr(clf, "predict_proba"):
            y_score = pipe.predict_proba(item["X_test"])[:, 1]
            fpr, tpr, _ = roc_curve(item["y_test"], y_score)
            auc = roc_auc_score(item["y_test"], y_score)
            st.markdown(f"### ROC Curve — AUC: **{auc:.4f}**")
            fig, ax = plt.subplots(figsize=(7,5))
            ax.plot(fpr,tpr,label=f"{chosen} (AUC={auc:.3f})")
            ax.plot([0,1],[0,1],"--"); ax.set_xlabel("False Positive Rate")
            ax.set_ylabel("True Positive Rate"); ax.legend()
            st.pyplot(fig); plt.close(fig)
        else:
            st.caption("ROC-AUC grafigi faqat ikki sinfli target uchun chiqariladi.")

st.markdown("---")
st.caption("AI Model Lab • Decision Tree | KNN | Random Forest • UCI Dataset 350")
