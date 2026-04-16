import streamlit as st
from agents import generator_agent, skeptic_agent, research_agent, corrector_agent

st.title("TruthGuard AI")

question = st.text_input("Ask something:")

if st.button("Analyze"):

    if question:
        gen = generator_agent(question)
        skeptic = skeptic_agent(gen)
        research = research_agent(skeptic)
        final = corrector_agent(research, gen, skeptic)

        st.subheader("Generator")
        st.write(gen)

        st.subheader("Skeptic")
        st.write(skeptic)

        st.subheader("Research")
        st.write(research)

        st.subheader("Final Answer")
        st.write(final)

    else:
        st.warning("Please enter a question")