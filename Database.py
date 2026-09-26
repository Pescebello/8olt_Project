#    []   {}   |

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(103)
num_tickets = 1000

tickets_IDs = [f'BLT-{0 + i}' for i in range(num_tickets)]
categories = ['Payment & Refund', 'Lost item', 'Account and security', 'Trip experience', 'Late delivery', 'App Bug']
category_probs = [0.35, 0.05, 0.25, 0.15, 0.15, 0.05]
ticket_categories = np.random.choice(categories, size=num_tickets, p=category_probs)

priority = ["Low", "Medium", "High", "Urgent"]
priority_probs = [0.40, 0.30, 0.20, 0.10]
ticket_priority = np.random.choice(priority, size=num_tickets, p=priority_probs)

customer_tiers = ["Free", "Standard", "Premium"]
tiers_probs = [0.5, 0.3, 0.2]
tkt_customer_tiers = np.random.choice(customer_tiers, size=num_tickets, p=tiers_probs)

def assign_priority(tier: str):

    if tier == "Premium":
        return "Urgent"
    elif tier == "Standard":
        return np.random.choice(["High", "Urgent"], p=[0.7, 0.3])
    else:
        return np.random.choice(["Low", "Medium", "High"], p=[0.6, 0.3, 0.1])

ticket_priority = [assign_priority(tier) for tier in tkt_customer_tiers]

channel = ["Email", "Live Chat", "Web Form", "In-App Ticket"]
channel_probs = [0.10, 0.65, 0.10, 0.15]
ticket_channel = np.random.choice(channel, size=num_tickets, p=channel_probs)


language = ['Italian', 'English', 'Estonian']
lang_probs = [0.80, 0.10, 0.10]
ticket_languages = np.random.choice(language, size=num_tickets, p=lang_probs)

start_date = datetime(2026, 6, 1)
created_at = [start_date + timedelta(
    days=np.random.randint(0, 30),
    hours=np.random.randint(0, 24),
    minutes=np.random.randint(0, 60))
              for i in range(num_tickets)]

T_Res_T_Min = np.random.lognormal(mean=3.5, sigma=0.8, size=num_tickets).astype(int)
T_Res_T_Min = np.clip(T_Res_T_Min, 5, 1440)

csat_score = []
for T_Res_T in T_Res_T_Min:
    if T_Res_T > 300:
        score = np.random.choice([1, 2, 3, 4, 5], p=[0.4, 0.3, 0.15, 0.1, 0.05])
    elif T_Res_T < 30:
        score = np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.05, 0.1, 0.3, 0.5])
    else:
        score = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.1, 0.3, 0.4, 0.1])

    csat_score.append(score)

df = pd.DataFrame({
    'tickets_ID': tickets_IDs,
    'created_at': created_at,
    'category': ticket_categories,
    'language': ticket_languages,
    'resolution_time_min': T_Res_T_Min,
    'csat': csat_score,
    'priority' : ticket_priority,
    'channel' : ticket_channel,
    'customer_tier' : tkt_customer_tiers,
})

df.to_csv('ßolt_ticket_data.csv', index=False)

print(df.head)