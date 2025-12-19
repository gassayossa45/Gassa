import streamlit as st
import base64
from PIL import Image

# ---------------------------------------------------------
# Grundeinstellungen
# ---------------------------------------------------------
st.set_page_config(
    page_title="Amedee – Portfolio",
    page_icon="🧠",
    layout="wide",
)

# ---------------------------------------------------------
# Sprachsystem
# ---------------------------------------------------------

# Sprachwahl in der Sidebar
language = st.sidebar.selectbox(
    "Sprache / Language / Langue",
    ("Deutsch", "English", "Français")
)

# Zentrales Text-Wörterbuch
texts = {
    "Deutsch": {
        "nav_title": "Navigation",
        "nav_about": "Über mich",
        "nav_projects": "Projekte",
        "nav_skills": "Skills",
        "nav_contact": "Kontakt",
        "links": "Links",
        "github": "GitHub",
        "linkedin": "LinkedIn",

        "header_role": "Elektrotechnik Ingenieur • Software Entwickler • Automation & Data Analysis • Python • SQL • Airflow • Docker",

        "about_title": "Über mich",
        "about_text": (
            "Ich bin Spezialist für Automatisierung, Datenanalyse und Workflow-Engineering mit "
            "Erfahrung in Python, SQL, Apache Airflow, Docker und modernen Datenplattformen.\n\n"
            "Ich entwickle skalierbare, robuste Lösungen, die Datenflüsse automatisieren, "
            "Cloud-Ressourcen effizient nutzen und verständliche Einblicke für technische und "
            "nicht-technische Stakeholder liefern."
        ),
        "about_highlight_title": "Was mich auszeichnet",
        "about_highlight_list": """
- Strukturierte, analytische Arbeitsweise  
- Beharrliche Fehlersuche und Troubleshooting  
- Audience-aware Kommunikation (komplexe Themen verständlich erklären)  
- Internationale Offenheit (Remote & Relocation möglich)  
- Fokus auf robuste, wartbare, praxisnahe Lösungen  
        """,

        "projects_title": "Ausgewählte Projekte",
        "project1_title": "Streamlit/PostgreSQL Online Shop",
        "project1_text": (
            "Webanwendung mit Benutzerregistrierung, Login, Produktansicht und Bestellübersicht. "
            "Fokus auf Datenintegrität, Benutzererlebnis und klare Trennung von Logik und Darstellung."
        ),
        "project1_stack": "Tech-Stack: Python, Streamlit, PostgreSQL, Docker",
        "project2_title": "Airflow Workflow Automation",
        "project2_text": (
            "Daten-Pipelines mit Apache Airflow zur Automatisierung wiederkehrender Tasks, "
            "inklusive Trennung von Schema-Erstellung und Datenverarbeitung, Logging und Monitoring."
        ),
        "project2_stack": "Tech-Stack: Python, Airflow, Docker, SQL",
        "project3_title": "Weitere Projekte",
        "project3_text": (
            "Weitere Beispiele für Automatisierung, Datenanalyse und Infrastruktur finden Sie "
            "in meinen GitHub-Repositories. Dort dokumentiere ich auch Lernpfade, Experimente "
            "und Prototypen."
        ),
        "project_repo_link": "GitHub-Repository öffnen",
        "project_all_link": "Alle Projekte auf GitHub ansehen",

        "skills_title": "Skills",
        "skills_tech_title": "Technische Skills",
        "skills_tech_col1": """
- Python  
- SQL & PostgreSQL  
- Apache Airflow  
- Docker  
- ETL & Data Pipelines  
        """,
        "skills_tech_col2": """
- Power BI / Tableau  
- Linux & Cloud-Grundlagen  
- Git & GitHub  
- Streamlit  
        """,
        "skills_soft_title": "Soziale Kompetenz",
        "skills_soft_list": """
- Kommunikationsstärke – technische Inhalte klar und zielgruppengerecht vermitteln  
- Teamfähigkeit – Zusammenarbeit in interdisziplinären und internationalen Teams  
- Beharrlichkeit & Problemlösungskompetenz – auch in komplexen Situationen  
- Interkulturelle Zusammenarbeit – offen für unterschiedliche Arbeitskulturen  
- Anpassungsfähigkeit & Belastbarkeit – fokussiert auch unter Zeitdruck  
        """,

        "contact_title": "Kontakt & Lebenslauf",
        "contact_intro": (
            "Ich bin offen für internationale Projekte, Remote-Rollen und neue Herausforderungen "
            "im Bereich Automatisierung, Datenanalyse und Workflow-Engineering."
        ),
        "contact_email_section": "E-Mail schreiben",
        "contact_gmail_button": "Gmail öffnen",
        "contact_yahoo_button": "Yahoo Mail öffnen",
        "contact_default_mail_button": "Standard-Mailprogramm",
        "contact_phone_title": "📞 Kontakt",
        "contact_phone_intro": "Wenn Sie mich erreichen möchten:",
        "contact_phone_label": "Telefon:",
        "cv_global_title": "📄 Lebenslauf herunterladen",
        "cv_download_label": "📥 Lebenslauf als PDF herunterladen",
        "cv_info_text": "Der Lebenslauf liegt aktuell auf Deutsch vor.",

    },

    "English": {
        "nav_title": "Navigation",
        "nav_about": "About me",
        "nav_projects": "Projects",
        "nav_skills": "Skills",
        "nav_contact": "Contact",
        "links": "Links",
        "github": "GitHub",
        "linkedin": "LinkedIn",

        "header_role": "Electrical Engineer • Software Developer • Automation & Data Analysis • Python • SQL • Airflow • Docker",

        "about_title": "About me",
        "about_text": (
            "I am a specialist in automation, data analytics, and workflow engineering with "
            "experience in Python, SQL, Apache Airflow, Docker, and modern data platforms.\n\n"
            "I build scalable, robust solutions that automate data flows, use cloud resources "
            "efficiently, and deliver clear insights for both technical and non-technical stakeholders."
        ),
        "about_highlight_title": "What sets me apart",
        "about_highlight_list": """
- Structured and analytical way of working  
- Persistent debugging and troubleshooting  
- Audience-aware communication (explaining complex topics clearly)  
- International mindset (open to remote work & relocation)  
- Focus on robust, maintainable, real-world solutions  
        """,

        "projects_title": "Selected projects",
        "project1_title": "Streamlit/PostgreSQL Online Shop",
        "project1_text": (
            "Web application with user registration, login, product view, and order overview. "
            "Focus on data integrity, user experience, and clear separation of logic and presentation."
        ),
        "project1_stack": "Tech stack: Python, Streamlit, PostgreSQL, Docker",
        "project2_title": "Airflow Workflow Automation",
        "project2_text": (
            "Data pipelines with Apache Airflow to automate recurring tasks, including separation "
            "of schema creation and data processing, logging, and monitoring."
        ),
        "project2_stack": "Tech stack: Python, Airflow, Docker, SQL",
        "project3_title": "More projects",
        "project3_text": (
            "You can find further examples of automation, data analytics, and infrastructure "
            "in my GitHub repositories, including learning paths, experiments, and prototypes."
        ),
        "project_repo_link": "Open GitHub repository",
        "project_all_link": "View all projects on GitHub",

        "skills_title": "Skills",
        "skills_tech_title": "Technical skills",
        "skills_tech_col1": """
- Python  
- SQL & PostgreSQL  
- Apache Airflow  
- Docker  
- ETL & data pipelines  
        """,
        "skills_tech_col2": """
- Power BI / Tableau  
- Linux & basic cloud knowledge  
- Git & GitHub  
- Streamlit  
        """,
        "skills_soft_title": "Soft skills",
        "skills_soft_list": """
- Strong communication – explaining technical content clearly to different audiences  
- Teamwork – collaboration in interdisciplinary and international teams  
- Persistence & problem-solving – especially in complex situations  
- Intercultural collaboration – open to different working cultures  
- Adaptability & resilience – focused even under time pressure  
        """,

        "contact_title": "Contact & CV",
        "contact_intro": (
            "I am open to international projects, remote roles, and new challenges in automation, "
            "data analytics, and workflow engineering."
        ),
        "contact_email_section": "Send an email",
        "contact_gmail_button": "Open Gmail",
        "contact_yahoo_button": "Open Yahoo Mail",
        "contact_default_mail_button": "Default mail program",
        "contact_phone_title": "📞 Contact",
        "contact_phone_intro": "If you would like to reach me:",
        "contact_phone_label": "Phone:",
        "cv_global_title": "📄 Download CV",
        "cv_download_label": "📥 Download CV as PDF",
        "cv_info_text": "The CV is currently available in German.",

    },

    "Français": {
        "nav_title": "Navigation",
        "nav_about": "À propos de moi",
        "nav_projects": "Projets",
        "nav_skills": "Compétences",
        "nav_contact": "Contact",
        "links": "Liens",
        "github": "GitHub",
        "linkedin": "LinkedIn",

        "header_role": "Ingénieur en électrotechnique • Développeur logiciel • Automation & Data Analysis • Python • SQL • Airflow • Docker",

        "about_title": "À propos de moi",
        "about_text": (
            "Je suis spécialiste en automatisation, analyse de données et ingénierie de flux de travail, "
            "avec de l'expérience en Python, SQL, Apache Airflow, Docker et plateformes de données modernes.\n\n"
            "Je conçois des solutions robustes et évolutives qui automatisent les flux de données, "
            "optimisent l'utilisation des ressources cloud et fournissent des informations claires pour "
            "les parties prenantes techniques et non techniques."
        ),
        "about_highlight_title": "Ce qui me distingue",
        "about_highlight_list": """
- Approche de travail structurée et analytique  
- Persévérance dans le débogage et la résolution de problèmes  
- Communication adaptée au public (explication claire de sujets complexes)  
- Ouverture internationale (remote & relocalisation possibles)  
- Focalisation sur des solutions robustes, maintenables et concrètes  
        """,

        "projects_title": "Projets sélectionnés",
        "project1_title": "Boutique en ligne Streamlit/PostgreSQL",
        "project1_text": (
            "Application web avec inscription des utilisateurs, connexion, vue produit et résumé des commandes. "
            "Accent sur l'intégrité des données, l'expérience utilisateur et une séparation claire entre logique "
            "et présentation."
        ),
        "project1_stack": "Stack technique : Python, Streamlit, PostgreSQL, Docker",
        "project2_title": "Automatisation de workflows avec Airflow",
        "project2_text": (
            "Pipelines de données avec Apache Airflow pour automatiser des tâches récurrentes, "
            "incluant la séparation entre création de schéma et traitement des données, journalisation "
            "et monitoring."
        ),
        "project2_stack": "Stack technique : Python, Airflow, Docker, SQL",
        "project3_title": "Autres projets",
        "project3_text": (
            "Vous trouverez d'autres exemples d'automatisation, d'analyse de données et d'infrastructure "
            "dans mes dépôts GitHub, y compris des parcours d'apprentissage, des expériences et des prototypes."
        ),
        "project_repo_link": "Ouvrir le dépôt GitHub",
        "project_all_link": "Voir tous les projets sur GitHub",

        "skills_title": "Compétences",
        "skills_tech_title": "Compétences techniques",
        "skills_tech_col1": """
- Python  
- SQL & PostgreSQL  
- Apache Airflow  
- Docker  
- ETL & pipelines de données  
        """,
        "skills_tech_col2": """
- Power BI / Tableau  
- Linux & bases du cloud  
- Git & GitHub  
- Streamlit  
        """,
        "skills_soft_title": "Compétences relationnelles",
        "skills_soft_list": """
- Excellentes capacités de communication – expliquer clairement le contenu technique  
- Travail en équipe – collaboration dans des équipes interdisciplinaires et internationales  
- Persévérance & résolution de problèmes – même dans des situations complexes  
- Collaboration interculturelle – ouverture à différentes cultures de travail  
- Adaptabilité & résistance au stress – concentré même sous pression  
        """,

        "contact_title": "Contact & CV",
        "contact_intro": (
            "Je suis ouvert aux projets internationaux, aux postes en remote et aux nouveaux défis "
            "dans les domaines de l'automatisation, de l'analyse de données et de l'ingénierie des workflows."
        ),
        "contact_email_section": "Envoyer un e-mail",
        "contact_gmail_button": "Ouvrir Gmail",
        "contact_yahoo_button": "Ouvrir Yahoo Mail",
        "contact_default_mail_button": "Programme de messagerie par défaut",
        "contact_phone_title": "📞 Contact",
        "contact_phone_intro": "Pour me joindre :",
        "contact_phone_label": "Téléphone :",
        "cv_global_title": "📄 Télécharger le CV",
        "cv_download_label": "📥 Télécharger le CV en PDF",
        "cv_info_text": "Le CV est actuellement disponible en allemand.",
    },
}

