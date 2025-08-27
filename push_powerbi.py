import requests
import json
import random
import datetime
import time

POWER_BI_PUSH_URL = "https://api.powerbi.com/beta/73909f4c-6643-4341-beaf-0452e917e087/datasets/82157fef-2708-4f43-b2d8-8cbf5b9e1c5f/rows?experience=power-bi&selectedWorkspaceObjectId=me&key=xMVckmPTBJXuOGgmjBSnw6GziHMvMF16JfD0mVtewdN7ARXQhtAHQFVK9AIcug60LfRfw6HQXc%2FzN5pvxptn2w%3D%3D "

def push_data():
    while True:
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(20.0, 35.0), 2)  
        status = random.choice(["Normal", "Warning", "Critical"])
        
        data = [{
            "time": now,
            "temperature": temperature,
            "status": status
        }]
        
        response = requests.post(
            POWER_BI_PUSH_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        
        if response.status_code == 200:
            print(f"✅ Data sent: {data}")
        else:
            print(f"❌ Failed ({response.status_code}): {response.text}")
        
        time.sleep(5)

if __name__ == "__main__":
    push_data()
