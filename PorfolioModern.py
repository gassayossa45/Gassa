import streamlit as st
import base64
from PIL import Image
#from streamlit_pdf_viewer import pdf_viewer


# ---------------------------------------------------------
# Grundeinstellungen
# ---------------------------------------------------------
st.set_page_config(
    page_title="Amedee – Portfolio",
    page_icon="🧠",
    layout="wide",
)

# ---------------------------------------------------------
# Header / Logo-Bereich
# ---------------------------------------------------------
def render_header():
    col1, col2 = st.columns([1, 4])
    with col1:
        try:
            st.image("lebenslauf_self.jpg", width=90)
        except Exception:
            st.write("")
    with col2:
        st.markdown(
            """
            <div style="padding-top:10px;">
                <span style="font-size:28px; font-weight:700;">Amedee Gael Gassa Yossa</span><br>
                <span style="font-size:16px; color:#9CA3AF;">
                 Elektrotechnik Ingenieur • Software Entwickler • Automation & Data Analysis • Python • SQL • Airflow • Docker
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("---")


# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Seite auswählen", ["Über mich", "Projekte", "Skills", "Kontakt"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Links**")
st.sidebar.markdown("[GitHub](https://github.com/gassayossa45/Projekt)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/amédée-gaël-gassa-yossa-545363396)")

# Header auf allen Seiten
render_header()

# ---------------------------------------------------------
# ÜBER MICH
# ---------------------------------------------------------
if page == "Über mich":
    st.subheader("Über mich")

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            #st.image("lebenslauf_self.jpg", width=260)
            st.write("")
        except Exception:
            st.info("Profilbild: Datei 'lebenslauf_self.jpg' noch nicht vorhanden.")

    with col2:
        st.write(
            """
Ich bin Spezialist für Automatisierung, Datenanalyse und Workflow-Engineering mit Erfahrung in Python, SQL,
Apache Airflow, Docker und modernen Datenplattformen.

Ich entwickle skalierbare, robuste Lösungen, die Datenflüsse automatisieren, Cloud-Ressourcen effizient nutzen
und verständliche Einblicke für technische und nicht-technische Stakeholder liefern.
            """
        )

        st.markdown("#### Was mich auszeichnet")
        st.markdown(
            """
- Strukturierte, analytische Arbeitsweise  
- Beharrliche Fehlersuche und Troubleshooting  
- Audience-aware Kommunikation (komplexe Themen verständlich erklären)  
- Internationale Offenheit (Remote & Relocation möglich)  
- Fokus auf robuste, wartbare, praxisnahe Lösungen  
            """
        )

# ---------------------------------------------------------
# PROJEKTE
# ---------------------------------------------------------
elif page == "Projekte":
    st.subheader("Ausgewählte Projekte")

    # Projekt 1
    st.markdown("### Streamlit/PostgreSQL Online Shop")
    st.write(
        """
Webanwendung mit Benutzerregistrierung, Login, Produktansicht und Bestellübersicht.
Fokus auf Datenintegrität, Benutzererlebnis und klare Trennung von Logik und Darstellung.
        """
    )
    st.markdown("**Tech-Stack:** Python, Streamlit, PostgreSQL, Docker")
    st.markdown("[GitHub-Repository öffnen](https://github.com/gassayossa45/Projekt)")

    st.markdown("---")

    # Projekt 2
    st.markdown("### Airflow Workflow Automation")
    st.write(
        """
Daten-Pipelines mit Apache Airflow zur Automatisierung wiederkehrender Tasks,
inklusive Trennung von Schema-Erstellung und Datenverarbeitung, Logging und Monitoring.
        """
    )
    st.markdown("**Tech-Stack:** Python, Airflow, Docker, SQL")
    st.markdown("[GitHub-Repository öffnen](https://github.com/gassayossa45/Projekt)")

    st.markdown("---")

    # Projekt 3 – allgemeiner Verweis
    st.markdown("### Weitere Projekte")
    st.write(
        """
Weitere Beispiele für Automatisierung, Datenanalyse und Infrastruktur findest du 
in meinen GitHub-Repositories. Dort dokumentiere ich auch Lernpfade, Experimente
und Prototypen.
        """
    )
    st.markdown("[Alle Projekte auf GitHub ansehen](https://github.com/gassayossa45/Projekt)")

# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
elif page == "Skills":
    st.subheader("Skills")

    st.markdown("#### Technische Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
- Python  
- SQL & PostgreSQL  
- Apache Airflow  
- Docker  
- ETL & Data Pipelines  
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

    st.markdown("#### Soziale Kompetenz")
    st.markdown(
        """
- Kommunikationsstärke – technische Inhalte klar und zielgruppengerecht vermitteln  
- Teamfähigkeit – Zusammenarbeit in interdisziplinären und internationalen Teams  
- Beharrlichkeit & Problemlösungskompetenz – auch in komplexen Situationen  
- Interkulturelle Zusammenarbeit – offen für unterschiedliche Arbeitskulturen  
- Anpassungsfähigkeit & Belastbarkeit – fokussiert auch unter Zeitdruck  
        """
    )

# ---------------------------------------------------------
# KONTAKT
# ---------------------------------------------------------
elif page == "Kontakt":
    st.subheader("Kontakt & Lebenslauf")

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            #st.image("lebenslauf_self.jpg", width=220)
            st.write("")
        except Exception:
            st.info("Profilbild: Datei 'lebenslauf_self.jpg' noch nicht vorhanden.")

    with col2:
        st.write(
            """
Ich bin offen für internationale Projekte, Remote-Rollen und neue Herausforderungen im Bereich
Automatisierung, Datenanalyse und Workflow-Engineering.
            """
        )

        st.markdown("### E-Mail schreiben")

        # Gmail Button
        st.markdown(
            """
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gassa45@yahoo.com" 
            target="_blank" style="text-decoration:none;">
                <button style="
                    padding:10px 18px; 
                    border-radius:8px; 
                    border:none; 
                    background:#EA4335; 
                    color:white;
                    margin-bottom:6px;
                    cursor:pointer;">
                    Gmail öffnen
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

        # Yahoo Button
        st.markdown(
            """
            <a href="https://compose.mail.yahoo.com/?to=gassa45@yahoo.com" 
            target="_blank" style="text-decoration:none;">
                <button style="
                    padding:10px 18px; 
                    border-radius:8px; 
                    border:none; 
                    background:#6001D2; 
                    color:white;
                    margin-bottom:6px;
                    cursor:pointer;">
                    Yahoo Mail öffnen
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

        # Standard-Mailprogramm
        st.markdown(
            """
            <a href="mailto:gassa45@yahoo.com" 
            style="text-decoration:none;">
                <button style="
                    padding:10px 18px; 
                    border-radius:8px; 
                    border:none; 
                    background:#0F9D58; 
                    color:white;
                    cursor:pointer;">
                    Standard-Mailprogramm
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.subheader("📞 Kontakt")

        st.write("Wenn Sie mich erreichen möchten:")

        st.markdown("""
        **Telefon:** +49 152 13629046   
        """)
# --- Lebenslauf Download ---
st.markdown("### 📄 Lebenslauf herunterladen")

with open("Lebenslaufgassa.pdf", "rb") as pdf:
    pdf_bytes = pdf.read()

st.download_button(
    label="📥 Lebenslauf als PDF herunterladen",
    data=pdf_bytes,
    file_name="Lebenslaufgassa.pdf",
    mime="application/pdf"
)