t = texts[language]

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title(t["nav_title"])
page = st.sidebar.radio(
    t["nav_title"],
    [t["nav_about"], t["nav_projects"], t["nav_skills"], t["nav_contact"]]
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**{t['links']}**")
st.sidebar.markdown(f"[{t['github']}](https://github.com/gassayossa45/Projekt)")
st.sidebar.markdown(f"[{t['linkedin']}](https://www.linkedin.com/in/amédée-gaël-gassa-yossa-545363396)")

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
            f"""
            <div style="padding-top:10px;">
                <span style="font-size:28px; font-weight:700;">Amedee Gael Gassa Yossa</span><br>
                <span style="font-size:16px; color:#9CA3AF;">
                 {t['header_role']}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("---")

# Header auf allen Seiten
render_header()

# ---------------------------------------------------------
# ÜBER MICH / ABOUT
# ---------------------------------------------------------
if page == t["nav_about"]:
    st.subheader(t["about_title"])

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            # Optional: Profilbild hier noch einmal anzeigen, wenn gewünscht
            # st.image("lebenslauf_self.jpg", width=260)
            st.write("")
        except Exception:
            st.info("Profilbild: Datei 'lebenslauf_self.jpg' noch nicht vorhanden.")

    with col2:
        st.write(t["about_text"])

        st.markdown(f"#### {t['about_highlight_title']}")
        st.markdown(t["about_highlight_list"])

# ---------------------------------------------------------
# PROJEKTE / PROJECTS
# ---------------------------------------------------------
elif page == t["nav_projects"]:
    st.subheader(t["projects_title"])

    # Projekt 1
    st.markdown(f"### {t['project1_title']}")
    st.write(t["project1_text"])
    st.markdown(f"**{t['project1_stack']}**")
    st.markdown(f"[{t['project_repo_link']}](https://github.com/gassayossa45/Projekt)")

    st.markdown("---")

    # Projekt 2
    st.markdown(f"### {t['project2_title']}")
    st.write(t["project2_text"])
    st.markdown(f"**{t['project2_stack']}**")
    st.markdown(f"[{t['project_repo_link']}](https://github.com/gassayossa45/Projekt)")

    st.markdown("---")

    # Projekt 3 – allgemeiner Verweis
    st.markdown(f"### {t['project3_title']}")
    st.write(t["project3_text"])
    st.markdown(f"[{t['project_all_link']}](https://github.com/gassayossa45/Projekt)")

# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
elif page == t["nav_skills"]:
    st.subheader(t["skills_title"])

    st.markdown(f"#### {t['skills_tech_title']}")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(t["skills_tech_col1"])

    with col2:
        st.markdown(t["skills_tech_col2"])

    st.markdown(f"#### {t['skills_soft_title']}")
    st.markdown(t["skills_soft_list"])

# ---------------------------------------------------------
# KONTAKT
# ---------------------------------------------------------
elif page == t["nav_contact"]:
    st.subheader(t["contact_title"])

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            # Optional: Profilbild hier
            # st.image("lebenslauf_self.jpg", width=220)
            st.write("")
        except Exception:
            st.info("Profilbild: Datei 'lebenslauf_self.jpg' noch nicht vorhanden.")

    with col2:
        st.write(t["contact_intro"])

        st.markdown(f"### {t['contact_email_section']}")

        # Gmail Button
        st.markdown(
            f"""
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
                    {t['contact_gmail_button']}
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

        # Yahoo Button
        st.markdown(
            f"""
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
                    {t['contact_yahoo_button']}
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )

        # Standard-Mailprogramm
        st.markdown(
            f"""
            <a href="mailto:gassa45@yahoo.com" 
            style="text-decoration:none;">
                <button style="
                    padding:10px 18px; 
                    border-radius:8px; 
                    border:none; 
                    background:#0F9D58; 
                    color:white;
                    cursor:pointer;">
                    {t['contact_default_mail_button']}
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
        st.subheader(t["contact_phone_title"])

        st.write(t["contact_phone_intro"])

        st.markdown(f"""
        **{t['contact_phone_label']}** +49 152 13629046   
        """)

# ---------------------------------------------------------
# Lebenslauf Download (global, unter allen Seiten)
# ---------------------------------------------------------
st.markdown(f"### {t['cv_global_title']}")
st.write(t["cv_info_text"])

try:
    with open("Lebenslaufgassa.pdf", "rb") as pdf:
        pdf_bytes = pdf.read()

    st.download_button(
        label=t["cv_download_label"],
        data=pdf_bytes,
        file_name="Lebenslaufgassa.pdf",
        mime="application/pdf"
    )
except FileNotFoundError:
    st.error("Die Datei 'Lebenslaufgassa.pdf' wurde nicht gefunden. Bitte sicherstellen, dass sie im gleichen Ordner liegt.")