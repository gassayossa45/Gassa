import streamlit as st
import psycopg2
import bcrypt
from datetime import datetime, date

# =========================
# Datenbankverbindung
# =========================
def get_connection():
    return psycopg2.connect(
        dbname="OlineShop",
        user="postgres",
        password="Gassa2012!&237",
        host="localhost",
        port="5432"
    )

# =========================
# Benutzer-Funktionen
# =========================
def register_user(name, email, password):
    conn = get_connection()
    cur = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cur.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
            (name, email, psycopg2.Binary(password_hash))
        )
        conn.commit()
        st.success("Registrierung erfolgreich!")
    except Exception as e:
        conn.rollback()
        st.error(f"Fehler: {e}")
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, password_hash FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode('utf-8'), bytes(user[2])):
        return user
    return None

# =========================
# Produkt- und Bestell-Funktionen
# =========================
def get_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description, price, stock, image_url FROM products")
    products = cur.fetchall()
    conn.close()
    return products

def place_order(user_id, product_id, quantity):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Bestand nur reduzieren, wenn ausreichend vorhanden
        cur.execute(
            "UPDATE products SET stock = stock - %s WHERE id = %s AND stock >= %s",
            (quantity, product_id, quantity)
        )
        if cur.rowcount == 0:
            raise Exception("Nicht genug Bestand für dieses Produkt.")
        # Bestellung speichern
        cur.execute(
            "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)",
            (user_id, product_id, quantity)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        st.error(f"Bestellung fehlgeschlagen: {e}")
        raise
    finally:
        conn.close()

def get_orders(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT o.id, p.name, o.quantity, o.order_date
        FROM orders o
        JOIN products p ON o.product_id = p.id
        WHERE o.user_id = %s
        ORDER BY o.order_date DESC
    """, (user_id,))
    orders = cur.fetchall()
    conn.close()
    return orders

def get_all_orders(filter_customer=None, filter_product=None, start_date=None, end_date=None):
    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT o.id, u.name, p.name, o.quantity, o.order_date
        FROM orders o
        JOIN users u ON o.user_id = u.id
        JOIN products p ON o.product_id = p.id
        WHERE 1=1
    """
    params = []
    if filter_customer:
        query += " AND u.name ILIKE %s"
        params.append(f"%{filter_customer}%")
    if filter_product:
        query += " AND p.name ILIKE %s"
        params.append(f"%{filter_product}%")
    if start_date:
        # Startdatum inkl. Tagesbeginn
        query += " AND o.order_date >= %s"
        params.append(datetime.combine(start_date, datetime.min.time()))
    if end_date:
        # Enddatum inkl. Tagesende
        query += " AND o.order_date <= %s"
        params.append(datetime.combine(end_date, datetime.max.time()))
    query += " ORDER BY o.order_date DESC"
    cur.execute(query, tuple(params))
    orders = cur.fetchall()
    conn.close()
    return orders

# =========================
# UI: Titel und Session-Infos
# =========================
st.title("🛒 Mein kleiner Online-Shop")

# Benutzeranzeige/Logout
if "user" in st.session_state and st.session_state["user"]:
    st.write(f"👤 Angemeldet als: {st.session_state['user']['name']}")
    if st.button("Logout"):
        st.session_state["user"] = None
        st.success("Erfolgreich abgemeldet!")

# Menü mit allen Bereichen
menu = st.sidebar.selectbox(
    "Menü",
    ["Login", "Registrieren", "Shop", "Meine Bestellungen", "Admin", "Bestellungen Übersicht"]
)

# =========================
# Registrierung
# =========================
if menu == "Registrieren":
    st.subheader("Neuen Benutzer registrieren")
    name = st.text_input("Name")
    email = st.text_input("E-Mail")
    password = st.text_input("Passwort", type="password")
    if st.button("Registrieren"):
        if not name or not email or not password:
            st.error("Bitte alle Felder ausfüllen.")
        else:
            register_user(name, email, password)

# =========================
# Login
# =========================
elif menu == "Login":
    st.subheader("Login")
    email = st.text_input("E-Mail")
    password = st.text_input("Passwort", type="password")
    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.session_state["user"] = {
                "id": user[0],
                "name": user[1],
                "email": email
            }
            st.success(f"Willkommen, {user[1]}!")
        else:
            st.error("Login fehlgeschlagen")

# =========================
# Shop
# =========================
elif menu == "Shop":
    if "user" in st.session_state and st.session_state["user"]:
        st.subheader("Produkte")
        products = get_products()
        if "cart" not in st.session_state:
            st.session_state["cart"] = []

        cols = st.columns(3)
        for idx, p in enumerate(products):
            with cols[idx % 3]:
                if p[5]:
                    st.image(p[5], width=150)
                st.write(f"**{p[1]}**")
                st.write(p[2] or "")
                st.write(f"Preis: {p[3]} €")
                st.write(f"Verfügbar: {p[4]}")
                disabled = p[4] <= 0
                if st.button(f"In den Warenkorb: {p[1]}", key=f"add_{p[0]}", disabled=disabled):
                    st.session_state["cart"].append(p)
                if disabled:
                    st.caption("Ausverkauft")

        st.write("### Warenkorb")
        if st.session_state["cart"]:
            cart_table = [{"Produkt": item[1], "Preis (€)": item[3]} for item in st.session_state["cart"]]
            st.table(cart_table)
            total = sum(item[3] for item in st.session_state["cart"])
            st.write(f"**Gesamtsumme: {total:.2f} €**")
            if st.button("Bestellung abschließen"):
                try:
                    for item in st.session_state["cart"]:
                        place_order(st.session_state["user"]["id"], item[0], 1)
                    st.success("Bestellung erfolgreich abgeschlossen!")
                    st.session_state["cart"] = []
                except Exception:
                    st.error("Eine oder mehrere Positionen konnten nicht bestellt werden.")
        else:
            st.write("Dein Warenkorb ist leer.")
    else:
        st.warning("Bitte zuerst einloggen!")

# =========================
# Meine Bestellungen
# =========================
elif menu == "Meine Bestellungen":
    if "user" in st.session_state and st.session_state["user"]:
        st.subheader("Meine Bestellungen")
        orders = get_orders(st.session_state["user"]["id"])
        if orders:
            st.table([
                {"Bestell-ID": o[0], "Produkt": o[1], "Menge": o[2], "Datum": o[3].strftime("%Y-%m-%d %H:%M")}
                for o in orders
            ])
        else:
            st.info("Du hast bisher keine Bestellungen.")
    else:
        st.warning("Bitte zuerst einloggen!")

# =========================
# Admin – Produktverwaltung
# =========================
elif menu == "Admin":
    st.subheader("Admin-Bereich – Produktverwaltung")

    st.write("### Neues Produkt hinzufügen")
    new_name = st.text_input("Produktname")
    new_desc = st.text_area("Beschreibung")
    new_price = st.number_input("Preis (€)", min_value=0.0, format="%.2f")
    new_stock = st.number_input("Bestand", min_value=0)
    new_image = st.text_input("Bild-URL")

    if st.button("Produkt hinzufügen"):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products (name, description, price, stock, image_url) VALUES (%s, %s, %s, %s, %s)",
            (new_name, new_desc, new_price, new_stock, new_image)
        )
        conn.commit()
        conn.close()
        st.success(f"Produkt '{new_name}' wurde hinzugefügt!")

    st.write("### Bestehende Produkte")
    products = get_products()
    for p in products:
        st.write(f"**{p[1]}** – Bestand: {p[4]}, Preis: {p[3]} €")
        col1, col2, col3 = st.columns(3)
        with col1:
            new_stock_val = st.number_input(f"Neuer Bestand für {p[1]}", min_value=0, value=int(p[4]), key=f"stock_{p[0]}")
        with col2:
            new_price_val = st.number_input(f"Neuer Preis für {p[1]}", min_value=0.0, value=float(p[3]), format="%.2f", key=f"price_{p[0]}")
        with col3:
            new_image_val = st.text_input(f"Neue Bild-URL für {p[1]}", value=p[5] or "", key=f"image_{p[0]}")

        c1, c2 = st.columns(2)
        with c1:
            if st.button(f"Update {p[1]}", key=f"update_{p[0]}"):
                conn = get_connection()
                cur = conn.cursor()
                cur.execute(
                    "UPDATE products SET stock = %s, price = %s, image_url = %s WHERE id = %s",
                    (new_stock_val, new_price_val, new_image_val, p[0])
                )
                conn.commit()
                conn.close()
                st.success(f"Produkt '{p[1]}' wurde aktualisiert!")
        with c2:
            if st.button(f"Löschen {p[1]}", key=f"delete_{p[0]}"):
                conn = get_connection()
                cur = conn.cursor()
                cur.execute("DELETE FROM products WHERE id = %s", (p[0],))
                conn.commit()
                conn.close()
                st.warning(f"Produkt '{p[1]}' wurde gelöscht!")

# =========================
# Admin – Bestellungen Übersicht
# =========================
elif menu == "Bestellungen Übersicht":
    st.subheader("📦 Alle Bestellungen (Admin)")

    # Filter
    with st.expander("Filter anzeigen"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            filter_customer = st.text_input("Filter Kunde (Name enthält)")
            start_date = st.date_input("Startdatum", value=None)
        with col_f2:
            filter_product = st.text_input("Filter Produkt (Name enthält)")
            end_date = st.date_input("Enddatum", value=None)

        sd = start_date if start_date else None
        ed = end_date if end_date else None

    orders = get_all_orders(
        filter_customer=filter_customer if filter_customer else None,
        filter_product=filter_product if filter_product else None,
        start_date=sd,
        end_date=ed
    )

    if orders:
        st.table([
            {"Bestell-ID": o[0], "Kunde": o[1], "Produkt": o[2], "Menge": o[3], "Datum": o[4].strftime("%Y-%m-%d %H:%M")}
            for o in orders
        ])
        st.caption(f"Anzahl Bestellungen: {len(orders)}")
    else:
        st.info("Es liegen keine Bestellungen für die gewählten Filter vor.")
st.image("images/lisenz.jpg",width=50)