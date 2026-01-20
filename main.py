import asyncio
from droidrun import DroidAgent, DroidrunConfig, AgentConfig, LoggingConfig, TracingConfig


async def main():
    # 1. Setup Config (Keep this standard)

    config = DroidrunConfig(
        agent=AgentConfig(max_steps=100),
        logging=LoggingConfig(debug=True, save_trajectory="none"),
        tracing=TracingConfig(enabled=True, provider="phoenix")
    )

    print("### Train ticketing Automation using droidrun ###")
    print("____________________________________________________")
    print("Please provide the following details:")
    train_no = input("Enter train no:")
    date_of_journey = input("Enter date of journey:")
    passenger_name = input("Enter passenger name:")
    gender = input("Enter gender")
    age = input("Enter age:")
    coach_class = input("Enter coach class:")
    berth_preference = input("Enter berth preference:")
    boarding_city = input("Enter boarding city:")
    destination_city = input("Enter destination city:")

    # 2. Create Agent with max_steps
    agent = DroidAgent(
        goal=f"Open ixigo trains app and book a ticket from {boarding_city} to {destination_city} on {date_of_journey}, train no. {train_no}, class {coach_class} for passenger {passenger_name},gender: {gender}, berth preference: {berth_preference} click on the book now button and proceed to payment, I would enter the pin",
        config=config,
   
    )


 # Run agent
    result = await agent.run()

    # Check results (result is a ResultEvent object)
    print(f"Success: {result.success}")
    print(f"Reason: {result.reason}")
    print(f"Steps: {result.steps}")

if __name__ == "__main__":
    asyncio.run(main())
