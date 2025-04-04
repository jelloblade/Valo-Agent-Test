
import streamlit as st
import pandas as pd

# Define criteria and explanations
criteria = {
    "A": "Raw Aim Potential",
    "B": "Movement Freedom / Mobility",
    "C": "Solo Carry Potential",
    "D": "Utility for Entry / Fragging",
    "E": "Setups / Traps / Passive Control",
    "F": "Information Gathering",
    "G": "Team Support / Buffs / Healing",
    "H": "Smokes / Map Control",
    "I": "Flashes / Blind Initiation",
    "J": "Lineups / Post-Plant Utility",
    "K": "Disruption / Chaos / Confusion",
    "L": "Lurk Playstyle / Off-Timing Focus",
    "M": "Resilience / Second Chances",
    "N": "Aggressive Entry Initiator",
    "O": "Silent / Covert Playstyle",
    "P": "Anchor / Site Lockdown Role"
}

# Agent to criteria mapping
agent_criteria = {
    "Jett": ["A", "B", "C", "N"],
    "Phoenix": ["A", "D", "I", "M"],
    "Reyna": ["A", "C", "L", "M"],
    "Raze": ["A", "B", "D", "K"],
    "Yoru": ["B", "K", "O", "L"],
    "Neon": ["A", "B", "N", "K"],
    "Iso": ["A", "C", "L", "M"],
    "Waylay": ["A", "B", "K", "O", "L"],
    "Sova": ["F", "J", "D", "L"],
    "Breach": ["I", "D", "N", "K"],
    "Skye": ["F", "G", "I", "D"],
    "KAY/O": ["F", "I", "D", "K"],
    "Fade": ["F", "K", "D", "L"],
    "Gekko": ["F", "G", "D", "I"],
    "Tejo": ["D", "K", "F", "J"],
    "Brimstone": ["H", "J", "P", "D"],
    "Viper": ["H", "J", "P", "E"],
    "Omen": ["H", "K", "O", "P"],
    "Astra": ["H", "J", "P", "F"],
    "Harbor": ["H", "G", "P", "D"],
    "Clove": ["K", "M", "H", "O"],
    "Sage": ["G", "M", "P", "J"],
    "Cypher": ["E", "F", "P", "L"],
    "Killjoy": ["E", "P", "J", "F"],
    "Chamber": ["A", "E", "L", "P"],
    "Deadlock": ["P", "E", "F", "G"],
    "Vyse": ["E", "F", "K", "P"]
}

st.title("Valorant Agent Match Finder")
st.markdown("**Rank your top 4–6 criteria** to find the agent that best fits your playstyle.")

# User input: rank top 6 criteria
selections = []
cols = st.columns(3)
options = list(criteria.items())
for i in range(6):
    with cols[i % 3]:
        pick = st.selectbox(f"Rank {i+1}", [""] + [f"{k} - {v}" for k, v in options if f"{k} - {v}" not in selections], key=f"rank_{i}")
        if pick:
            selections.append(pick)

ranked_letters = [s.split(" - ")[0] for s in selections if s]

# Match logic
if ranked_letters:
    scores = []
    for agent, tags in agent_criteria.items():
        score = sum([(len(ranked_letters) - i) for i, letter in enumerate(ranked_letters) if letter in tags])
        if score > 0:
            scores.append((agent, score))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    st.markdown("### Best Matching Agents:")
    for agent, score in sorted_scores[:10]:
        st.write(f"**{agent}** – Match Score: {score}")
