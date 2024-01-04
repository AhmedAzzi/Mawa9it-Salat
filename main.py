import requests
import tkinter as tk
from tkinter import ttk


def fetch_prayer_times():
    city, country = city_field.get(), country_field.get(),
    if city and country:
        url = f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={8}"
        try:
            response = requests.get(url)
            info = response.json()
            if "data" in info:
                timings = info["data"]["timings"]
                i = 4
                for key, value in timings.items():
                    if key not in ["Sunrise", "Sunset", "Imsak", "Midnight", "Firstthird", "Lastthird"]:
                        ttk.Label(frame, text=key).grid(
                            row=i, column=0, padx=50, pady=10)
                        ttk.Label(frame, text=value).grid(
                            row=i, column=1, padx=50, pady=10)
                        i += 1
            else:
                return None
        except Exception as e:
            return f"Unxpected error pccured {e}"
    else:
        country_field.insert(0, data.get("country"))
        city_field.insert(0, data.get("city"))
        
if __name__ == "__main__":
    ip = requests.get("https://api.ipify.org").text
    data = requests.get(f"http://ip-api.com/json/{ip}").json()

    root = tk.Tk()
    root.title('Prayer Times')

    frame = ttk.Frame(root, padding=20)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text='City:').grid(row=0, column=0, padx=50)

    city_field = ttk.Entry(frame)
    city_field.insert(0, data.get("city"))
    city_field.grid(row=0, column=1, pady=10)

    ttk.Label(frame, text='Country:').grid(row=1, column=0, padx=50)

    country_field = ttk.Entry(frame)
    country_field.insert(0, data.get("country"))
    country_field.grid(row=1, column=1, pady=10)

    ttk.Button(
        frame, text='Fetch Prayer Time', command=fetch_prayer_times).grid(row=3, column=0, pady=10, columnspan=2)

    root.mainloop()
