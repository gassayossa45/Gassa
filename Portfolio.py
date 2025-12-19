import streamlit as st

st.set_page_config(
    page_title="Amedee – Portfolio",
    page_icon="🧠",
    layout="wide",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Gehe zu", ["Über mich", "Projekte", "Skills", "Kontakt"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Links**")
st.sidebar.markdown("[GitHub]( https://github.com/gassayossa45/Projekt)")
st.sidebar.markdown("[LinkedIn]( https://www.linkedin.com/in/amédée-gaël-gassa-yossa-545363396)")

# -------------------------
# Über mich
# -------------------------
if page == "Über mich":
    st.title("Amedee – Automation & Data Analysis Specialist")
    st.write(
        """
Ich bin Spezialist für Automatisierung und Datenanalyse mit Erfahrung in Python, SQL,
Apache Airflow, Docker und modernen Datenplattformen.  
Ich entwickle skalierbare, robuste Lösungen, die Datenflüsse automatisieren,
Cloud-Ressourcen effizient nutzen und klare Einblicke für Stakeholder liefern.
        """
    )

    st.subheader("Was mich auszeichnet")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
- Strukturierte Arbeitsweise  
- Beharrliche Fehlersuche  
- Fokus auf robuste, wartbare Lösungen  
- End-to-End Workflow-Verständnis  
            """
        )

    with col2:
        st.markdown(
            """
- Internationale Offenheit (Remote & Relocation)  
- Audience-aware Kommunikation  
- Teamorientierte Zusammenarbeit  
- Hohe Anpassungsfähigkeit  
            """
        )

# -------------------------
# Projekte
# -------------------------
elif page == "Projekte":
    st.title("Ausgewählte Projekte")

    st.subheader("1. Streamlit/PostgreSQL Online Shop")
    st.write(
        """
Webanwendung mit Benutzerregistrierung, Login, Produktansicht und Bestellübersicht.
Fokus auf Datenintegrität, Benutzerführung und klarer Trennung von Logik und Darstellung.
        """
    )
    st.markdown("**Tech-Stack:** Python, Streamlit, PostgreSQL, Docker")
    st.markdown("[GitHub-Repository öffnen](https://github.com//gassayossa45/Projekt )")

    st.markdown("---")

    st.subheader("2. Airflow Workflow Automation")
    st.write(
        """
Daten-Pipelines mit Apache Airflow zur Automatisierung wiederkehrender Tasks,
inklusive Trennung von Schema-Erstellung und Datenverarbeitung, Logging und Monitoring.
        """
    )
    st.markdown("**Tech-Stack:** Python, Airflow, Docker, SQL")
    st.markdown("[GitHub-Repository öffnen](https://github.com//gassayossa45/Projekt)")

    st.markdown("---")

    st.subheader("3. Weitere Projekte")
    st.write(
        """
Weitere Beispiele für Automatisierung, Datenanalyse und Infrastruktur findest du 
in meinen GitHub-Repositories.
        """
    )
    st.markdown("[GitHub-Profil öffnen](https://github.com//gassayossa45/Projekt)")

# -------------------------
# Skills
# -------------------------
elif page == "Skills":
    st.title("Skills")

    st.subheader("Technische Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
- Python  
- SQL & PostgreSQL  
- Apache Airflow  
- Docker  
- ETL & Data Pipelines
- Power BI
- Excel
- Visual Basic 
            """
        )

    with col2:
        st.markdown(
            """
- Power BI / Tableau  
- Linux & Cloud-Grundlagen  
- Git & GitHub  
- Streamlit  
            """
        )

    st.subheader("Soziale Kompetenz")
    st.markdown(
        """
- Kommunikationsstärke  
- Teamfähigkeit  
- Beharrlichkeit & Problemlösungskompetenz  
- Interkulturelle Zusammenarbeit  
- Anpassungsfähigkeit & Belastbarkeit  
        """
    )

# -------------------------
# Kontakt
# -------------------------
elif page == "Kontakt":
    st.title("Kontakt")

    st.write(
        """
Ich bin offen für internationale Projekte, Remote-Rollen und neue Herausforderungen
im Bereich Automatisierung, Datenanalyse und Workflow-Engineering.
        """
    )

    #st.markdown("📧 **E-Mail:** gassa45@yahoo.com | gassayossa45@gmail.com")
    st.markdown("📧**E-Mail:**[gassa45@yahoo.com](https://compose.mail.yahoo.com/?to=gassa45@yahoo.com)")
    st.markdown("[📧 E-Mail schreiben](https://mail.google.com/mail/?view=cm&fs=1&to=gassa45@yahoo.com)")
    st.markdown("📧 **E-Mail:**[gassayossa45@gmail.com](https://compose.mail.gmail.com/?to=gassayossa45@gmail.com)")

    st.markdown("🔗 **LinkedIn:**  https://www.linkedin.com/in/amédée-gaël-gassa-yossa-545363396")
    st.markdown("💻 **GitHub:**  https://github.com/gassayossa45/Projekt")