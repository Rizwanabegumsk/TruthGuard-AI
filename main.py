from agents import generator_agent, skeptic_agent, research_agent, corrector_agent

question = input("Ask something: ")

gen = generator_agent(question)
skeptic = skeptic_agent(gen)
research = research_agent(skeptic)
final = corrector_agent(research, gen, skeptic)

print("\n" + "="*50)
print(" TRUTHGUARD AI SYSTEM")
print("="*50)

print("\n Generator:\n", gen)
print("\n Skeptic:\n", skeptic)
print("\n Research:\n", research)
print("\n Final Answer:\n", final)

print("\n" + "="*50)
