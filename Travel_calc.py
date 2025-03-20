import pandas as pd



def calculate_travel_costs(num_athletes, num_coaches, days):
    
    sgl_price = 150  
    twin_price = 190  
    lunch_price = 35
    dinner_price = 45
    transfer_hotel_airport = 1600
    transfer_pool_hotel = 5750
    gym_price = 1800
    pool_price = 8050
    
    total_people = num_athletes + num_coaches
    num_twin = num_athletes // 2  
    num_sgl = num_coaches  
    
    # Проживання
    twin_total = num_twin * twin_price * days
    sgl_total = num_sgl * sgl_price * days
    
    #Харчування
    lunch_total = lunch_price * total_people * days
    dinner_total = dinner_price * total_people * days
    
    # Загальна вартість
    accommodation_total = twin_total + sgl_total
    services_total = (transfer_hotel_airport + transfer_pool_hotel +
                      lunch_total + dinner_total + gym_price + pool_price)
    total_cost = accommodation_total + services_total
    
    
    cost_per_person_sgl_per_day = sgl_total / (num_sgl * days) if num_sgl else 0
    cost_per_person_twin_per_day = twin_total / (num_twin * 2 * days) if num_twin else 0
    
    
    data = {
        "Category": ["Twin", "SGL", "Transfers hotel-airport", "Transfer pool-hotel",
                     "Lunch", "Dinner", "Gym", "Pool", "Total"],
        "Cost": [twin_total, sgl_total, transfer_hotel_airport, transfer_pool_hotel,
                 lunch_total, dinner_total, gym_price, pool_price, total_cost]
    }
    df = pd.DataFrame(data)
    
    df_per_person = pd.DataFrame({
        "Category": ["Trip price per person in SGL per day", "Trip price per person in TWIN per day"],
        "Cost": [cost_per_person_sgl_per_day, cost_per_person_twin_per_day]
    })
    
    
    output_path = "travel_costs.xlsx"
    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, sheet_name="Total Costs", index=False)
        df_per_person.to_excel(writer, sheet_name="Cost per Person", index=False)
    
    print(f"Файл з розрахунками збережено: {output_path}")

calculate_travel_costs(num_athletes=20, num_coaches=6, days=15)
