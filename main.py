import streamlit as st

# Setzen der Seitenüberschrift und des Titels
st.set_page_config(page_title="Time Pro", page_icon=":muscle:", layout="centered")

# Überschrift anzeigen
st.title("Time Pro")

# Weitere Inhalte hinzufügen (optional)
st.write("""
    Willkommen auf der Webseite für das optimale Trainingstiming!
    Hier kannst du mehr über den besten Zeitpunkt für dein Training erfahren.
    Lass uns herausfinden, wie du dein Training am effektivsten gestalten kannst!
""")

# Ein Button, um interaktive Elemente hinzuzufügen
if st.button('Mehr erfahren'):
    st.write("Das ideale Trainingstiming hängt von verschiedenen Faktoren ab, z.B. Tageszeit, Ernährung und Schlaf.")

# Hier sollte im weiteren Verlauf unseres projektes die Funktionen eingebunden werden, die die Daten auswerten und visualisieren.Um damit die Nutzer:innen zu unterstützen, den optimalen Zeitpunkt für ihr Training zu finden.
