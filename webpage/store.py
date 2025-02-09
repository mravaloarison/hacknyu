import streamlit as st
from PIL import Image
import random

# Set the page configuration
st.set_page_config(page_title="Store", page_icon="🛒", layout="wide")

# Custom CSS to style the page
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: white;
        font-family: Arial, sans-serif;
    }
    
    .navbar {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #2c2c2c;
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
    }
    
    .coin-balance-container {
        display: flex;
        align-items: center;
        font-size: 18px;
        color: #00ff00;
    }

    .coin-balance {
        margin-left: 10px;
    }

    .reward-button {
        background-color: #00ff00;
        border: none;
        color: #1a1a1a;
        padding: 12px 25px;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
        margin: 10px;
    }

    .reward-button:hover {
        background-color: #cccccc;
    }

    .reward-section {
        margin-top: 120px;
        padding: 20px;
        background-color: #2c2c2c;
        border-radius: 10px;
        color: white;
    }

    .reward-title {
        font-size: 24px;
        color: #00ff00;
        margin-bottom: 20px;
    }

    .reward-description {
        font-size: 16px;
        color: #cccccc;
    }
    </style>
""", unsafe_allow_html=True)

# Simulated initial coin balance
coins = 10

# Reward options
rewards = [
    {"name": "1 Meal to those in need", "cost":2},
    {"name": "3 Meal to those in need", "cost": 5},
    {"name": "5 Meal to those in need", "cost": 10},
    {"name": "10 Meal to those in need", "cost": 15},
]

# Navbar with coin balance at the top-right corner
st.markdown("""
    <div class="navbar">
""", unsafe_allow_html=True)

# Display the animated coin GIF using st.image (increased size)
coin_icon_path = "animated_coin.gif"  # Ensure the GIF file is in the same directory as your script
st.image(coin_icon_path, width=50)  # Increase size to 50px for better visibility

# Display the current coin balance (just the number, no "Coins:" text)
st.markdown(f"""
    <div class="coin-balance-container">
        <span>{coins}</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    </div>
""", unsafe_allow_html=True)

# Reward redemption section
st.markdown("<div class='reward-section'>", unsafe_allow_html=True)
st.markdown("<div class='reward-title'>Available Rewards</div>", unsafe_allow_html=True)

# Display each reward option with buttons for redemption
for reward in rewards:
    st.markdown(f"""
        <div>
            <span class="reward-title">{reward['name']}</span>
            <p class="reward-description">Cost: {reward['cost']} coins</p>
            <button class="reward-button" onclick="alert('Redeemed {reward['name']} for {reward['cost']} coins!')">Redeem</button>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Transaction Simulation: Redeem coins
def redeem_coins(selected_reward):
    global coins
    if coins >= selected_reward["cost"]:
        coins -= selected_reward["cost"]
        st.success(f"Successfully redeemed {selected_reward['name']} for {selected_reward['cost']} coins!")
    else:
        st.error(f"Not enough coins to redeem {selected_reward['name']}.")

# Select a reward and redeem it (simulate the transaction)
reward_name = st.selectbox("Select a reward", [reward["name"] for reward in rewards])
if st.button("Redeem"):
    selected_reward = next(reward for reward in rewards if reward["name"] == reward_name)
    redeem_coins(selected_reward)

# Simulate a Solana Transaction (for demonstration purposes)
def solana_transaction_simulation(reward_name, cost):
    # Here we would interact with Solana's blockchain to process the transaction.
    # For demonstration, we simulate a successful transaction.
    transaction_result = random.choice(["Success", "Failure"])
    if transaction_result == "Success":
        st.success(f"Solana transaction successful: {reward_name} redeemed for {cost} coins.")
    else:
        st.error("Transaction failed, please try again.")

# If a reward is redeemed, simulate the transaction
if coins < 10:
    solana_transaction_simulation(reward_name, selected_reward["cost"])
