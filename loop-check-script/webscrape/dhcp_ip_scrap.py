import pandas as pd

def get_dhcp_ip_pool(wing_number, side, floor):
    # Load the CSV file into a DataFrame
    df = pd.read_csv('Hostel_02_IP_Alloc.csv')  # Replace 'your_csv_file.csv' with your CSV file path
    
    # Drop rows with missing values in 'Wing/Floor' column
    df = df.dropna(subset=['Wing/Floor'])
    
    # Create a filter condition based on input values
    filter_condition = (df['Wing/Floor'].str.contains(f'Wing {wing_number} {side}, Floor {floor}')) 
    
    # Apply the filter to get matching rows
    matching_rows = df[filter_condition]
    
    # Extract the corresponding DHCP IP Pool values
    dhcp_ip_pools = matching_rows['DHCP IP Pool'].tolist()
    
    return dhcp_ip_pools

# Example usage

#wing_number = 2
#side = 'Left'
#floor = 0

#dhcp_ip_pools = get_dhcp_ip_pool(wing_number, side, floor)
#print(dhcp_ip_pools)
